import { useCallback, useState, useEffect, useMemo } from 'react'
import { Link } from 'react-router-dom'
import { useDatasets, useUploadFile, useDatasetPreview } from '../hooks/useDatasets'
import { useProfiling } from '../hooks/useProfiling'
import { useStore } from '../store'
import { Dataset, DatasetFile } from '../types/dataset'
import { generateEDANotebook } from '../utils/notebookGenerator'
import { DataSourceSelector } from '../components/eda/DataSourceSelector'
import { ProfiledDataView } from '../components/eda/ProfiledDataView'
import { TimeSeriesConfigPanel } from '../components/eda/TimeSeriesConfigPanel'

interface TransformConfig {
  column: string
  type: 'fillna' | 'scale' | 'encode' | 'drop' | 'log' | 'clip'
}

function EDAAnalysis() {
  const { data: datasetsData, isLoading: loadingDatasets } = useDatasets()
  const uploadMutation = useUploadFile()
  const addNotification = useStore((state) => state.addNotification)
  const {
    profile, loading: profilingLoading, error: profilingError, profileFile,
    tsProfile, tsLoading, tsError, profileTimeSeries,
    startAsyncProfile, getAsyncProfileStatus, setProfileData, setTsProfileData,
  } = useProfiling()

  const [sourceType, setSourceType] = useState<'upload' | 'dataset'>('upload')
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
  const [timeColumn, setTimeColumn] = useState('')
  const [targetColumn, setTargetColumn] = useState('')
  const [idColumn, setIdColumn] = useState('')
  const [rollingWindow, setRollingWindow] = useState('')
  const [asyncRequestId, setAsyncRequestId] = useState<string | null>(null)
  const [asyncDominoJobId, setAsyncDominoJobId] = useState<string | null>(null)
  const [asyncProfileStatus, setAsyncProfileStatus] = useState<'idle' | 'starting' | 'pending' | 'running' | 'completed' | 'failed'>('idle')
  const [asyncProfileError, setAsyncProfileError] = useState<string | null>(null)

  const datasets = datasetsData?.datasets || []

  const offset = (currentPage - 1) * pageSize
  const { data: preview, isLoading: previewLoading, error: previewError } = useDatasetPreview(
    selectedFilePath || '',
    pageSize,
    offset
  )

  const resetAsyncState = useCallback(() => {
    setAsyncRequestId(null)
    setAsyncDominoJobId(null)
    setAsyncProfileStatus('idle')
    setAsyncProfileError(null)
  }, [])

  const startAsyncTabularProfiling = useCallback(async (
    filePath: string,
    size: number,
    strategy: string,
    stratifyCol?: string
  ) => {
    setAsyncProfileStatus('starting')
    setAsyncProfileError(null)
    setAsyncRequestId(null)
    try {
      const response = await startAsyncProfile({
        mode: 'tabular',
        file_path: filePath,
        sample_size: size,
        sampling_strategy: strategy,
        stratify_column: stratifyCol || undefined,
      })
      setAsyncRequestId(response.request_id)
      setAsyncDominoJobId(response.domino_job_id || null)
      setAsyncProfileStatus(response.status === 'pending' ? 'pending' : 'running')
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Failed to start async EDA profiling'
      setAsyncProfileError(message)
      setAsyncProfileStatus('failed')
      addNotification(message, 'error')
    }
  }, [addNotification, startAsyncProfile])

  const startAsyncTimeSeriesProfiling = useCallback(async (
    filePath: string,
    tc: string,
    tgt: string,
    id: string,
    size: number,
    strategy: string,
    rw: string
  ) => {
    setAsyncProfileStatus('starting')
    setAsyncProfileError(null)
    setAsyncRequestId(null)
    try {
      const response = await startAsyncProfile({
        mode: 'timeseries',
        file_path: filePath,
        time_column: tc,
        target_column: tgt,
        id_column: id || undefined,
        sample_size: size,
        sampling_strategy: strategy,
        rolling_window: Number(rw) || undefined,
      })
      setAsyncRequestId(response.request_id)
      setAsyncDominoJobId(response.domino_job_id || null)
      setAsyncProfileStatus(response.status === 'pending' ? 'pending' : 'running')
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Failed to start async time series profiling'
      setAsyncProfileError(message)
      setAsyncProfileStatus('failed')
      addNotification(message, 'error')
    }
  }, [addNotification, startAsyncProfile])

  useEffect(() => {
    if (!selectedFilePath) return
    if (edaExecutionTarget === 'local') {
      resetAsyncState()
      void profileFile(selectedFilePath)
      return
    }
    void startAsyncTabularProfiling(selectedFilePath, sampleSize, samplingStrategy, stratifyColumn || undefined)
  }, [selectedFilePath, edaExecutionTarget, profileFile, resetAsyncState, startAsyncTabularProfiling])

  useEffect(() => {
    if (!asyncRequestId || edaExecutionTarget !== 'domino_job') return

    let mounted = true
    let intervalId: number | null = null

    const pollStatus = async () => {
      try {
        const status = await getAsyncProfileStatus(asyncRequestId)
        if (!mounted) return

        setAsyncDominoJobId(status.domino_job_id || asyncDominoJobId)

        if (status.status === 'completed') {
          if (status.mode === 'timeseries' && status.result) {
            setTsProfileData(status.result as any)
          } else if (status.result) {
            setProfileData(status.result as any)
          }
          setAsyncProfileStatus('completed')
          setAsyncProfileError(null)
          if (intervalId !== null) window.clearInterval(intervalId)
          return
        }

        if (status.status === 'failed') {
          setAsyncProfileStatus('failed')
          setAsyncProfileError(status.error || 'Async profiling failed')
          if (intervalId !== null) window.clearInterval(intervalId)
          return
        }

        setAsyncProfileStatus(status.status === 'pending' ? 'pending' : 'running')
      } catch (error) {
        if (!mounted) return
        const message = error instanceof Error ? error.message : 'Failed to poll async profiling status'
        setAsyncProfileStatus('failed')
        setAsyncProfileError(message)
        if (intervalId !== null) window.clearInterval(intervalId)
      }
    }

    void pollStatus()
    intervalId = window.setInterval(() => {
      void pollStatus()
    }, 4000)

    return () => {
      mounted = false
      if (intervalId !== null) window.clearInterval(intervalId)
    }
  }, [asyncDominoJobId, asyncRequestId, edaExecutionTarget, getAsyncProfileStatus, setProfileData, setTsProfileData])

  const onDrop = useCallback(
    async (acceptedFiles: File[]) => {
      if (acceptedFiles.length === 0) return
      const file = acceptedFiles[0]
      try {
        const result = await uploadMutation.mutateAsync(file)
        setSelectedFilePath(result.file_path)
        setSelectedFileName(result.file_name)
      } catch (error) {
        addNotification(
          error instanceof Error ? error.message : 'Upload failed',
          'error'
        )
      }
    },
    [uploadMutation, addNotification]
  )

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
      <Link to="/dashboard" className="text-domino-accent-purple hover:underline">
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
          sourceType={sourceType}
          setSourceType={setSourceType}
          datasets={datasets}
          loadingDatasets={loadingDatasets}
          selectedDataset={selectedDataset}
          uploadIsPending={uploadMutation.isPending}
          onDrop={onDrop}
          onSelectDataset={handleSelectDataset}
          onSelectFile={handleSelectFile}
          formatSize={formatSize}
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
        <div className="flex items-center border border-[#d9d9d9] rounded-[2px] overflow-hidden">
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
            className={`px-4 py-1.5 text-sm font-medium border-l border-[#d9d9d9] ${
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
          onChange={(e) => setEdaExecutionTarget(e.target.value as 'local' | 'domino_job')}
          className="h-[32px] px-3 text-sm border border-[#d9d9d9] rounded-[2px] bg-white"
        >
          <option value="local">Local (In App)</option>
          <option value="domino_job">Domino Job (External)</option>
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
