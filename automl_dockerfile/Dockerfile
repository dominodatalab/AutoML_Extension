# Domino Oil & Gas Demo Environment
# AutoGluon-powered environment for Tabular, TimeSeries, and Multimodal ML
# Compatible with Domino Data Lab compute environments

# FROM python:3.10-slim-bullseye

LABEL maintainer="Domino Data Lab"
LABEL description="AutoGluon AutoML environment for Domino Data Lab"
LABEL version="1.0.0"

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Set Python environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Create domino user and group (required for Domino environments)
RUN groupadd -g 12574 domino \
    && useradd -m -s /bin/bash -u 12574 -g domino domino

# Install comprehensive system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    gfortran \
    cmake \
    pkg-config \
    make \
    libgomp1 \
    libopenblas-dev \
    libopenblas-base \
    liblapack-dev \
    liblapack3 \
    libblas-dev \
    libblas3 \
    libgl1-mesa-glx \
    libgl1-mesa-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libxrender1 \
    libfontconfig1 \
    libice6 \
    libjpeg-dev \
    libjpeg62-turbo \
    libpng-dev \
    libpng16-16 \
    libtiff-dev \
    libtiff5 \
    libwebp-dev \
    libopenjp2-7 \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    ffmpeg \
    libhdf5-dev \
    libhdf5-serial-dev \
    zlib1g-dev \
    liblzma-dev \
    libbz2-dev \
    libssl-dev \
    ca-certificates \
    libsqlite3-dev \
    curl \
    wget \
    git \
    unzip \
    zip \
    netcat \
    locales \
    sudo \
    openssh-server \
    && mkdir -p /run/sshd \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Add domino user to sudoers
RUN echo "domino ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Set locale
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8

# Set working directory
WORKDIR /app

# Upgrade pip and install core build tools
RUN pip install --upgrade pip setuptools wheel Cython

# ============================================
# App dependencies
# ============================================
RUN pip install aiosqlite==0.22.1

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
    "numpy>=1.24.0,<2.0.0" \
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
# MLflow for Experiment Tracking TODO OLD MLFLOW VERSION
# ============================================
RUN pip install \
    "mlflow>=2.10.0" \
    "mlflow-skinny>=2.10.0"

# ============================================
# Domino SDK TODO OLD DOMINO SDK VERSION
# ============================================
RUN pip install "dominodatalab>=1.2.0"

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
# Jupyter Environment
# ============================================
RUN pip install \
    "jupyter>=1.0.0" \
    "jupyterlab>=4.0.0" \
    "ipywidgets>=8.0.0" \
    "notebook>=7.0.0" \
    "ipykernel>=6.25.0" \
    "nbformat>=5.9.0" \
    "nbconvert>=7.8.0" \
    "jupyterlab-widgets>=3.0.0"

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

# Create directories for Domino
RUN mkdir -p /mnt/data /mnt/artifacts /mnt/code /mnt/imported/data \
    && chown -R domino:domino /mnt /app

# Copy requirements file if exists (for custom dependencies)
COPY --chown=domino:domino requirements.txt* /app/

# Install any additional requirements if file exists
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Set environment variables for Domino
ENV DOMINO_WORKING_DIR=/mnt/code \
    DOMINO_DATASETS_DIR=/mnt/data \
    DOMINO_ARTIFACTS_DIR=/mnt/artifacts \
    DOMINO_IMPORTED_DATA_DIR=/mnt/imported/data

# Configure Jupyter
RUN mkdir -p /home/domino/.jupyter \
    && echo "c.NotebookApp.ip = '0.0.0.0'" >> /home/domino/.jupyter/jupyter_notebook_config.py \
    && echo "c.NotebookApp.open_browser = False" >> /home/domino/.jupyter/jupyter_notebook_config.py \
    && echo "c.NotebookApp.allow_root = True" >> /home/domino/.jupyter/jupyter_notebook_config.py \
    && echo "c.ServerApp.ip = '0.0.0.0'" >> /home/domino/.jupyter/jupyter_notebook_config.py \
    && echo "c.ServerApp.open_browser = False" >> /home/domino/.jupyter/jupyter_notebook_config.py \
    && echo "c.ServerApp.allow_root = True" >> /home/domino/.jupyter/jupyter_notebook_config.py \
    && chown -R domino:domino /home/domino

# Download NLTK data (commonly needed for NLP)
RUN python -c "import nltk; nltk.download('punkt', quiet=True); nltk.download('stopwords', quiet=True); nltk.download('wordnet', quiet=True)"

RUN python -c "from autogluon.tabular import TabularPredictor; print('TabularPredictor: OK')" && \
	python -c "from autogluon.timeseries import TimeSeriesPredictor; print('TimeSeriesPredictor: OK')"
  	# MultiModalPredictor verified at runtime (requires pkg_resources via legacy autogluon code)

# ============================================
# Domino Agents SDK and MLflow Update
# ============================================
USER root

RUN pip install mlflow==3.2.0
RUN pip install "dominodatalab[agents] @ git+https://github.com/dominodatalab/python-domino.git@release-2.0.0"

# ============================================
# ArXiv Research Agent Dependencies
# ============================================
RUN pip install \
    "pydantic>=2.5.0" \
    "pydantic-ai[openai]>=0.0.14" \
    "httpx>=0.27.0" \
    "feedparser>=6.0.10" \
    "pdfplumber>=0.10.0"

# Pin setuptools to restore pkg_resources (removed in setuptools 72+)
# Must come AFTER all other pip installs to avoid being overwritten
RUN pip install "setuptools<72"

RUN curl -fOL https://github.com/cdr/code-server/releases/download/v3.10.2/code-server_3.10.2_amd64.deb && \
    dpkg -i code-server_3.10.2_amd64.deb

  # Add a VS Code start script
  RUN mkdir -p /opt/domino/workspaces/vscode && \
      chown -R domino:domino /opt/domino/workspaces/vscode && \
      echo '#!/bin/bash' > /opt/domino/workspaces/vscode/start && \
      echo 'SETTINGS_DIR=${DOMINO_WORKING_DIR}/.vscode' >> /opt/domino/workspaces/vscode/start && \
      echo 'FILE=${SETTINGS_DIR}/settings.json' >> /opt/domino/workspaces/vscode/start && \
      echo '# Add a user setting file if it doesnt exist' >> /opt/domino/workspaces/vscode/start && \
      echo 'if [ ! -f "$FILE" ]; then' >> /opt/domino/workspaces/vscode/start && \
      echo '    sudo mkdir -p "${FILE%/*}"' >> /opt/domino/workspaces/vscode/start && \
      echo '    sudo chown -R domino:domino ${SETTINGS_DIR}' >> /opt/domino/workspaces/vscode/start && \
      echo '    cat > "$FILE" << SETTINGS' >> /opt/domino/workspaces/vscode/start && \
      echo '{' >> /opt/domino/workspaces/vscode/start && \
      echo '    "extensions.autoUpdate": false,' >> /opt/domino/workspaces/vscode/start && \
      echo '    "extensions.autoCheckUpdates": false,' >> /opt/domino/workspaces/vscode/start && \
      echo '    "python.pythonPath": "/usr/local/bin/python",' >> /opt/domino/workspaces/vscode/start && \
      echo '    "workbench.startupEditor": "none",' >> /opt/domino/workspaces/vscode/start && \
      echo '    "workbench.colorTheme": "Default Dark+"' >> /opt/domino/workspaces/vscode/start && \
      echo '}' >> /opt/domino/workspaces/vscode/start && \
      echo 'SETTINGS' >> /opt/domino/workspaces/vscode/start && \
      echo 'fi' >> /opt/domino/workspaces/vscode/start && \
      echo 'code-server ${DOMINO_WORKING_DIR} --user-data-dir ${SETTINGS_DIR} --auth none --bind-addr 0.0.0.0:8888 --extensions-dir ${HOME}/.local/share/code-server/extensions --disable-telemetry' >> /opt/domino/workspaces/vscode/start && \
      chmod +x /opt/domino/workspaces/vscode/start

RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g @anthropic-ai/claude-code && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

