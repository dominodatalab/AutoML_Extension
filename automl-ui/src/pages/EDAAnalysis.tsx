import { useState, useEffect, useMemo } from 'react'
import { Link, useSearchParams } from 'react-router-dom'
import { useDatasets, useDatasetPreview } from '../hooks/useDatasets'
import { useEdaAsyncProfiling } from '../hooks/useEdaAsyncProfiling'
import { useProfiling } from '../hooks/useProfiling'
import { useStore } from '../store'
import { Dataset, DatasetFile } from '../types/dataset'
import type { TransformConfig } from '../types/eda'
import { generateEDANotebook } from '../utils/notebookGenerator'
import { getFileName } from '../utils/path'
import { useCapabilities } from '../hooks/useCapabilities'
import { DataSourceSelector } from '../components/eda/DataSourceSelector'
import { useProjectUserSummary } from '../hooks/useProjectUserSummary'
import { ProfiledDataView } from '../components/eda/ProfiledDataView'
import { TimeSeriesConfigPanel } from '../components/eda/TimeSeriesConfigPanel'
import { buildAppPath } from '../utils/appPath'

function EDAAnalysis() {
  const { dominoJobs } = useCapabilities()
  const { project_name: projectName } = useProjectUserSummary()
  const [searchParams] = useSearchParams()
  const { data: datasetsData, isLoading: loadingDatasets, error: datasetsError } = useDatasets()
  const addNotification = useStore((state) => state.addNotification)
  const {
    profile, loading: profilingLoading, error: profilingError, profileFile,
    tsProfile, tsLoading, tsError, profileTimeSeries,
    startAsyncProfile, getAsyncProfileStatus, setProfileData, setTsProfileData,
  } = useProfiling()

  const [selectedDataset, setSelectedDataset] = useState<Dataset | null>(null)
  const [selectedFilePath, setSelectedFilePath] = useState<string | null>(null)
  const [selectedFileName, setSelectedFileName] = useState<string | null>(null)
  const [transforms, setTransforms] = useState<TransformConfig[]>([])
  const [isExporting, setIsExporting] = useState(false)
  const [currentPage, setCurrentPage] = useState(1)
  const [pageSize, setPageSize] = useState(50)
  const [samplingStrategy, setSamplingStrategy] = useState('random')
  const [sampleSize, setSampleSize] = useState(50000)
  const [stratifyColumn, setStratifyColumn] = useState('')
  const [edaExecutionTarget, setEdaExecutionTarget] = useState<'local' | 'domino_job'>('local')
  const [edaMode, setEdaMode] = useState<'tabular' | 'timeseries'>('tabular')

  // Force local if Domino Jobs capability is unavailable
  useEffect(() => {
    if (!dominoJobs && edaExecutionTarget === 'domino_job') {
      setEdaExecutionTarget('local')
    }
  }, [dominoJobs])
  const [timeColumn, setTimeColumn] = useState('')
  const [targetColumn, setTargetColumn] = useState('')
  const [idColumn, setIdColumn] = useState('')
  const [rollingWindow, setRollingWindow] = useState('')
  const [querySelectionApplied, setQuerySelectionApplied] = useState(false)

  const datasets = datasetsData?.datasets || []
  const datasetLoadError = datasetsError instanceof Error ? datasetsError.message : null

  useEffect(() => {
    if (querySelectionApplied) return

    const queryFilePath = searchParams.get('file_path')
    const queryDatasetId = searchParams.get('dataset_id')

    if (!queryFilePath && !queryDatasetId) {
      setQuerySelectionApplied(true)
      return
    }

    if (queryFilePath) {
      setSelectedFilePath(queryFilePath)
      setSelectedFileName(getFileName(queryFilePath))
      setQuerySelectionApplied(true)
      return
    }

    if (queryDatasetId) {
      if (loadingDatasets) return

      const datasetMatch = datasets.find((dataset) => dataset.id === queryDatasetId)
      if (datasetMatch) {
        setSelectedDataset(datasetMatch)
      }
    }

    setQuerySelectionApplied(true)
  }, [datasets, loadingDatasets, querySelectionApplied, searchParams])

  const offset = (currentPage - 1) * pageSize
  const { data: preview, isLoading: previewLoading, error: previewError } = useDatasetPreview(
    selectedFilePath || '',
    pageSize,
    offset,
    searchParams.get('dataset_id') || undefined
  )

  const {
    asyncDominoJobId,
    asyncProfileError,
    asyncProfileStatus,
    resetAsyncState,
    startAsyncTabularProfiling,
    startAsyncTimeSeriesProfiling,
  } = useEdaAsyncProfiling({
    edaExecutionTarget,
    startAsyncProfile,
    getAsyncProfileStatus,
    setProfileData,
    setTsProfileData,
    addNotification,
  })

  useEffect(() => {
    if (!selectedFilePath) return
    if (edaExecutionTarget === 'local') {
      resetAsyncState()
      void profileFile(selectedFilePath)
      return
    }
    void startAsyncTabularProfiling(selectedFilePath, sampleSize, samplingStrategy, stratifyColumn || undefined)
  }, [selectedFilePath, edaExecutionTarget, profileFile, resetAsyncState, startAsyncTabularProfiling])

  const handleSelectDataset = (dataset: Dataset) => {
    setSelectedDataset(selectedDataset?.id === dataset.id ? null : dataset)
  }

  const handleSelectFile = (file: DatasetFile) => {
    resetAsyncState()
    setSelectedFilePath(file.path)
    setSelectedFileName(file.name)
    setTransforms([])
  }

  const handleChangeFile = () => {
    resetAsyncState()
    setSelectedFilePath(null)
    setSelectedFileName(null)
    setTransforms([])
    setProfileData(null)
    setTsProfileData(null)
  }

  const formatSize = (bytes: number): string => {
    if (bytes < 1024) return `${bytes} B`
    if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`
    return `${(bytes / (1024 * 1024)).toFixed(1)} MB`
  }

  const hasDatetimeColumns = useMemo(() => {
    if (!profile?.columns) return false
    return profile.columns.some(
      (c) => c.semantic_type === 'datetime' || c.dtype.includes('datetime')
    )
  }, [profile])

  const handleRunTSAnalysis = (tc: string, tgt: string, id: string, size: number, strategy: string, rw: string) => {
    if (!selectedFilePath) return
    setTimeColumn(tc)
    setTargetColumn(tgt)
    setIdColumn(id)
    setRollingWindow(rw)
    if (edaExecutionTarget === 'domino_job') {
      void startAsyncTimeSeriesProfiling(selectedFilePath, tc, tgt, id, size, strategy, rw)
      return
    }
    void profileTimeSeries({
      mode: 'timeseries',
      file_path: selectedFilePath,
      time_column: tc,
      target_column: tgt,
      id_column: id || undefined,
      sample_size: size,
      sampling_strategy: strategy,
      rolling_window: Number(rw) || undefined,
    })
  }

  const handleReanalyze = (strategy: string, size: number, stratifyCol: string) => {
    setSamplingStrategy(strategy)
    setSampleSize(size)
    setStratifyColumn(stratifyCol)
    if (selectedFilePath) {
      if (edaExecutionTarget === 'domino_job') {
        void startAsyncTabularProfiling(selectedFilePath, size, strategy, stratifyCol || undefined)
      } else {
        void profileFile(selectedFilePath, size, strategy, stratifyCol || undefined)
      }
    }
  }

  const addTransform = (transform: TransformConfig) => {
    setTransforms(prev => [...prev, transform])
  }

  const removeTransform = (index: number) => {
    setTransforms(prev => prev.filter((_, i) => i !== index))
  }

  const exportNotebook = async () => {
    if (!selectedFilePath || !selectedFileName || !profile) return
    setIsExporting(true)
    try {
      const tsConfig = (edaMode === 'timeseries' && tsProfile) ? {
        tsProfile,
        timeColumn,
        targetColumn,
        idColumn,
      } : undefined
      const notebook = generateEDANotebook({ path: selectedFilePath, name: selectedFileName }, profile, transforms, tsConfig)
      const blob = new Blob([JSON.stringify(notebook, null, 2)], { type: 'application/x-ipynb+json' })
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `eda_${selectedFileName.replace(/\.[^.]+$/, '')}.ipynb`
      document.body.appendChild(a)
      a.click()
      document.body.removeChild(a)
      URL.revokeObjectURL(url)
    } catch {
      addNotification('Failed to export notebook', 'error')
    } finally {
      setIsExporting(false)
    }
  }

  // Breadcrumb shared by both views
  const breadcrumb = (
    <nav className="flex items-center gap-2 text-sm">
      <Link to={buildAppPath('/dashboard')} className="text-domino-accent-purple hover:underline">
        AutoML
      </Link>
      <span className="text-domino-text-muted">/</span>
      <span className="text-domino-text-secondary">Data Exploration</span>
    </nav>
  )

  const isAsyncRunning = edaExecutionTarget === 'domino_job' &&
    ['starting', 'pending', 'running'].includes(asyncProfileStatus)
  const effectiveTabularLoading = edaExecutionTarget === 'domino_job'
    ? (edaMode === 'tabular' && isAsyncRunning)
    : profilingLoading
  const effectiveTabularError = edaExecutionTarget === 'domino_job'
    ? (edaMode === 'tabular' ? asyncProfileError : null)
    : profilingError
  const effectiveTsLoading = edaExecutionTarget === 'domino_job'
    ? (edaMode === 'timeseries' && isAsyncRunning)
    : tsLoading
  const effectiveTsError = edaExecutionTarget === 'domino_job'
    ? (edaMode === 'timeseries' ? asyncProfileError : null)
    : tsError

  // If no file selected, show file selection UI
  if (!selectedFilePath) {
    return (
      <div className="space-y-6">
        {breadcrumb}

        <div>
          <h1 className="text-2xl font-normal text-domino-text-primary">Data Exploration</h1>
          <p className="text-sm text-domino-text-secondary mt-1">
            Select a dataset to analyze data quality, distributions, and prepare transformations
          </p>
        </div>

        <DataSourceSelector
          datasets={datasets}
          loadingDatasets={loadingDatasets}
          datasetsError={datasetLoadError}
          selectedDataset={selectedDataset}
          onSelectDataset={handleSelectDataset}
          onSelectFile={handleSelectFile}
          formatSize={formatSize}
          projectName={projectName}
        />
      </div>
    )
  }

  // File is selected - show EDA analysis
  return (
    <div className="space-y-6">
      {breadcrumb}

      {/* Mode Toggle */}
      <div className="flex items-center gap-4">
        <div className="flex items-center border border-domino-border rounded-[2px] overflow-hidden">
          <button
            onClick={() => setEdaMode('tabular')}
            className={`px-4 py-1.5 text-sm font-medium ${
              edaMode === 'tabular'
                ? 'bg-domino-accent-purple text-white'
                : 'bg-white text-domino-text-secondary hover:bg-domino-bg-tertiary'
            }`}
          >
            Tabular
          </button>
          <button
            onClick={() => setEdaMode('timeseries')}
            className={`px-4 py-1.5 text-sm font-medium border-l border-domino-border ${
              edaMode === 'timeseries'
                ? 'bg-domino-accent-purple text-white'
                : 'bg-white text-domino-text-secondary hover:bg-domino-bg-tertiary'
            }`}
          >
            Time Series
          </button>
        </div>
        {edaMode === 'tabular' && hasDatetimeColumns && (
          <button
            onClick={() => setEdaMode('timeseries')}
            className="text-xs text-domino-accent-purple hover:underline"
          >
            Datetime columns detected — try Time Series mode
          </button>
        )}
      </div>

      <div className="flex items-center gap-3">
        <label className="text-sm text-domino-text-secondary">Execution:</label>
        <select
          value={edaExecutionTarget}
          disabled={true}
          onChange={(e) => setEdaExecutionTarget(e.target.value as 'local' | 'domino_job')}
          className="h-[32px] px-3 text-sm border border-domino-border rounded-[2px] bg-white"
        >
          <option value="local">Local (In App)</option>
          {dominoJobs && <option value="domino_job">Domino Job</option>}
        </select>
      </div>

      {edaExecutionTarget === 'domino_job' && asyncProfileStatus !== 'idle' && (
        <div className="border border-domino-border bg-domino-bg-tertiary p-3 text-sm text-domino-text-secondary">
          <p>
            Async profiling status: <span className="font-medium capitalize">{asyncProfileStatus}</span>
            {asyncDominoJobId ? ` | Domino Job ID: ${asyncDominoJobId}` : ''}
          </p>
          {asyncProfileError && (
            <p className="text-domino-accent-red mt-1">{asyncProfileError}</p>
          )}
        </div>
      )}

      {/* Time Series Config Panel */}
      {edaMode === 'timeseries' && profile?.columns && (
        <TimeSeriesConfigPanel
          columns={profile.columns}
          totalRows={profile.summary.total_rows}
          onRunAnalysis={handleRunTSAnalysis}
          loading={effectiveTsLoading}
          timeColumn={timeColumn}
          targetColumn={targetColumn}
          idColumn={idColumn}
          onTimeColumnChange={setTimeColumn}
          onTargetColumnChange={setTargetColumn}
          onIdColumnChange={setIdColumn}
          rollingWindow={rollingWindow}
          onRollingWindowChange={setRollingWindow}
        />
      )}

      <ProfiledDataView
        selectedFilePath={selectedFilePath}
        selectedFileName={selectedFileName!}
        preview={preview}
        previewLoading={previewLoading}
        previewError={previewError}
        profile={profile}
        profilingLoading={effectiveTabularLoading}
        profilingError={effectiveTabularError}
        transforms={transforms}
        isExporting={isExporting}
        currentPage={currentPage}
        pageSize={pageSize}
        samplingStrategy={samplingStrategy}
        sampleSize={sampleSize}
        stratifyColumn={stratifyColumn}
        onChangeFile={handleChangeFile}
        onExportNotebook={exportNotebook}
        onAddTransform={addTransform}
        onRemoveTransform={removeTransform}
        onPageChange={setCurrentPage}
        onPageSizeChange={(size) => { setPageSize(size); setCurrentPage(1); }}
        onReanalyze={handleReanalyze}
        edaMode={edaMode}
        tsProfile={tsProfile}
        tsLoading={effectiveTsLoading}
        tsError={effectiveTsError}
      />
    </div>
  )
}

export default EDAAnalysis
