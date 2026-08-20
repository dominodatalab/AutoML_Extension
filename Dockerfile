# AutoGluon-powered environment for Tabular, TimeSeries, and Multimodal ML
# Compatible with Domino Data Lab compute environments

#
# Required Domino Environment Base Image: python:3.10-slim-bullseye
#

LABEL maintainer="Domino Data Lab"
LABEL description="AutoGluon AutoML environment for Domino Data Lab"
ARG EXTENSION_VERSION=${EXTENSION_VERSION:-main}
LABEL version=$EXTENSION_VERSION

ARG GITHUB_ORG=dominodatalab
ARG DUSER=ubuntu
ARG DGROUP=ubuntu
ARG DEBIAN_FRONTEND=noninteractive

ENV DOMINO_USER=$DUSER
ENV DOMINO_GROUP=$DGROUP
ENV MLFLOW_VERSION=3.2.0
ARG DATABASE_URL
ENV DATABASE_URL=$DATABASE_URL

# Set Python environment variables
#
# PIP_NO_CACHE_DIR was removed deliberately. The pip download cache now lives
# in a BuildKit cache mount (see --mount=type=cache below), outside the image
# layers, so it adds nothing to final image size. Keeping it means a retry
# after a 502 does not re-download wheels that already succeeded.
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Per-attempt retry budget is deliberately LOW. files.pythonhosted.org
# intermittently returns 502 on PEP 658 *.whl.metadata sidecar requests from
# this build's network path. pip treats a 502 as a transport error rather than
# falling back to the full wheel, so it exhausts its retries and dies.
#
# A high PIP_RETRIES just burns every attempt inside the same bad 30 seconds
# (the original mlflow failure took 248s to give up). Instead each pip
# invocation fails fast and the pipr wrapper below retries the whole
# invocation with escalating sleeps, so attempts land in different minutes.
ENV PIP_RETRIES=3
ENV PIP_TIMEOUT=60

#
# Add Domino requirements
#
RUN apt-get update && \
    # Security updates
    grep security /etc/apt/sources.list > /etc/apt/security.sources.list && \
    apt-get upgrade -y -o Dir::Etc::SourceList=/etc/apt/security.sources.list && \
    apt-get install -y \
        apt-utils \
    # add C compiler for some of the python packages required in the training job
        build-essential \
        gcc \
    # Requirements for Domino executions
        curl \
        procps \
    # Requirements for node installation
        ca-certificates \
    # For troubleshooting
        sqlite3 \
    # Requirement for extension FE deps installation
        git

# ============================================
# pipr: retrying pip wrapper
# ============================================
# Every pip install below goes through pipr, which takes the same arguments and
# retries the whole install with escalating backoff (20s, 40s, 60s, 80s, 100s)
# before giving up. Worst case is about 5 minutes spread across 6 attempts,
# enough to ride out a transient 502 window.
#
# This MUST be defined before the first pip install. The smoke test at the end
# of this layer means a broken or off-PATH wrapper fails here with a clear
# message rather than 12 steps later with "pipr: not found".
RUN test -x /bin/bash || (echo "bash is required for the pipr wrapper" && exit 1)
RUN printf '%s\n' \
  '#!/bin/bash' \
  'set -uo pipefail' \
  'max=6' \
  'attempt=1' \
  'while [ "$attempt" -le "$max" ]; do' \
  '  echo "== pipr attempt $attempt/$max: pip install $* =="' \
  '  if python -m pip install "$@"; then' \
  '    echo "== pipr succeeded on attempt $attempt =="' \
  '    exit 0' \
  '  fi' \
  '  if [ "$attempt" -lt "$max" ]; then' \
  '    wait=$((attempt * 20))' \
  '    echo "== pipr attempt $attempt failed, sleeping ${wait}s before retry ==" >&2' \
  '    sleep "$wait"' \
  '  fi' \
  '  attempt=$((attempt + 1))' \
  'done' \
  'echo "== pipr: pip install failed after $max attempts ==" >&2' \
  'exit 1' \
  > /usr/local/bin/pipr \
 && chmod 755 /usr/local/bin/pipr \
 && pipr --help > /dev/null \
 && echo "pipr wrapper installed and callable"

#
# Add Domino user
#
RUN if ! id 12574 >/dev/null 2>&1; then \
        groupadd -g 12574 ${DOMINO_GROUP}; \
        useradd -u 12574 -g 12574 -m -N -s /bin/bash ${DOMINO_USER}; \
    fi

RUN chown -R ${DOMINO_USER}:${DOMINO_GROUP} "/home/${DOMINO_USER}"

WORKDIR /home/${DOMINO_USER}

RUN test -n "$EXTENSION_VERSION" || (echo "EXTENSION_VERSION build arg is empty" && exit 1)
RUN git clone https://github.com/$GITHUB_ORG/AutoML_Extension.git && cd AutoML_Extension && git checkout $EXTENSION_VERSION

WORKDIR /home/${DOMINO_USER}/AutoML_Extension

#
# Install frontend dependencies
#

# Install nodejs 20
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
 && apt-get install -y nodejs

# Install npm packages and build frontend
# npm retry settings added for the same reason as the pip ones: this build's
# egress path is flaky and npm's defaults give up quickly.
RUN npm config set fetch-retries 6 \
 && npm config set fetch-retry-maxtimeout 120000 \
 && cd automl-ui && npm i && npm run build

WORKDIR /

#
# Install backend/job dependencies
#
# This file deliberately uses plain pip (via pipr), not uv. uv hard-fails when
# a PEP 658 *.whl.metadata request returns 502, which is what this build
# environment's network path does. pip falls back to the full wheel.
#
# setuptools_scm is installed explicitly and up front. seqeval (a dependency of
# autogluon.multimodal) ships only as an sdist whose setup.py declares
# use_scm_version=True with setup_requires=['setuptools_scm']. If setuptools_scm
# is absent, setuptools fetches it from PyPI mid-build via the legacy
# fetch_build_eggs path. When that fetch fails, seqeval's version resolves to
# 0.0.0 and the whole AutoGluon resolution collapses. Having setuptools_scm
# present satisfies setup_requires from the working set, so no fetch happens.
RUN --mount=type=cache,target=/root/.cache/pip \
    pipr --upgrade pip wheel Cython setuptools setuptools_scm

#
# Mlflow for experiment tracking, must install before dominodatalab
#
# This is the step that failed on the .whl.metadata 502. curl is tried first
# because it retries plain file URLs on 502 (--retry-all-errors) and never
# touches the PEP 658 sidecar. Installing from the local wheel still resolves
# mlflow's own dependencies from the index normally. If the pinned URL goes
# stale, the curl leg fails and we fall through to a retrying index install.
RUN --mount=type=cache,target=/root/.cache/pip \
    if curl -fsSL --retry 8 --retry-all-errors --retry-delay 10 \
         -o /tmp/mlflow-3.2.0-py3-none-any.whl \
         https://files.pythonhosted.org/packages/0a/24/f488e66c6f667c7468f439d48446b30adafdb81abfcc01262cf3a50267f5/mlflow-3.2.0-py3-none-any.whl; then \
      echo "== fetched mlflow wheel directly, installing from local file ==" && \
      pipr /tmp/mlflow-3.2.0-py3-none-any.whl && \
      rm -f /tmp/mlflow-3.2.0-py3-none-any.whl; \
    else \
      echo "== direct wheel fetch failed, falling back to index install ==" && \
      pipr mlflow==$MLFLOW_VERSION; \
    fi

# ============================================
# App dependencies
# ============================================
RUN --mount=type=cache,target=/root/.cache/pip \
    pipr aiosqlite==0.22.1 aiofiles

# ============================================
# PyTorch Installation (CPU Version)
# ============================================
RUN --mount=type=cache,target=/root/.cache/pip \
    pipr torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cpu

# For GPU environments, comment out the above and use:
# RUN --mount=type=cache,target=/root/.cache/pip \
#     pipr torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu118

# ============================================
# AutoGluon Core Dependencies
# ============================================
RUN --mount=type=cache,target=/root/.cache/pip \
    pipr \
    "pandas>=2.0.0" \
    "scipy>=1.10.0" \
    "scikit-learn>=1.3.0"

# ============================================
# AutoGluon Tabular Dependencies
# ============================================
# workaround for broken fastai dependency: https://github.com/autogluon/autogluon/issues/5521#issuecomment-3836174413
# should be fixed in autogluon's 2.0 release
RUN --mount=type=cache,target=/root/.cache/pip \
    pipr "fastprogress==1.0.5"

# ============================================
# AutoGluon TimeSeries Dependencies
# ============================================
RUN --mount=type=cache,target=/root/.cache/pip \
    pipr \
    "statsmodels>=0.14.0" \
    "pmdarima>=2.0.3" \
    "tbats>=1.1.3" \
    "prophet>=1.1.4" \
    "gluonts>=0.14.0" \
    "pytorch-lightning>=2.0.0" \
    "holidays>=0.33" \
    "convertdate>=2.4.0" \
    "lunarcalendar>=0.0.9" \
    "tqdm>=4.65.0"

# ============================================
# AutoGluon Multimodal Dependencies
# ============================================
RUN --mount=type=cache,target=/root/.cache/pip \
    pipr \
    "transformers>=4.35.0" \
    "datasets>=2.14.0" \
    "tokenizers>=0.14.0" \
    "accelerate>=0.24.0" \
    "timm>=0.9.0" \
    "Pillow>=10.0.0" \
    "opencv-python-headless>=4.8.0" \
    "albumentations>=1.3.1" \
    "sentencepiece>=0.1.99" \
    "sacremoses>=0.0.53" \
    "nltk>=3.8.1" \
    "pdf2image>=1.16.3" \
    "pytesseract>=0.3.10" \
    "torchmetrics>=1.2.0" \
    "omegaconf>=2.3.0" \
    "jsonschema>=4.19.0" \
    "nptyping>=2.5.0" \
    "defusedxml>=0.7.1"

# ============================================
# seqeval (pre-installed ahead of AutoGluon)
# ============================================
# Built explicitly here, with setuptools_scm already available, so its version
# resolves correctly. Once installed, AutoGluon's seqeval requirement is
# already satisfied and pip will not rebuild it.
RUN --mount=type=cache,target=/root/.cache/pip \
    pipr --no-build-isolation "seqeval>=1.2.2,<1.3.0"

# ============================================
# AutoGluon Installation (All Modules)
# ============================================
# --no-build-isolation reuses the setuptools/wheel/Cython/setuptools_scm
# already installed above instead of fetching fresh copies into an isolated
# build env. This matters for oss2, a transitive dep pulled in via
# autogluon.multimodal -> openmim -> opendatalab -> openxlab -> oss2, and for
# seqeval's setup_requires.
#
# Largest download in the file, so it benefits most from the cache mount: a
# 502 on attempt 3 no longer restarts the whole download.
RUN --mount=type=cache,target=/root/.cache/pip \
    pipr --no-build-isolation \
    "autogluon>=1.1.0" \
    "autogluon.core>=1.1.0" \
    "autogluon.features>=1.1.0" \
    "autogluon.tabular[all]>=1.1.0" \
    "autogluon.timeseries>=1.1.0" \
    "autogluon.multimodal>=1.1.0"

# ============================================
# Visualization Libraries
# ============================================
RUN --mount=type=cache,target=/root/.cache/pip \
    pipr \
    "matplotlib>=3.7.0" \
    "seaborn>=0.12.0" \
    "plotly>=5.15.0" \
    "kaleido>=0.2.1" \
    "bokeh>=3.2.0" \
    "altair>=5.1.0"

# ============================================
# Model Serving (FastAPI)
# ============================================
RUN --mount=type=cache,target=/root/.cache/pip \
    pipr \
    "fastapi>=0.104.0" \
    "uvicorn[standard]>=0.24.0" \
    "python-multipart>=0.0.6" \
    "httpx>=0.25.0" \
    "starlette>=0.27.0" \
    "pydantic>=2.4.0" \
    "pydantic-settings>=2.0.0" \
    "uwsgi"

# ============================================
# Additional Data Science Utilities
# ============================================
RUN --mount=type=cache,target=/root/.cache/pip \
    pipr \
    "pyarrow>=14.0.0" \
    "fastparquet>=2023.10.0" \
    "openpyxl>=3.1.0" \
    "xlrd>=2.0.0" \
    "h5py>=3.10.0" \
    "sqlalchemy>=2.0.0" \
    "s3fs>=2023.10.0" \
    "pyyaml>=6.0" \
    "python-dotenv>=1.0.0" \
    "requests>=2.31.0" \
    "aiohttp>=3.8.0" \
    "tenacity>=8.2.0" \
    "joblib>=1.3.0" \
    "cloudpickle>=3.0.0" \
    "dill>=0.3.7" \
    "typing-extensions>=4.8.0"

# ============================================
# SHAP and Model Interpretability
# ============================================
RUN --mount=type=cache,target=/root/.cache/pip \
    pipr \
    "shap>=0.43.0" \
    "lime>=0.2.0.1" \
    "eli5>=0.13.0"

# ============================================
# ArXiv Research Agent Dependencies
# ============================================
RUN --mount=type=cache,target=/root/.cache/pip \
    pipr \
    "pydantic>=2.5.0" \
    "pydantic-ai[openai]>=0.0.14" \
    "httpx>=0.27.0" \
    "feedparser>=6.0.10" \
    "pdfplumber>=0.10.0"

# allow model endpoint builds to succeed -- seems /mnt is a python slim pre-existing dir
# and model endpoint builds create directories inside it which fails since its owned by another user
RUN chmod 777 /mnt

# Cleanup after apt package installs
RUN rm -rf /var/lib/apt/lists/*

# allow model endpoint builds to succeed -- permission errors with certain directory operations without this
USER ${DOMINO_USER}
