import type { DataProfile, TimeSeriesProfile } from '../types/profiling'

interface TransformConfig {
  column: string
  type: 'fillna' | 'scale' | 'encode' | 'drop' | 'log' | 'clip'
}

// --- Cell helpers ---

function markdownCell(source: string[]): Record<string, unknown> {
  return { cell_type: 'markdown', metadata: {}, source }
}

function codeCell(source: string[]): Record<string, unknown> {
  return { cell_type: 'code', metadata: {}, source, execution_count: null, outputs: [] }
}

function notebookWrapper(cells: Record<string, unknown>[]): Record<string, unknown> {
  return {
    nbformat: 4,
    nbformat_minor: 5,
    metadata: {
      kernelspec: { display_name: 'Python 3', language: 'python', name: 'python3' },
      language_info: { name: 'python', version: '3.9.0' },
    },
    cells,
  }
}

// --- Time Series EDA cells ---

function generateTimeSeriesEDACells(config: {
  file: { path: string; name: string }
  tsProfile: TimeSeriesProfile
  timeColumn: string
  targetColumn: string
  idColumn: string
}): Record<string, unknown>[] {
  const { tsProfile, timeColumn, targetColumn, idColumn } = config
  const cells: Record<string, unknown>[] = []

  // 1. Divider
  cells.push(markdownCell([
    '---\n',
    '\n',
    '# Time Series Analysis\n',
    '\n',
    `**Time Column:** \`${timeColumn}\`  \n`,
    `**Target Column:** \`${targetColumn}\`  \n`,
    ...(idColumn ? [`**ID Column:** \`${idColumn}\`  \n`] : []),
  ]))

  // 2. Additional TS imports
  cells.push(codeCell([
    '# Time series imports\n',
    'from statsmodels.tsa.stattools import adfuller, acf, pacf\n',
    'from statsmodels.tsa.seasonal import seasonal_decompose\n',
    'import matplotlib.dates as mdates\n',
  ]))

  // 3. Parse time column, ensure target numeric, sort, extract analysis series
  const seriesExtraction = idColumn
    ? [
        `# For multi-series: use the longest series for statistical analysis\n`,
        `counts = df.groupby("${idColumn}").size()\n`,
        `longest_id = counts.idxmax()\n`,
        `analysis_df = df[df["${idColumn}"] == longest_id].copy()\n`,
        `analysis_series = analysis_df.set_index("${timeColumn}")["${targetColumn}"].dropna().sort_index()\n`,
        `print(f"Analyzing series: {longest_id} ({len(analysis_series)} observations)")\n`,
      ]
    : [
        `analysis_series = df.set_index("${timeColumn}")["${targetColumn}"].dropna().sort_index()\n`,
        `print(f"Analysis series: {len(analysis_series)} observations")\n`,
      ]

  cells.push(codeCell([
    `# Prepare time series data\n`,
    `df["${timeColumn}"] = pd.to_datetime(df["${timeColumn}"], errors="coerce")\n`,
    `df["${targetColumn}"] = pd.to_numeric(df["${targetColumn}"], errors="coerce")\n`,
    `df = df.sort_values("${timeColumn}").reset_index(drop=True)\n`,
    `\n`,
    ...seriesExtraction,
  ]))

  // 4. Temporal Overview
  cells.push(markdownCell(['## Temporal Overview\n']))
  cells.push(codeCell([
    `times = df["${timeColumn}"].dropna()\n`,
    `print(f"Date range: {times.min()} to {times.max()}")\n`,
    `print(f"Total observations: {len(df)}")\n`,
    `freq = pd.infer_freq(times.sort_values().unique()[:1000])\n`,
    `print(f"Inferred frequency: {freq}")\n`,
    `\n`,
    `plt.figure(figsize=(14, 4))\n`,
    `plt.plot(df["${timeColumn}"], df["${targetColumn}"], linewidth=0.8, color="#7C3AED")\n`,
    `plt.title("${targetColumn} over Time")\n`,
    `plt.xlabel("Time")\n`,
    `plt.ylabel("${targetColumn}")\n`,
    `plt.tight_layout()\n`,
    `plt.show()\n`,
  ]))

  // 5. Gap Analysis
  cells.push(markdownCell(['## Gap Analysis\n']))
  cells.push(codeCell([
    `sorted_ts = df["${timeColumn}"].dropna().sort_values().reset_index(drop=True)\n`,
    `diffs = sorted_ts.diff().dropna()\n`,
    `median_diff = diffs.median()\n`,
    `threshold = median_diff * 2\n`,
    `gap_mask = diffs > threshold\n`,
    `\n`,
    `if gap_mask.any():\n`,
    `    gap_indices = gap_mask[gap_mask].index\n`,
    `    print(f"Found {len(gap_indices)} gaps (> 2x median interval of {median_diff})")\n`,
    `    gap_data = []\n`,
    `    for idx in gap_indices[:20]:\n`,
    `        gap_start = sorted_ts.iloc[idx - 1]\n`,
    `        gap_end = sorted_ts.iloc[idx]\n`,
    `        gap_data.append({"Start": gap_start, "End": gap_end, "Duration": gap_end - gap_start})\n`,
    `    display(pd.DataFrame(gap_data))\n`,
    `else:\n`,
    `    print("No significant gaps detected.")\n`,
  ]))

  // 6. Target Statistics
  cells.push(markdownCell(['## Target Statistics\n']))
  cells.push(codeCell([
    `target_vals = df["${targetColumn}"].dropna()\n`,
    `stats = {\n`,
    `    "Mean": target_vals.mean(),\n`,
    `    "Std": target_vals.std(),\n`,
    `    "CV": abs(target_vals.std() / target_vals.mean()) if abs(target_vals.mean()) > 1e-10 else 0,\n`,
    `    "Min": target_vals.min(),\n`,
    `    "Max": target_vals.max(),\n`,
    `    "Skewness": target_vals.skew(),\n`,
    `    "Kurtosis": target_vals.kurtosis(),\n`,
    `}\n`,
    `pd.DataFrame.from_dict(stats, orient="index", columns=["Value"]).round(4)\n`,
  ]))

  // 7. Stationarity Test (conditional)
  if (tsProfile.stationarity !== null) {
    cells.push(markdownCell(['## Stationarity Test (Augmented Dickey-Fuller)\n']))
    cells.push(codeCell([
      `result = adfuller(analysis_series.values, autolag="AIC")\n`,
      `statistic, pvalue, _, nobs, critical_values, _ = result\n`,
      `\n`,
      `print(f"ADF Statistic: {statistic:.4f}")\n`,
      `print(f"p-value: {pvalue:.6f}")\n`,
      `print(f"Observations: {nobs}")\n`,
      `print("Critical Values:")\n`,
      `for k, v in critical_values.items():\n`,
      `    print(f"  {k}: {v:.4f}")\n`,
      `\n`,
      `if pvalue < 0.05:\n`,
      `    print("\\nConclusion: Series is stationary (reject H0)")\n`,
      `else:\n`,
      `    print("\\nConclusion: Series is non-stationary (fail to reject H0)")\n`,
    ]))
  }

  // 8. Trend Analysis (conditional)
  if (tsProfile.trend_analysis !== null) {
    cells.push(markdownCell(['## Trend Analysis\n']))
    cells.push(codeCell([
      `y = analysis_series.values.astype(float)\n`,
      `x = np.arange(len(y), dtype=float)\n`,
      `mask = np.isfinite(y)\n`,
      `x_clean, y_clean = x[mask], y[mask]\n`,
      `\n`,
      `coeffs = np.polyfit(x_clean, y_clean, 1)\n`,
      `y_pred = np.polyval(coeffs, x_clean)\n`,
      `ss_res = np.sum((y_clean - y_pred) ** 2)\n`,
      `ss_tot = np.sum((y_clean - np.mean(y_clean)) ** 2)\n`,
      `r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0\n`,
      `\n`,
      `print(f"Slope: {coeffs[0]:.6f}")\n`,
      `print(f"R-squared: {r_squared:.4f}")\n`,
      `direction = "flat" if abs(coeffs[0]) < 1e-10 else ("upward" if coeffs[0] > 0 else "downward")\n`,
      `print(f"Direction: {direction}")\n`,
      `\n`,
      `plt.figure(figsize=(14, 4))\n`,
      `plt.plot(analysis_series.index, analysis_series.values, linewidth=0.8, alpha=0.7, label="Observed")\n`,
      `plt.plot(analysis_series.index[mask], y_pred, color="red", linewidth=2, label=f"Trend (R\\u00b2={r_squared:.3f})")\n`,
      `plt.title("Trend Analysis")\n`,
      `plt.legend()\n`,
      `plt.tight_layout()\n`,
      `plt.show()\n`,
    ]))
  }

  // 9. Rolling Statistics (conditional)
  if (tsProfile.rolling_statistics !== null) {
    const windowSize = tsProfile.rolling_statistics.window_size
    cells.push(markdownCell([`## Rolling Statistics (window=${windowSize})\n`]))
    cells.push(codeCell([
      `window = ${windowSize}\n`,
      `rolling_mean = analysis_series.rolling(window=window, center=True).mean()\n`,
      `rolling_std = analysis_series.rolling(window=window, center=True).std()\n`,
      `\n`,
      `fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 7), sharex=True)\n`,
      `\n`,
      `ax1.plot(analysis_series.index, analysis_series.values, linewidth=0.5, alpha=0.5, label="Observed")\n`,
      `ax1.plot(rolling_mean.index, rolling_mean.values, color="red", linewidth=1.5, label=f"Rolling Mean (w={window})")\n`,
      `ax1.set_title("Rolling Mean")\n`,
      `ax1.legend()\n`,
      `\n`,
      `ax2.plot(rolling_std.index, rolling_std.values, color="orange", linewidth=1.5, label=f"Rolling Std (w={window})")\n`,
      `ax2.set_title("Rolling Standard Deviation")\n`,
      `ax2.legend()\n`,
      `\n`,
      `plt.tight_layout()\n`,
      `plt.show()\n`,
    ]))
  }

  // 10. Seasonal Decomposition (conditional)
  if (tsProfile.seasonality !== null) {
    const { model, period } = tsProfile.seasonality
    cells.push(markdownCell([`## Seasonal Decomposition (model=${model}, period=${period})\n`]))
    cells.push(codeCell([
      `period = ${period}\n`,
      `model_type = "${model}"\n`,
      `\n`,
      `try:\n`,
      `    decomposition = seasonal_decompose(analysis_series, model=model_type, period=period, extrapolate_trend="freq")\n`,
      `except Exception:\n`,
      `    model_type = "additive"\n`,
      `    decomposition = seasonal_decompose(analysis_series, model="additive", period=period, extrapolate_trend="freq")\n`,
      `\n`,
      `fig, axes = plt.subplots(4, 1, figsize=(14, 10), sharex=True)\n`,
      `\n`,
      `axes[0].plot(decomposition.observed, linewidth=0.8)\n`,
      `axes[0].set_title("Observed")\n`,
      `\n`,
      `axes[1].plot(decomposition.trend, linewidth=0.8, color="red")\n`,
      `axes[1].set_title("Trend")\n`,
      `\n`,
      `axes[2].plot(decomposition.seasonal, linewidth=0.8, color="green")\n`,
      `axes[2].set_title("Seasonal")\n`,
      `\n`,
      `axes[3].plot(decomposition.resid, linewidth=0.8, color="orange")\n`,
      `axes[3].set_title("Residual")\n`,
      `\n`,
      `plt.tight_layout()\n`,
      `plt.show()\n`,
      `\n`,
      `# Seasonal strength\n`,
      `var_resid = np.var(decomposition.resid.dropna())\n`,
      `var_seasonal = np.var(decomposition.seasonal.dropna())\n`,
      `strength = var_seasonal / (var_seasonal + var_resid) if (var_seasonal + var_resid) > 0 else 0\n`,
      `print(f"Seasonal strength: {strength:.4f}")\n`,
    ]))
  }

  // 11. ACF/PACF (conditional)
  if (tsProfile.autocorrelation !== null) {
    const nlags = tsProfile.autocorrelation.nlags
    cells.push(markdownCell(['## Autocorrelation (ACF / PACF)\n']))
    cells.push(codeCell([
      `nlags = ${nlags}\n`,
      `acf_values, acf_ci = acf(analysis_series.values, nlags=nlags, alpha=0.05, fft=True)\n`,
      `pacf_values, pacf_ci = pacf(analysis_series.values, nlags=nlags, alpha=0.05)\n`,
      `ci = 1.96 / np.sqrt(len(analysis_series))\n`,
      `\n`,
      `fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))\n`,
      `\n`,
      `ax1.bar(range(len(acf_values)), acf_values, width=0.3, color="#7C3AED")\n`,
      `ax1.axhline(y=ci, linestyle="--", color="gray", alpha=0.7)\n`,
      `ax1.axhline(y=-ci, linestyle="--", color="gray", alpha=0.7)\n`,
      `ax1.axhline(y=0, color="black", linewidth=0.5)\n`,
      `ax1.set_title("ACF")\n`,
      `ax1.set_xlabel("Lag")\n`,
      `\n`,
      `ax2.bar(range(len(pacf_values)), pacf_values, width=0.3, color="#7C3AED")\n`,
      `ax2.axhline(y=ci, linestyle="--", color="gray", alpha=0.7)\n`,
      `ax2.axhline(y=-ci, linestyle="--", color="gray", alpha=0.7)\n`,
      `ax2.axhline(y=0, color="black", linewidth=0.5)\n`,
      `ax2.set_title("PACF")\n`,
      `ax2.set_xlabel("Lag")\n`,
      `\n`,
      `plt.tight_layout()\n`,
      `plt.show()\n`,
    ]))
  }

  // 12. Per-Series Summary (conditional)
  if (idColumn !== '' && tsProfile.per_series_summary) {
    cells.push(markdownCell(['## Per-Series Summary\n']))
    cells.push(codeCell([
      `per_series = df.groupby("${idColumn}").agg(\n`,
      `    count=("${targetColumn}", "size"),\n`,
      `    start=("${timeColumn}", "min"),\n`,
      `    end=("${timeColumn}", "max"),\n`,
      `    missing_rate=("${targetColumn}", lambda x: x.isna().mean()),\n`,
      `    mean=("${targetColumn}", "mean"),\n`,
      `    std=("${targetColumn}", "std"),\n`,
      `).sort_values("count", ascending=False)\n`,
      `\n`,
      `print(f"Total series: {len(per_series)}")\n`,
      `per_series.head(20).round(4)\n`,
    ]))
  }

  // 13. TS Recommendations & Warnings
  const recLines: string[] = ['## Time Series Recommendations & Warnings\n', '\n']
  if (tsProfile.recommendations.length > 0) {
    recLines.push('### Recommendations\n', '\n')
    recLines.push('| Priority | Type | Message |\n')
    recLines.push('|----------|------|---------|\n')
    for (const rec of tsProfile.recommendations) {
      recLines.push(`| ${rec.priority} | ${rec.type} | ${rec.message} |\n`)
    }
    recLines.push('\n')
  }
  if (tsProfile.warnings.length > 0) {
    recLines.push('### Warnings\n', '\n')
    recLines.push('| Severity | Type | Message |\n')
    recLines.push('|----------|------|---------|\n')
    for (const warn of tsProfile.warnings) {
      recLines.push(`| ${warn.severity} | ${warn.type} | ${warn.message} |\n`)
    }
  }
  if (tsProfile.recommendations.length === 0 && tsProfile.warnings.length === 0) {
    recLines.push('No specific recommendations or warnings.\n')
  }
  cells.push(markdownCell(recLines))

  return cells
}

// --- Main notebook generator ---

export function generateEDANotebook(
  selectedFile: { path: string; name: string },
  profile: DataProfile,
  transforms: TransformConfig[],
  tsConfig?: {
    tsProfile: TimeSeriesProfile
    timeColumn: string
    targetColumn: string
    idColumn: string
  }
): Record<string, unknown> {
  const cells: Record<string, unknown>[] = []

  cells.push(markdownCell([
    `# Exploratory Data Analysis\n`,
    `\n`,
    `**File:** ${selectedFile.name}\n`,
    `**Generated:** ${new Date().toISOString()}\n`,
  ]))

  const importLines = [
    'import pandas as pd\n',
    'import numpy as np\n',
    'import matplotlib.pyplot as plt\n',
    'import seaborn as sns\n',
    '\n',
    'plt.style.use("seaborn-v0_8-whitegrid")\n',
    'sns.set_palette("husl")\n',
    '%matplotlib inline\n',
  ]

  if (tsConfig) {
    importLines.push('\n')
    importLines.push('# Time series imports\n')
    importLines.push('from statsmodels.tsa.stattools import adfuller, acf, pacf\n')
    importLines.push('from statsmodels.tsa.seasonal import seasonal_decompose\n')
    importLines.push('import matplotlib.dates as mdates\n')
  }

  cells.push(codeCell(importLines))

  const loadCode = selectedFile.path.endsWith('.parquet')
    ? `df = pd.read_parquet("${selectedFile.path}")`
    : `df = pd.read_csv("${selectedFile.path}")`

  cells.push(codeCell([
    '# Load dataset\n',
    loadCode + '\n',
    'print(f"Dataset shape: {df.shape}")\n',
    'df.head(10)\n',
  ]))

  cells.push(markdownCell(['## Dataset Overview\n']))
  cells.push(codeCell([
    'df.info()\n',
    'print("\\n")\n',
    'df.describe(include="all").T\n',
  ]))

  cells.push(markdownCell(['## Missing Values\n']))
  cells.push(codeCell([
    'missing = df.isnull().sum()\n',
    'missing_pct = (missing / len(df) * 100).round(2)\n',
    'missing_df = pd.DataFrame({"Count": missing, "Percentage": missing_pct})\n',
    'missing_df = missing_df[missing_df["Count"] > 0].sort_values("Count", ascending=False)\n',
    '\n',
    'if len(missing_df) > 0:\n',
    '    display(missing_df)\n',
    '    plt.figure(figsize=(10, 5))\n',
    '    missing_df["Percentage"].plot(kind="bar", color="#7C3AED")\n',
    '    plt.title("Missing Values by Column")\n',
    '    plt.xlabel("Column")\n',
    '    plt.ylabel("Missing %")\n',
    '    plt.xticks(rotation=45, ha="right")\n',
    '    plt.tight_layout()\n',
    '    plt.show()\n',
    'else:\n',
    '    print("No missing values!")\n',
  ]))

  const numericCols = profile.columns.filter(c => ['numeric', 'integer', 'float'].includes(c.dtype)).slice(0, 6).map(c => c.name)

  if (numericCols.length > 0) {
    cells.push(markdownCell(['## Distributions\n']))
    cells.push(codeCell([
      `numeric_cols = ${JSON.stringify(numericCols)}\n`,
      'fig, axes = plt.subplots(2, 3, figsize=(14, 8))\n',
      'axes = axes.flatten()\n',
      'for i, col in enumerate(numeric_cols[:6]):\n',
      '    if i < len(axes):\n',
      '        df[col].hist(bins=30, ax=axes[i], color="#7C3AED", edgecolor="white")\n',
      '        axes[i].set_title(col)\n',
      '        axes[i].set_xlabel("Value")\n',
      '        axes[i].set_ylabel("Frequency")\n',
      'plt.tight_layout()\n',
      'plt.show()\n',
    ]))
  }

  cells.push(markdownCell(['## Correlations\n']))
  cells.push(codeCell([
    'numeric_df = df.select_dtypes(include=[np.number])\n',
    'if len(numeric_df.columns) >= 2:\n',
    '    corr = numeric_df.corr()\n',
    '    plt.figure(figsize=(12, 10))\n',
    '    mask = np.triu(np.ones_like(corr, dtype=bool))\n',
    '    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="RdBu_r", center=0, square=True)\n',
    '    plt.title("Correlation Matrix")\n',
    '    plt.tight_layout()\n',
    '    plt.show()\n',
  ]))

  if (transforms.length > 0) {
    cells.push(markdownCell(['## Data Transformations\n']))

    const transformCode: string[] = ['df_transformed = df.copy()\n', '\n']
    const transformTypeLabels: Record<string, string> = {
      fillna: 'Fill Missing Values',
      scale: 'Standardize/Scale',
      encode: 'One-Hot Encode',
      log: 'Log Transform',
      clip: 'Clip Outliers',
      drop: 'Drop Column',
    }

    transforms.forEach((t, idx) => {
      transformCode.push(`# ${idx + 1}. ${transformTypeLabels[t.type]} on ${t.column}\n`)
      switch (t.type) {
        case 'fillna':
          transformCode.push(`if df_transformed["${t.column}"].dtype in [np.float64, np.int64]:\n`)
          transformCode.push(`    df_transformed["${t.column}"].fillna(df_transformed["${t.column}"].median(), inplace=True)\n`)
          transformCode.push(`else:\n`)
          transformCode.push(`    df_transformed["${t.column}"].fillna(df_transformed["${t.column}"].mode()[0], inplace=True)\n`)
          break
        case 'scale':
          transformCode.push(`from sklearn.preprocessing import StandardScaler\n`)
          transformCode.push(`scaler = StandardScaler()\n`)
          transformCode.push(`df_transformed["${t.column}_scaled"] = scaler.fit_transform(df_transformed[["${t.column}"]])\n`)
          break
        case 'encode':
          transformCode.push(`df_transformed = pd.get_dummies(df_transformed, columns=["${t.column}"], prefix="${t.column}")\n`)
          break
        case 'log':
          transformCode.push(`df_transformed["${t.column}_log"] = np.log1p(df_transformed["${t.column}"].clip(lower=0))\n`)
          break
        case 'clip':
          transformCode.push(`lower = df_transformed["${t.column}"].quantile(0.01)\n`)
          transformCode.push(`upper = df_transformed["${t.column}"].quantile(0.99)\n`)
          transformCode.push(`df_transformed["${t.column}"] = df_transformed["${t.column}"].clip(lower, upper)\n`)
          break
        case 'drop':
          transformCode.push(`df_transformed.drop(columns=["${t.column}"], inplace=True)\n`)
          break
      }
      transformCode.push('\n')
    })

    transformCode.push('print(f"Transformed shape: {df_transformed.shape}")\n')
    transformCode.push('df_transformed.head()\n')

    cells.push(codeCell(transformCode))

    cells.push(codeCell([
      `output_path = "${selectedFile.path.replace(/\.[^.]+$/, '_transformed.csv')}"\n`,
      'df_transformed.to_csv(output_path, index=False)\n',
      'print(f"Saved to: {output_path}")\n',
    ]))
  }

  // Append time series cells if TS config provided
  if (tsConfig) {
    const tsCells = generateTimeSeriesEDACells({
      file: selectedFile,
      tsProfile: tsConfig.tsProfile,
      timeColumn: tsConfig.timeColumn,
      targetColumn: tsConfig.targetColumn,
      idColumn: tsConfig.idColumn,
    })
    cells.push(...tsCells)
  }

  // Summary
  const summaryLines = [
    '## Summary\n',
    `- **Rows:** ${profile.summary.total_rows.toLocaleString()}\n`,
    `- **Columns:** ${profile.summary.total_columns}\n`,
    `- **Memory:** ${profile.summary.memory_usage_mb.toFixed(2)} MB\n`,
    `- **Transformations:** ${transforms.length}\n`,
  ]
  if (tsConfig) {
    summaryLines.push(`- **Time Series Analysis:** Included (target: \`${tsConfig.targetColumn}\`, time: \`${tsConfig.timeColumn}\`)\n`)
  }
  cells.push(markdownCell(summaryLines))

  return notebookWrapper(cells)
}
