# Domino Oil & Gas Demo Environment
# AutoGluon-powered environment for Tabular, TimeSeries, and Multimodal ML
# Compatible with Domino Data Lab compute environments

#
# Required Domino Environment Base Image: python:3.10-slim-bullseye
#

LABEL maintainer="Domino Data Lab"
LABEL description="AutoGluon AutoML environment for Domino Data Lab"
LABEL version="1.0.0"

ARG EXTENSION_VERSION=main
ARG GITHUB_ORG=dominodatalab
ARG DUSER=ubuntu
ARG DGROUP=ubuntu
ARG DEBIAN_FRONTEND=noninteractive

ENV DOMINO_USER=$DUSER
ENV DOMINO_GROUP=$DGROUP
ENV MLFLOW_VERSION=3.2.0

# Set Python environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

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

#
# Add Domino user
#
RUN if ! id 12574 >/dev/null 2>&1; then \
        groupadd -g 12574 ${DOMINO_GROUP}; \
        useradd -u 12574 -g 12574 -m -N -s /bin/bash ${DOMINO_USER}; \
    fi

RUN chown -R ${DOMINO_USER}:${DOMINO_GROUP} "/home/${DOMINO_USER}"

WORKDIR /home/${DOMINO_USER}

# TODO refactor the pip installations to also use this
RUN git clone https://github.com/$GITHUB_ORG/AutoML_Extension.git --depth 1 --branch $EXTENSION_VERSION

WORKDIR /home/${DOMINO_USER}/AutoML_Extension

#
# Install frontend dependencies
#

# Install nodejs 20
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
 && apt-get install -y nodejs

# Install npm packages and build frontend
RUN cd automl-ui && npm i && npm run build

WORKDIR /

#
# Install backend/job dependencies
#

# install uv to improve depependency resolution
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN alias pip="uv pip"
RUN pip install --upgrade pip setuptools wheel Cython

#
# Mlflow for experiment tracking, must install before dominodatalab
#
RUN pip install mlflow==$MLFLOW_VERSION

# ============================================
# App dependencies
# ============================================
RUN pip install aiosqlite==0.22.1 aiofiles

# ============================================
# PyTorch Installation (CPU Version)
# ============================================
RUN pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cpu

# For GPU environments, comment out the above and use:
# RUN pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu118

# ============================================
# AutoGluon Core Dependencies
# ============================================
RUN pip install \
    "pandas>=2.0.0" \
    "scipy>=1.10.0" \
    "scikit-learn>=1.3.0"

# ============================================
# AutoGluon Tabular Dependencies
# ============================================
RUN pip install \
    "lightgbm>=4.0.0" \
    "xgboost>=2.0.0" \
    "catboost>=1.2" \
    "featuretools>=1.27.0" \
    "ray[tune]>=2.6.0" \
    "hyperopt>=0.2.7" \
    "optuna>=3.3.0" \
    "ConfigSpace>=0.7.1" \
    "boto3>=1.28.0" \
    "psutil>=5.9.0" \
    "networkx>=3.1"

# ============================================
# AutoGluon TimeSeries Dependencies
# ============================================
RUN pip install \
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
RUN pip install \
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
# AutoGluon Installation (All Modules)
# ============================================
RUN pip install \
    "autogluon>=1.1.0" \
    "autogluon.core>=1.1.0" \
    "autogluon.features>=1.1.0" \
    "autogluon.tabular>=1.1.0" \
    "autogluon.timeseries>=1.1.0" \
    "autogluon.multimodal>=1.1.0"


# ============================================
# Visualization Libraries
# ============================================
RUN pip install \
    "matplotlib>=3.7.0" \
    "seaborn>=0.12.0" \
    "plotly>=5.15.0" \
    "kaleido>=0.2.1" \
    "bokeh>=3.2.0" \
    "altair>=5.1.0"

# ============================================
# Model Serving (FastAPI)
# ============================================
RUN pip install \
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
RUN pip install \
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
RUN pip install \
    "shap>=0.43.0" \
    "lime>=0.2.0.1" \
    "eli5>=0.13.0"

# ============================================
# ArXiv Research Agent Dependencies
# ============================================
RUN pip install \
    "pydantic>=2.5.0" \
    "pydantic-ai[openai]>=0.0.14" \
    "httpx>=0.27.0" \
    "feedparser>=6.0.10" \
    "pdfplumber>=0.10.0"

# Cleanup after apt package installs
RUN rm -rf /var/lib/apt/lists/*
