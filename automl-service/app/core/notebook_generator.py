"""Generate Jupyter notebooks from job configurations."""

from typing import Any, Dict, List


def make_cell(cell_type: str, source: List[str], execution_count: int = None) -> Dict[str, Any]:
    """Create a Jupyter notebook cell."""
    cell = {
        "cell_type": cell_type,
        "metadata": {},
        "source": source,
    }
    if cell_type == "code":
        cell["execution_count"] = execution_count
        cell["outputs"] = []
    return cell


def generate_binary_classification_notebook(job) -> Dict[str, Any]:
    """Generate a Jupyter notebook for classification training.

    Args:
        job: Job database model with training configuration

    Returns:
        Dict representing the Jupyter notebook JSON structure
    """
    cells = []

    # Title cell
    cells.append(make_cell("markdown", [
        f"# AutoML Classification: {job.name}\n",
        "\n",
        f"**Description:** {job.description or 'Classification model training'}\n",
        "\n",
        "This notebook was generated from the AutoML UI configuration.\n",
        "\n",
        "## Contents\n",
        "1. Setup and Imports\n",
        "2. Load Data\n",
        "3. Configure and Train Model\n",
        "4. Evaluate Model\n",
        "5. MLflow Experiment Tracking\n",
        "6. Register Model to Domino Registry\n"
    ]))

    # Setup cell
    cells.append(make_cell("markdown", [
        "## 1. Setup and Imports"
    ]))

    cells.append(make_cell("code", [
        "import os\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "from datetime import datetime\n",
        "\n",
        "# AutoGluon\n",
        "from autogluon.tabular import TabularPredictor\n",
        "\n",
        "# MLflow for experiment tracking\n",
        "import mlflow\n",
        "from mlflow import MlflowClient\n",
        "\n",
        "# Visualization\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "# Set up display options\n",
        "pd.set_option('display.max_columns', None)\n",
        "pd.set_option('display.max_rows', 100)\n",
        "\n",
        "print(f\"AutoGluon version: {__import__('autogluon').__version__}\")\n",
        "print(f\"MLflow version: {mlflow.__version__}\")"
    ]))

    # Configuration cell
    cells.append(make_cell("markdown", [
        "## 2. Configuration\n",
        "\n",
        "These parameters were configured in the AutoML UI:"
    ]))

    # Build config dict
    preset = job.preset.value if hasattr(job.preset, 'value') else str(job.preset)

    config_lines = [
        "# Training Configuration\n",
        "CONFIG = {\n",
        f"    'job_name': '{job.name}',\n",
        f"    'target_column': '{job.target_column}',\n",
        f"    'preset': '{preset}',\n",
        f"    'time_limit': {job.time_limit or 3600},\n",
    ]

    if job.eval_metric:
        config_lines.append(f"    'eval_metric': '{job.eval_metric}',\n")
    else:
        config_lines.append("    'eval_metric': 'roc_auc',  # Default for binary classification\n")

    # Feature columns may be stored in autogluon_config
    feature_columns = None
    if job.autogluon_config and 'feature_columns' in job.autogluon_config:
        feature_columns = job.autogluon_config['feature_columns']
    if feature_columns:
        config_lines.append(f"    'feature_columns': {feature_columns},\n")

    config_lines.append("}\n")
    config_lines.append("\n")
    config_lines.append(f"DATA_PATH = '{job.file_path}'\n")
    config_lines.append(f"MODEL_SAVE_PATH = './AutogluonModels/{job.name.replace(' ', '_')}'\n")

    cells.append(make_cell("code", config_lines))

    # Advanced config if present
    if job.autogluon_config:
        cells.append(make_cell("markdown", [
            "### Advanced Configuration"
        ]))

        advanced_lines = ["# Advanced AutoGluon settings\n", "ADVANCED_CONFIG = {\n"]

        if 'advanced' in job.autogluon_config:
            adv = job.autogluon_config['advanced']
            if adv.get('num_bag_folds'):
                advanced_lines.append(f"    'num_bag_folds': {adv['num_bag_folds']},\n")
            if adv.get('num_stack_levels'):
                advanced_lines.append(f"    'num_stack_levels': {adv['num_stack_levels']},\n")
            if adv.get('auto_stack'):
                advanced_lines.append(f"    'auto_stack': {adv['auto_stack']},\n")
            if adv.get('excluded_model_types'):
                advanced_lines.append(f"    'excluded_model_types': {adv['excluded_model_types']},\n")
            if adv.get('num_gpus'):
                advanced_lines.append(f"    'num_gpus': {adv['num_gpus']},\n")

        advanced_lines.append("}\n")
        cells.append(make_cell("code", advanced_lines))

    # Load data cell
    cells.append(make_cell("markdown", [
        "## 3. Load Data"
    ]))

    cells.append(make_cell("code", [
        "# Load the dataset\n",
        "df = pd.read_csv(DATA_PATH)\n",
        "\n",
        "print(f\"Dataset shape: {df.shape}\")\n",
        "print(f\"\\nTarget distribution:\")\n",
        "print(df[CONFIG['target_column']].value_counts())\n",
        "\n",
        "df.head()"
    ]))

    cells.append(make_cell("code", [
        "# Check for missing values\n",
        "missing = df.isnull().sum()\n",
        "missing_pct = (missing / len(df) * 100).round(2)\n",
        "missing_df = pd.DataFrame({'Missing': missing, 'Percent': missing_pct})\n",
        "missing_df[missing_df['Missing'] > 0]"
    ]))

    cells.append(make_cell("code", [
        "# Train/test split\n",
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "train_df, test_df = train_test_split(\n",
        "    df, \n",
        "    test_size=0.2, \n",
        "    random_state=42,\n",
        "    stratify=df[CONFIG['target_column']]\n",
        ")\n",
        "\n",
        "print(f\"Training samples: {len(train_df)}\")\n",
        "print(f\"Test samples: {len(test_df)}\")"
    ]))

    # Train model cell
    cells.append(make_cell("markdown", [
        "## 4. Train Model"
    ]))

    train_code = [
        "# Initialize and train AutoGluon TabularPredictor\n",
        "predictor = TabularPredictor(\n",
        "    label=CONFIG['target_column'],\n",
        "    problem_type='binary',\n",
        "    eval_metric=CONFIG.get('eval_metric', 'roc_auc'),\n",
        "    path=MODEL_SAVE_PATH,\n",
        ")\n",
        "\n",
    ]

    # Build fit kwargs
    if job.autogluon_config and 'advanced' in job.autogluon_config:
        train_code.append("# Train with advanced configuration\n")
        train_code.append("predictor.fit(\n")
        train_code.append("    train_data=train_df,\n")
        train_code.append("    presets=CONFIG['preset'],\n")
        train_code.append("    time_limit=CONFIG['time_limit'],\n")

        adv = job.autogluon_config['advanced']
        if adv.get('num_bag_folds'):
            train_code.append(f"    num_bag_folds={adv['num_bag_folds']},\n")
        if adv.get('num_stack_levels'):
            train_code.append(f"    num_stack_levels={adv['num_stack_levels']},\n")
        if adv.get('auto_stack'):
            train_code.append(f"    auto_stack={adv['auto_stack']},\n")
        if adv.get('excluded_model_types'):
            train_code.append(f"    excluded_model_types={adv['excluded_model_types']},\n")
        if adv.get('num_gpus'):
            train_code.append(f"    num_gpus={adv['num_gpus']},\n")

        train_code.append(")\n")
    else:
        train_code.append("# Train with preset configuration\n")
        train_code.append("predictor.fit(\n")
        train_code.append("    train_data=train_df,\n")
        train_code.append("    presets=CONFIG['preset'],\n")
        train_code.append("    time_limit=CONFIG['time_limit'],\n")
        train_code.append(")\n")

    train_code.append("\n")
    train_code.append("print(\"Training complete!\")")

    cells.append(make_cell("code", train_code))

    # Leaderboard cell
    cells.append(make_cell("code", [
        "# View model leaderboard\n",
        "leaderboard = predictor.leaderboard(test_df, silent=True)\n",
        "leaderboard"
    ]))

    # Evaluate model cell
    cells.append(make_cell("markdown", [
        "## 5. Evaluate Model\n",
        "\n",
        "Evaluate the trained model with binary classification metrics."
    ]))

    cells.append(make_cell("code", [
        "# Make predictions\n",
        "y_true = test_df[CONFIG['target_column']]\n",
        "y_pred = predictor.predict(test_df)\n",
        "y_pred_proba = predictor.predict_proba(test_df)\n",
        "\n",
        "# Get the positive class column\n",
        "positive_class = predictor.positive_class\n",
        "y_pred_proba_positive = y_pred_proba[positive_class]\n",
        "\n",
        "print(f\"Positive class: {positive_class}\")"
    ]))

    cells.append(make_cell("code", [
        "# Calculate metrics\n",
        "from sklearn.metrics import (\n",
        "    accuracy_score, precision_score, recall_score, f1_score,\n",
        "    roc_auc_score, average_precision_score, confusion_matrix,\n",
        "    classification_report\n",
        ")\n",
        "\n",
        "metrics = {\n",
        "    'accuracy': accuracy_score(y_true, y_pred),\n",
        "    'precision': precision_score(y_true, y_pred, pos_label=positive_class),\n",
        "    'recall': recall_score(y_true, y_pred, pos_label=positive_class),\n",
        "    'f1': f1_score(y_true, y_pred, pos_label=positive_class),\n",
        "    'roc_auc': roc_auc_score(y_true, y_pred_proba_positive),\n",
        "    'avg_precision': average_precision_score(y_true, y_pred_proba_positive),\n",
        "}\n",
        "\n",
        "print(\"=\" * 50)\n",
        "print(\"CLASSIFICATION METRICS\")\n",
        "print(\"=\" * 50)\n",
        "for metric, value in metrics.items():\n",
        "    print(f\"{metric:20s}: {value:.4f}\")\n",
        "\n",
        "print(\"\\n\" + \"=\" * 50)\n",
        "print(\"CLASSIFICATION REPORT\")\n",
        "print(\"=\" * 50)\n",
        "print(classification_report(y_true, y_pred))"
    ]))

    cells.append(make_cell("code", [
        "# Confusion Matrix\n",
        "cm = confusion_matrix(y_true, y_pred)\n",
        "\n",
        "fig, ax = plt.subplots(figsize=(8, 6))\n",
        "sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)\n",
        "ax.set_xlabel('Predicted')\n",
        "ax.set_ylabel('Actual')\n",
        "ax.set_title('Confusion Matrix')\n",
        "plt.tight_layout()\n",
        "plt.show()"
    ]))

    cells.append(make_cell("code", [
        "# ROC Curve\n",
        "from sklearn.metrics import roc_curve, auc\n",
        "\n",
        "fpr, tpr, thresholds = roc_curve(y_true, y_pred_proba_positive, pos_label=positive_class)\n",
        "roc_auc = auc(fpr, tpr)\n",
        "\n",
        "fig, ax = plt.subplots(figsize=(8, 6))\n",
        "ax.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.4f})')\n",
        "ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random')\n",
        "ax.set_xlim([0.0, 1.0])\n",
        "ax.set_ylim([0.0, 1.05])\n",
        "ax.set_xlabel('False Positive Rate')\n",
        "ax.set_ylabel('True Positive Rate')\n",
        "ax.set_title('Receiver Operating Characteristic (ROC) Curve')\n",
        "ax.legend(loc='lower right')\n",
        "plt.tight_layout()\n",
        "plt.show()"
    ]))

    cells.append(make_cell("code", [
        "# Precision-Recall Curve\n",
        "from sklearn.metrics import precision_recall_curve\n",
        "\n",
        "precision, recall, thresholds = precision_recall_curve(y_true, y_pred_proba_positive, pos_label=positive_class)\n",
        "avg_prec = average_precision_score(y_true, y_pred_proba_positive)\n",
        "\n",
        "fig, ax = plt.subplots(figsize=(8, 6))\n",
        "ax.plot(recall, precision, color='darkorange', lw=2, label=f'PR curve (AP = {avg_prec:.4f})')\n",
        "ax.set_xlim([0.0, 1.0])\n",
        "ax.set_ylim([0.0, 1.05])\n",
        "ax.set_xlabel('Recall')\n",
        "ax.set_ylabel('Precision')\n",
        "ax.set_title('Precision-Recall Curve')\n",
        "ax.legend(loc='lower left')\n",
        "plt.tight_layout()\n",
        "plt.show()"
    ]))

    cells.append(make_cell("code", [
        "# Feature Importance\n",
        "try:\n",
        "    importance = predictor.feature_importance(test_df)\n",
        "    importance_df = importance.reset_index()\n",
        "    importance_df.columns = ['Feature', 'Importance']\n",
        "    importance_df = importance_df.head(20)\n",
        "    \n",
        "    fig, ax = plt.subplots(figsize=(10, 8))\n",
        "    sns.barplot(data=importance_df, x='Importance', y='Feature', ax=ax)\n",
        "    ax.set_title('Top 20 Feature Importance')\n",
        "    plt.tight_layout()\n",
        "    plt.show()\n",
        "except Exception as e:\n",
        "    print(f\"Could not compute feature importance: {e}\")"
    ]))

    # MLflow tracking cell
    cells.append(make_cell("markdown", [
        "## 6. MLflow Experiment Tracking\n",
        "\n",
        "Log the experiment to MLflow for tracking and comparison."
    ]))

    experiment_name = job.experiment_name or job.name.replace(' ', '_')

    cells.append(make_cell("code", [
        "# Configure MLflow\n",
        "# In Domino, MLflow tracking is automatically configured\n",
        "# For local runs, you may need to set MLFLOW_TRACKING_URI\n",
        "\n",
        f"EXPERIMENT_NAME = '{experiment_name}'\n",
        "\n",
        "mlflow.set_experiment(EXPERIMENT_NAME)\n",
        "\n",
        "with mlflow.start_run(run_name=CONFIG['job_name']) as run:\n",
        "    # Log parameters\n",
        "    mlflow.log_param('preset', CONFIG['preset'])\n",
        "    mlflow.log_param('time_limit', CONFIG['time_limit'])\n",
        "    mlflow.log_param('target_column', CONFIG['target_column'])\n",
        "    mlflow.log_param('problem_type', 'binary')\n",
        "    mlflow.log_param('eval_metric', CONFIG.get('eval_metric', 'roc_auc'))\n",
        "    mlflow.log_param('best_model', predictor.get_model_best())\n",
        "    \n",
        "    # Log metrics\n",
        "    for metric_name, metric_value in metrics.items():\n",
        "        mlflow.log_metric(metric_name, metric_value)\n",
        "    \n",
        "    # Log tags\n",
        "    mlflow.set_tag('source', 'automl-notebook')\n",
        "    mlflow.set_tag('model_type', 'tabular')\n",
        "    mlflow.set_tag('framework', 'autogluon')\n",
        "    \n",
        "    # Log leaderboard as artifact\n",
        "    leaderboard.to_csv('leaderboard.csv', index=False)\n",
        "    mlflow.log_artifact('leaderboard.csv')\n",
        "    \n",
        "    print(f\"Logged to MLflow run: {run.info.run_id}\")\n",
        "    print(f\"Experiment: {EXPERIMENT_NAME}\")"
    ]))

    # Model registry cell
    cells.append(make_cell("markdown", [
        "## 7. Register Model to Domino Registry\n",
        "\n",
        "Deploy the model to the Domino Model Registry for production use."
    ]))

    cells.append(make_cell("code", [
        "# Model wrapper for MLflow pyfunc\n",
        "class AutoGluonTabularWrapper(mlflow.pyfunc.PythonModel):\n",
        "    \"\"\"MLflow PythonModel wrapper for AutoGluon TabularPredictor.\"\"\"\n",
        "    \n",
        "    def load_context(self, context):\n",
        "        from autogluon.tabular import TabularPredictor\n",
        "        self.predictor = TabularPredictor.load(context.artifacts['model_path'])\n",
        "    \n",
        "    def predict(self, context, model_input):\n",
        "        predictions = self.predictor.predict(model_input)\n",
        "        try:\n",
        "            probabilities = self.predictor.predict_proba(model_input)\n",
        "            return {\n",
        "                'predictions': predictions.tolist(),\n",
        "                'probabilities': probabilities.to_dict('records')\n",
        "            }\n",
        "        except Exception:\n",
        "            return {'predictions': predictions.tolist()}"
    ]))

    model_name = job.name.replace(' ', '_').replace('-', '_')

    cells.append(make_cell("code", [
        f"# Register model\n",
        f"MODEL_NAME = 'automlapp-{model_name}'\n",
        "\n",
        "# Model description for registry\n",
        "model_description = f'''\n",
        "## AutoML Classification Model\n",
        "\n",
        "**Purpose:** Classification model trained with AutoGluon TabularPredictor.\n",
        "\n",
        "### Model Details\n",
        "- **Framework:** AutoGluon TabularPredictor\n",
        "- **Problem Type:** Classification\n",
        "- **Preset:** {CONFIG['preset']}\n",
        "- **Time Limit:** {CONFIG['time_limit']} seconds\n",
        "\n",
        "### Training Configuration\n",
        "- **Target Column:** {CONFIG['target_column']}\n",
        "- **Eval Metric:** {CONFIG.get('eval_metric', 'auto')}\n",
        "- **Best Model:** {{predictor.get_model_best()}}\n",
        "\n",
        "### Usage\n",
        "```python\n",
        "import mlflow\n",
        "model = mlflow.pyfunc.load_model(f\"models:/{{MODEL_NAME}}/latest\")\n",
        "predictions = model.predict(input_df)\n",
        "```\n",
        "'''\n",
        "\n",
        "conda_env = {\n",
        "    'name': 'autogluon_env',\n",
        "    'channels': ['conda-forge'],\n",
        "    'dependencies': [\n",
        "        'python=3.10',\n",
        "        'pip',\n",
        "        {\n",
        "            'pip': [\n",
        "                'autogluon>=1.1.0',\n",
        "                'mlflow>=2.10.0',\n",
        "                'pandas>=2.0.0',\n",
        "                'uwsgi>=2.0.20',\n",
        "            ]\n",
        "        }\n",
        "    ]\n",
        "}\n",
        "\n",
        "with mlflow.start_run(run_name=f'register_{MODEL_NAME}') as run:\n",
        "    # Log metrics for model card\n",
        "    for metric_name, metric_value in metrics.items():\n",
        "        mlflow.log_metric(metric_name, metric_value)\n",
        "    \n",
        "    # Log parameters for model card\n",
        "    mlflow.log_params({\n",
        "        'model_type': 'TabularPredictor',\n",
        "        'problem_type': 'binary',\n",
        "        'preset': CONFIG['preset'],\n",
        "        'time_limit': CONFIG['time_limit'],\n",
        "        'target_column': CONFIG['target_column'],\n",
        "        'best_model': predictor.get_model_best(),\n",
        "        'num_features': len(train_df.columns) - 1,\n",
        "        'training_samples': len(train_df),\n",
        "        'test_samples': len(test_df),\n",
        "    })\n",
        "    \n",
        "    # Log model with pyfunc wrapper\n",
        "    mlflow.pyfunc.log_model(\n",
        "        artifact_path='model',\n",
        "        python_model=AutoGluonTabularWrapper(),\n",
        "        artifacts={'model_path': MODEL_SAVE_PATH},\n",
        "        conda_env=conda_env,\n",
        "        registered_model_name=MODEL_NAME,\n",
        "    )\n",
        "    \n",
        "    print(f\"Model registered: {MODEL_NAME}\")\n",
        "    print(f\"Run ID: {run.info.run_id}\")"
    ]))

    cells.append(make_cell("code", [
        "# Update model description and tags in registry\n",
        "client = MlflowClient()\n",
        "\n",
        "# Update model description\n",
        "client.update_registered_model(name=MODEL_NAME, description=model_description)\n",
        "\n",
        "# Set registered model tags\n",
        "client.set_registered_model_tag(MODEL_NAME, 'source', 'automl-ui')\n",
        "client.set_registered_model_tag(MODEL_NAME, 'model_type', 'tabular')\n",
        "client.set_registered_model_tag(MODEL_NAME, 'framework', 'autogluon')\n",
        "\n",
        "# Get the latest version and set version-specific tags\n",
        "versions = client.search_model_versions(f\"name='{MODEL_NAME}'\")\n",
        "\n",
        "if versions:\n",
        "    latest = max(versions, key=lambda v: int(v.version))\n",
        "    version = latest.version\n",
        "    \n",
        "    # Set version tags with metrics\n",
        "    for metric_name, metric_value in metrics.items():\n",
        "        client.set_model_version_tag(MODEL_NAME, version, metric_name, f'{metric_value:.4f}')\n",
        "    \n",
        "    client.set_model_version_tag(MODEL_NAME, version, 'training_samples', str(len(train_df)))\n",
        "    client.set_model_version_tag(MODEL_NAME, version, 'best_model', predictor.get_model_best())\n",
        "    \n",
        "    print(f\"\\nRegistered Model: {MODEL_NAME}\")\n",
        "    print(f\"Version: {version}\")\n",
        "    print(f\"Status: {latest.status}\")\n",
        "    print(f\"Source: {latest.source}\")\n",
        "else:\n",
        "    print(\"No versions found\")\n",
        "\n",
        "print(f\"\\nModel description and tags updated for: {MODEL_NAME}\")"
    ]))

    # Summary cell
    cells.append(make_cell("markdown", [
        "## Summary\n",
        "\n",
        "This notebook has:\n",
        "1. Loaded and prepared the training data\n",
        "2. Trained an AutoGluon TabularPredictor for binary classification\n",
        "3. Evaluated the model with comprehensive metrics\n",
        "4. Logged the experiment to MLflow\n",
        "5. Registered the model to the Domino Model Registry\n",
        "\n",
        "### Next Steps\n",
        "- Review the model leaderboard to understand which algorithms performed best\n",
        "- Analyze feature importance to understand key predictors\n",
        "- Use the registered model for inference in production\n"
    ]))

    # Build notebook structure
    notebook = {
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10.0"
            },
            "generated_by": "AutoML UI",
            "job_id": job.id,
            "job_name": job.name,
        },
        "nbformat": 4,
        "nbformat_minor": 5,
        "cells": cells
    }

    return notebook
