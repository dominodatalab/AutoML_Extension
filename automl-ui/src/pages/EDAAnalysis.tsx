import { useCallback, useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useDropzone } from 'react-dropzone'
import {
  CloudArrowUpIcon,
  CircleStackIcon,
  DocumentIcon,
  CheckCircleIcon,
  ArrowDownTrayIcon,
  ArrowPathIcon,
} from '@heroicons/react/24/outline'
import clsx from 'clsx'
import { useDatasets, useUploadFile, useDatasetPreview } from '../hooks/useDatasets'
import { useProfiling } from '../hooks/useProfiling'
import { useStore } from '../store'
import Spinner from '../components/common/Spinner'
import Dropdown from '../components/common/Dropdown'
import { Dataset, DatasetFile } from '../types/dataset'
import { ColumnExplorer } from '../components/eda/ColumnExplorer'
import { CorrelationMatrix } from '../components/eda/CorrelationMatrix'
import { MissingValuesChart } from '../components/eda/MissingValuesChart'
import { DataQualityPanel } from '../components/eda/DataQualityPanel'
import type { DataProfile } from '../types/profiling'

type EDATab = 'data' | 'columns' | 'correlations' | 'quality' | 'transforms'

interface TransformConfig {
  column: string
  type: 'fillna' | 'scale' | 'encode' | 'drop' | 'log' | 'clip'
}

function EDAAnalysis() {
  const { data: datasetsData, isLoading: loadingDatasets } = useDatasets()
  const uploadMutation = useUploadFile()
  const addNotification = useStore((state) => state.addNotification)
  const { profile, loading: profilingLoading, error: profilingError, profileFile } = useProfiling()

  const [sourceType, setSourceType] = useState<'upload' | 'dataset'>('dataset')
  const [selectedDataset, setSelectedDataset] = useState<Dataset | null>(null)
  const [selectedFilePath, setSelectedFilePath] = useState<string | null>(null)
  const [selectedFileName, setSelectedFileName] = useState<string | null>(null)
  const [activeTab, setActiveTab] = useState<EDATab>('data')
  const [transforms, setTransforms] = useState<TransformConfig[]>([])
  const [isExporting, setIsExporting] = useState(false)
  const [currentPage, setCurrentPage] = useState(1)
  const [pageSize, setPageSize] = useState(50)

  const datasets = datasetsData?.datasets || []

  const offset = (currentPage - 1) * pageSize
  const { data: preview, isLoading: previewLoading, error: previewError } = useDatasetPreview(
    selectedFilePath || '',
    pageSize,
    offset
  )

  useEffect(() => {
    if (selectedFilePath) {
      profileFile(selectedFilePath)
    }
  }, [selectedFilePath, profileFile])

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

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'text/csv': ['.csv'],
      'application/vnd.apache.parquet': ['.parquet', '.pq'],
    },
    maxFiles: 1,
  })

  const handleSelectDataset = (dataset: Dataset) => {
    setSelectedDataset(selectedDataset?.id === dataset.id ? null : dataset)
  }

  const handleSelectFile = (file: DatasetFile) => {
    setSelectedFilePath(file.path)
    setSelectedFileName(file.name)
    setTransforms([])
  }

  const handleChangeFile = () => {
    setSelectedFilePath(null)
    setSelectedFileName(null)
    setTransforms([])
    setActiveTab('data')
  }

  const formatSize = (bytes: number): string => {
    if (bytes < 1024) return `${bytes} B`
    if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`
    return `${(bytes / (1024 * 1024)).toFixed(1)} MB`
  }

  const formatNumber = (num: number | null | undefined): string => {
    if (num === null || num === undefined) return '-'
    if (typeof num !== 'number' || isNaN(num)) return '-'
    const abs = Math.abs(num)
    if (abs >= 1e9) return (num / 1e9).toFixed(2) + 'B'
    if (abs >= 1e6) return (num / 1e6).toFixed(2) + 'M'
    if (abs >= 1e3) return num.toLocaleString(undefined, { maximumFractionDigits: 2 })
    if (abs < 0.001 && abs > 0) return num.toExponential(2)
    if (Number.isInteger(num)) return num.toLocaleString()
    return num.toFixed(4)
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
      const notebook = generateEDANotebook({ path: selectedFilePath, name: selectedFileName }, profile, transforms)
      const blob = new Blob([JSON.stringify(notebook, null, 2)], { type: 'application/x-ipynb+json' })
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `eda_${selectedFileName.replace(/\.[^.]+$/, '')}.ipynb`
      document.body.appendChild(a)
      a.click()
      document.body.removeChild(a)
      URL.revokeObjectURL(url)
      // Notebook exported - no notification needed
    } catch {
      addNotification('Failed to export notebook', 'error')
    } finally {
      setIsExporting(false)
    }
  }

  const tabs = [
    { id: 'data' as const, label: 'Data Preview' },
    { id: 'columns' as const, label: 'Column Analysis' },
    { id: 'correlations' as const, label: 'Correlations' },
    { id: 'quality' as const, label: 'Data Quality' },
    { id: 'transforms' as const, label: 'Transformations' },
  ]

  // If no file selected, show file selection UI
  if (!selectedFilePath) {
    return (
      <div className="space-y-6">
        {/* Breadcrumb */}
        <nav className="flex items-center gap-2 text-sm">
          <Link to="/dashboard" className="text-domino-accent-purple hover:underline">
            AutoML
          </Link>
          <span className="text-domino-text-muted">/</span>
          <span className="text-domino-text-secondary">Data Exploration</span>
        </nav>

        {/* Page Header */}
        <div>
          <h1 className="text-2xl font-normal text-domino-text-primary">Data Exploration</h1>
          <p className="text-sm text-domino-text-secondary mt-1">
            Select a dataset to analyze data quality, distributions, and prepare transformations
          </p>
        </div>

        {/* Data Source Selection */}
        <div className="space-y-4">
          <div className="flex gap-4">
            <button
              onClick={() => setSourceType('upload')}
              className={clsx(
                'flex-1 p-4 border transition-colors text-left',
                sourceType === 'upload'
                  ? 'border-domino-accent-purple bg-domino-accent-purple/5'
                  : 'border-domino-border bg-white hover:border-domino-text-muted'
              )}
            >
              <CloudArrowUpIcon className="h-6 w-6 text-domino-accent-purple mb-2" />
              <p className="font-medium text-domino-text-primary">Upload File</p>
              <p className="text-sm text-domino-text-secondary">Upload a CSV or Parquet file</p>
            </button>

            <button
              onClick={() => setSourceType('dataset')}
              className={clsx(
                'flex-1 p-4 border transition-colors text-left',
                sourceType === 'dataset'
                  ? 'border-domino-accent-purple bg-domino-accent-purple/5'
                  : 'border-domino-border bg-white hover:border-domino-text-muted'
              )}
            >
              <CircleStackIcon className="h-6 w-6 text-domino-accent-purple mb-2" />
              <p className="font-medium text-domino-text-primary">Domino Dataset</p>
              <p className="text-sm text-domino-text-secondary">Select from mounted datasets</p>
            </button>
          </div>

          {/* Upload Area */}
          {sourceType === 'upload' && (
            <div className="bg-white border border-domino-border">
              <div
                {...getRootProps()}
                className={clsx(
                  'border border-dashed p-8 text-center cursor-pointer transition-colors bg-domino-bg-tertiary',
                  isDragActive
                    ? 'border-domino-accent-purple'
                    : 'border-domino-border hover:border-domino-text-muted'
                )}
              >
                <input {...getInputProps()} />
                {uploadMutation.isPending ? (
                  <div className="flex flex-col items-center">
                    <Spinner className="mb-4" />
                    <p className="text-domino-text-secondary">Uploading...</p>
                  </div>
                ) : (
                  <div className="flex flex-col items-center">
                    <CloudArrowUpIcon className="h-12 w-12 text-domino-accent-purple mb-4" />
                    <p className="text-domino-text-primary">
                      Drag or click to upload <span className="text-domino-accent-purple cursor-pointer">files</span>
                    </p>
                    <p className="text-sm text-domino-text-muted mt-4">
                      * Supports CSV and Parquet files
                    </p>
                    <p className="text-sm text-domino-text-muted">
                      * File size may not exceed 550 MB
                    </p>
                  </div>
                )}
              </div>
            </div>
          )}

          {/* Dataset Selection */}
          {sourceType === 'dataset' && (
            <div className="space-y-3">
              {loadingDatasets ? (
                <div className="flex justify-center py-8">
                  <Spinner />
                </div>
              ) : datasets.length === 0 ? (
                <div className="text-center py-8">
                  <CircleStackIcon className="h-12 w-12 text-domino-text-muted mx-auto mb-4" />
                  <p className="text-domino-text-muted">No datasets mounted</p>
                  <p className="text-sm text-domino-text-muted mt-2">
                    Mount a dataset to this app to get started
                  </p>
                </div>
              ) : (
                datasets.map((dataset: Dataset) => (
                  <div key={dataset.id} className="space-y-2">
                    <button
                      onClick={() => handleSelectDataset(dataset)}
                      className={clsx(
                        'w-full p-4 rounded-lg border-2 transition-colors text-left flex items-center gap-4',
                        selectedDataset?.id === dataset.id
                          ? 'border-domino-accent-purple bg-domino-accent-purple/10'
                          : 'border-domino-border hover:border-domino-text-muted'
                      )}
                    >
                      <CircleStackIcon className="h-8 w-8 text-domino-accent-purple flex-shrink-0" />
                      <div className="flex-1 min-w-0">
                        <p className="font-medium text-domino-text-primary truncate">{dataset.name}</p>
                        <p className="text-sm text-domino-text-secondary">
                          {dataset.file_count} files, {formatSize(dataset.size_bytes)}
                        </p>
                      </div>
                      {selectedDataset?.id === dataset.id && (
                        <CheckCircleIcon className="h-6 w-6 text-domino-accent-green flex-shrink-0" />
                      )}
                    </button>

                    {selectedDataset?.id === dataset.id && dataset.files.length > 0 && (
                      <div className="ml-8 space-y-1">
                        {dataset.files
                          .filter(f => f.name.endsWith('.csv') || f.name.endsWith('.parquet') || f.name.endsWith('.pq'))
                          .map((file) => (
                            <button
                              key={file.path}
                              onClick={() => handleSelectFile(file)}
                              className="w-full p-3 rounded-lg border border-domino-border hover:border-domino-text-muted transition-colors text-left flex items-center gap-3"
                            >
                              <DocumentIcon className="h-5 w-5 text-domino-text-muted flex-shrink-0" />
                              <div className="flex-1 min-w-0">
                                <p className="text-sm text-domino-text-primary truncate">{file.name}</p>
                                <p className="text-xs text-domino-text-muted">{formatSize(file.size)}</p>
                              </div>
                            </button>
                          ))}
                      </div>
                    )}
                  </div>
                ))
              )}
            </div>
          )}
        </div>
      </div>
    )
  }

  // File is selected - show EDA analysis
  return (
    <div className="space-y-6">
      {/* Breadcrumb */}
      <nav className="flex items-center gap-2 text-sm">
        <Link to="/dashboard" className="text-domino-accent-purple hover:underline">
          AutoML
        </Link>
        <span className="text-domino-text-muted">/</span>
        <span className="text-domino-text-secondary">Data Exploration</span>
      </nav>

      {/* Page Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-normal text-domino-text-primary">Data Exploration</h1>
          <p className="text-sm text-domino-text-secondary mt-1">
            Analyze data quality, distributions, and prepare transformations
          </p>
        </div>
        {profile && (
          <button
            onClick={exportNotebook}
            disabled={isExporting}
            className="h-[32px] px-[15px] bg-domino-accent-purple text-white text-sm font-normal rounded-[2px] hover:bg-domino-accent-purple-hover transition-all duration-200 inline-flex items-center gap-2 disabled:opacity-50"
          >
            {isExporting ? (
              <ArrowPathIcon className="h-4 w-4 animate-spin" />
            ) : (
              <ArrowDownTrayIcon className="h-4 w-4" />
            )}
            Export Notebook
          </button>
        )}
      </div>

      {/* Selected File Info */}
      <div className="bg-domino-accent-purple/5 border border-domino-accent-purple p-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <DocumentIcon className="h-6 w-6 text-domino-accent-purple" />
          <div>
            <p className="font-medium text-domino-text-primary">{selectedFileName}</p>
            {preview && (
              <p className="text-sm text-domino-text-secondary">
                {preview.columns?.length || 0} columns, {preview.total_rows?.toLocaleString() || 0} rows
              </p>
            )}
          </div>
        </div>
        <button
          onClick={handleChangeFile}
          className="text-sm text-domino-accent-purple hover:underline"
        >
          Change File
        </button>
      </div>

      {/* EDA Tabs */}
      <div className="border-b border-domino-border">
        <nav className="flex">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={clsx(
                'px-6 py-3 text-sm border-b-2 -mb-px transition-colors',
                activeTab === tab.id
                  ? 'border-domino-accent-purple text-domino-accent-purple font-medium'
                  : 'border-transparent text-domino-text-secondary hover:text-domino-text-primary'
              )}
            >
              {tab.label}
            </button>
          ))}
        </nav>
      </div>

      {/* Tab Content */}
      <div className="bg-white border border-domino-border p-6">
        {activeTab === 'data' && (
          <DataPreviewContent
            preview={preview}
            previewLoading={previewLoading}
            previewError={previewError}
            formatNumber={formatNumber}
            currentPage={currentPage}
            pageSize={pageSize}
            onPageChange={setCurrentPage}
            onPageSizeChange={(size) => { setPageSize(size); setCurrentPage(1); }}
          />
        )}

        {activeTab === 'columns' && (
          profilingLoading ? (
            <div className="flex items-center justify-center py-20">
              <Spinner />
            </div>
          ) : profilingError ? (
            <div className="text-center py-20 text-domino-accent-red">{profilingError}</div>
          ) : profile ? (
            <ColumnExplorer columns={profile.columns} filePath={selectedFilePath} />
          ) : null
        )}

        {activeTab === 'correlations' && (
          profilingLoading ? (
            <div className="flex items-center justify-center py-20">
              <Spinner />
            </div>
          ) : profile?.correlations ? (
            <CorrelationMatrix correlations={profile.correlations} columns={profile.columns} />
          ) : (
            <div className="text-center py-20 text-domino-text-muted">
              No correlation data available
            </div>
          )
        )}

        {activeTab === 'quality' && (
          profilingLoading ? (
            <div className="flex items-center justify-center py-20">
              <Spinner />
            </div>
          ) : profile ? (
            <div className="space-y-6">
              <MissingValuesChart columns={profile.columns} />
              <DataQualityPanel
                warnings={profile.warnings}
                recommendations={profile.recommendations}
                columns={profile.columns}
              />
            </div>
          ) : null
        )}

        {activeTab === 'transforms' && profile && (
          <TransformsContent
            profile={profile}
            transforms={transforms}
            onAddTransform={addTransform}
            onRemoveTransform={removeTransform}
          />
        )}
      </div>
    </div>
  )
}

function DataPreviewContent({
  preview,
  previewLoading,
  previewError,
  formatNumber,
  currentPage,
  pageSize,
  onPageChange,
  onPageSizeChange,
}: {
  preview: { columns?: string[]; rows?: Record<string, unknown>[]; total_rows?: number } | undefined
  previewLoading: boolean
  previewError: unknown
  formatNumber: (num: number | null | undefined) => string
  currentPage: number
  pageSize: number
  onPageChange: (page: number) => void
  onPageSizeChange: (size: number) => void
}) {
  const totalRows = preview?.total_rows || 0
  const totalPages = Math.ceil(totalRows / pageSize)
  const startRow = (currentPage - 1) * pageSize + 1
  const endRow = Math.min(currentPage * pageSize, totalRows)

  if (previewError) {
    return (
      <div className="text-center py-20 text-domino-accent-red">
        <p className="font-medium">Failed to load data</p>
        <p className="text-sm mt-1">{previewError instanceof Error ? previewError.message : 'Unknown error'}</p>
      </div>
    )
  }

  if (!preview && !previewLoading) return null

  return (
    <div>
      {/* Page size selector */}
      <div className="flex items-center justify-between mb-3">
        <div className="flex items-center gap-2 text-sm text-domino-text-secondary">
          <span>Rows per page:</span>
          <Dropdown
            value={String(pageSize)}
            onChange={(val) => onPageSizeChange(Number(val))}
            className="w-[80px]"
            options={[
              { value: '25', label: '25' },
              { value: '50', label: '50' },
              { value: '100', label: '100' },
              { value: '250', label: '250' },
              { value: '500', label: '500' },
            ]}
          />
        </div>
        <div className="text-sm text-domino-text-muted">
          {totalRows > 0 ? `${startRow.toLocaleString()}–${endRow.toLocaleString()} of ${totalRows.toLocaleString()} rows` : '0 rows'}
        </div>
      </div>

      {/* Data table */}
      <div className="overflow-auto border border-domino-border relative" style={{ maxHeight: '500px' }}>
        {previewLoading && (
          <div className="absolute inset-0 bg-white/70 flex items-center justify-center z-10">
            <Spinner />
          </div>
        )}
        <table className="w-full text-sm">
          <thead className="sticky top-0 bg-domino-bg-tertiary">
            <tr>
              <th className="px-3 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase border-b border-domino-border w-12">
                #
              </th>
              {preview?.columns?.map((col: string) => (
                <th
                  key={col}
                  className="px-3 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase border-b border-domino-border whitespace-nowrap"
                >
                  {col}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {preview?.rows?.map((row: Record<string, unknown>, idx: number) => (
              <tr key={idx} className="hover:bg-domino-bg-tertiary border-b border-domino-border">
                <td className="px-3 py-2 text-domino-text-muted">{startRow + idx}</td>
                {preview?.columns?.map((col: string) => {
                  const value = row[col]
                  const displayValue = value === null || value === undefined
                    ? '-'
                    : typeof value === 'number'
                    ? formatNumber(value)
                    : String(value)
                  return (
                    <td
                      key={col}
                      className="px-3 py-2 text-domino-text-primary whitespace-nowrap max-w-[200px] truncate"
                      title={String(value ?? '')}
                    >
                      {value === null || value === undefined ? (
                        <span className="text-domino-text-muted italic">null</span>
                      ) : (
                        displayValue
                      )}
                    </td>
                  )
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Pagination controls */}
      {totalPages > 1 && (
        <div className="flex items-center justify-end gap-2 mt-4">
          <button
            onClick={() => onPageChange(1)}
            disabled={currentPage === 1}
            className="h-[32px] px-3 text-sm border border-[#d9d9d9] rounded-[2px] text-domino-text-secondary disabled:opacity-50 disabled:cursor-not-allowed hover:bg-domino-bg-tertiary"
          >
            First
          </button>
          <button
            onClick={() => onPageChange(currentPage - 1)}
            disabled={currentPage === 1}
            className="h-[32px] w-[32px] flex items-center justify-center border border-[#d9d9d9] rounded-[2px] text-domino-text-secondary disabled:opacity-50 disabled:cursor-not-allowed hover:bg-domino-bg-tertiary"
          >
            &lt;
          </button>
          <span className="text-sm text-domino-text-secondary px-2">
            Page {currentPage} of {totalPages}
          </span>
          <button
            onClick={() => onPageChange(currentPage + 1)}
            disabled={currentPage === totalPages}
            className="h-[32px] w-[32px] flex items-center justify-center border border-[#d9d9d9] rounded-[2px] text-domino-text-secondary disabled:opacity-50 disabled:cursor-not-allowed hover:bg-domino-bg-tertiary"
          >
            &gt;
          </button>
          <button
            onClick={() => onPageChange(totalPages)}
            disabled={currentPage === totalPages}
            className="h-[32px] px-3 text-sm border border-[#d9d9d9] rounded-[2px] text-domino-text-secondary disabled:opacity-50 disabled:cursor-not-allowed hover:bg-domino-bg-tertiary"
          >
            Last
          </button>
        </div>
      )}
    </div>
  )
}

function TransformsContent({
  profile,
  transforms,
  onAddTransform,
  onRemoveTransform,
}: {
  profile: DataProfile
  transforms: TransformConfig[]
  onAddTransform: (transform: TransformConfig) => void
  onRemoveTransform: (index: number) => void
}) {
  const [selectedColumn, setSelectedColumn] = useState<string>('')
  const [selectedType, setSelectedType] = useState<TransformConfig['type']>('fillna')

  const transformTypes: { value: TransformConfig['type']; label: string }[] = [
    { value: 'fillna', label: 'Fill Missing Values' },
    { value: 'scale', label: 'Standardize/Scale' },
    { value: 'encode', label: 'One-Hot Encode' },
    { value: 'log', label: 'Log Transform' },
    { value: 'clip', label: 'Clip Outliers' },
    { value: 'drop', label: 'Drop Column' },
  ]

  const addSelectedTransform = () => {
    if (!selectedColumn) return
    onAddTransform({ column: selectedColumn, type: selectedType })
    setSelectedColumn('')
  }

  const columnsWithIssues = profile.columns.filter(
    col => col.missing_percentage > 5 || (col.issues && col.issues.length > 0)
  )

  return (
    <div className="space-y-6">
      {columnsWithIssues.length > 0 && (
        <div>
          <h3 className="text-sm font-medium text-domino-text-primary mb-3">Recommended Transformations</h3>
          <div className="space-y-2">
            {columnsWithIssues.slice(0, 5).map((col) => (
              <div key={col.name} className="flex items-center justify-between p-3 bg-domino-bg-tertiary border border-domino-border">
                <div>
                  <span className="text-sm font-medium text-domino-text-primary">{col.name}</span>
                  <span className="text-xs text-domino-text-muted ml-2">
                    {col.missing_percentage > 5 && `${col.missing_percentage.toFixed(1)}% missing`}
                    {col.issues?.length ? ` - ${col.issues[0]}` : ''}
                  </span>
                </div>
                <button
                  onClick={() => onAddTransform({
                    column: col.name,
                    type: col.missing_percentage > 5 ? 'fillna' : 'scale'
                  })}
                  className="text-sm text-domino-accent-purple hover:underline"
                >
                  Add
                </button>
              </div>
            ))}
          </div>
        </div>
      )}

      <div>
        <h3 className="text-sm font-medium text-domino-text-primary mb-3">Add Transformation</h3>
        <div className="flex gap-4 items-end">
          <div className="flex-1">
            <label className="block text-xs text-domino-text-muted mb-1">Column</label>
            <Dropdown
              value={selectedColumn}
              onChange={setSelectedColumn}
              placeholder="Select column..."
              options={profile.columns.map((col) => ({ value: col.name, label: col.name }))}
            />
          </div>
          <div className="flex-1">
            <label className="block text-xs text-domino-text-muted mb-1">Transformation</label>
            <Dropdown
              value={selectedType}
              onChange={(val) => setSelectedType(val as TransformConfig['type'])}
              options={transformTypes}
            />
          </div>
          <button
            onClick={addSelectedTransform}
            disabled={!selectedColumn}
            className="h-[32px] px-4 text-sm bg-domino-accent-purple text-white rounded-[2px] hover:bg-domino-accent-purple-hover disabled:opacity-50"
          >
            Add
          </button>
        </div>
      </div>

      <div>
        <h3 className="text-sm font-medium text-domino-text-primary mb-3">
          Selected Transformations ({transforms.length})
        </h3>
        {transforms.length === 0 ? (
          <div className="p-6 text-center text-domino-text-muted text-sm bg-domino-bg-tertiary border border-domino-border">
            No transformations selected. Add transformations to include in the exported notebook.
          </div>
        ) : (
          <div className="border border-domino-border divide-y divide-domino-border">
            {transforms.map((t, idx) => (
              <div key={idx} className="px-4 py-3 flex items-center justify-between bg-white">
                <div className="flex items-center gap-4">
                  <span className="text-xs text-domino-text-muted w-6">{idx + 1}.</span>
                  <span className="text-sm font-medium text-domino-text-primary">{t.column}</span>
                  <span className="text-xs px-2 py-1 bg-domino-bg-tertiary text-domino-text-secondary">
                    {transformTypes.find(tt => tt.value === t.type)?.label}
                  </span>
                </div>
                <button
                  onClick={() => onRemoveTransform(idx)}
                  className="text-xs text-domino-accent-red hover:underline"
                >
                  Remove
                </button>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}

function generateEDANotebook(
  selectedFile: { path: string; name: string },
  profile: DataProfile,
  transforms: TransformConfig[]
): Record<string, unknown> {
  const cells = []

  cells.push({
    cell_type: 'markdown',
    metadata: {},
    source: [
      `# Exploratory Data Analysis\n`,
      `\n`,
      `**File:** ${selectedFile.name}\n`,
      `**Generated:** ${new Date().toISOString()}\n`,
    ],
  })

  cells.push({
    cell_type: 'code',
    metadata: {},
    source: [
      'import pandas as pd\n',
      'import numpy as np\n',
      'import matplotlib.pyplot as plt\n',
      'import seaborn as sns\n',
      '\n',
      'plt.style.use("seaborn-v0_8-whitegrid")\n',
      'sns.set_palette("husl")\n',
      '%matplotlib inline\n',
    ],
    execution_count: null,
    outputs: [],
  })

  const loadCode = selectedFile.path.endsWith('.parquet')
    ? `df = pd.read_parquet("${selectedFile.path}")`
    : `df = pd.read_csv("${selectedFile.path}")`

  cells.push({
    cell_type: 'code',
    metadata: {},
    source: ['# Load dataset\n', loadCode + '\n', 'print(f"Dataset shape: {df.shape}")\n', 'df.head(10)\n'],
    execution_count: null,
    outputs: [],
  })

  cells.push({ cell_type: 'markdown', metadata: {}, source: ['## Dataset Overview\n'] })
  cells.push({
    cell_type: 'code',
    metadata: {},
    source: ['df.info()\n', 'print("\\n")\n', 'df.describe(include="all").T\n'],
    execution_count: null,
    outputs: [],
  })

  cells.push({ cell_type: 'markdown', metadata: {}, source: ['## Missing Values\n'] })
  cells.push({
    cell_type: 'code',
    metadata: {},
    source: [
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
    ],
    execution_count: null,
    outputs: [],
  })

  const numericCols = profile.columns.filter(c => ['numeric', 'integer', 'float'].includes(c.dtype)).slice(0, 6).map(c => c.name)

  if (numericCols.length > 0) {
    cells.push({ cell_type: 'markdown', metadata: {}, source: ['## Distributions\n'] })
    cells.push({
      cell_type: 'code',
      metadata: {},
      source: [
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
      ],
      execution_count: null,
      outputs: [],
    })
  }

  cells.push({ cell_type: 'markdown', metadata: {}, source: ['## Correlations\n'] })
  cells.push({
    cell_type: 'code',
    metadata: {},
    source: [
      'numeric_df = df.select_dtypes(include=[np.number])\n',
      'if len(numeric_df.columns) >= 2:\n',
      '    corr = numeric_df.corr()\n',
      '    plt.figure(figsize=(12, 10))\n',
      '    mask = np.triu(np.ones_like(corr, dtype=bool))\n',
      '    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="RdBu_r", center=0, square=True)\n',
      '    plt.title("Correlation Matrix")\n',
      '    plt.tight_layout()\n',
      '    plt.show()\n',
    ],
    execution_count: null,
    outputs: [],
  })

  if (transforms.length > 0) {
    cells.push({ cell_type: 'markdown', metadata: {}, source: ['## Data Transformations\n'] })

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

    cells.push({ cell_type: 'code', metadata: {}, source: transformCode, execution_count: null, outputs: [] })

    cells.push({
      cell_type: 'code',
      metadata: {},
      source: [
        `output_path = "${selectedFile.path.replace(/\.[^.]+$/, '_transformed.csv')}"\n`,
        'df_transformed.to_csv(output_path, index=False)\n',
        'print(f"Saved to: {output_path}")\n',
      ],
      execution_count: null,
      outputs: [],
    })
  }

  cells.push({
    cell_type: 'markdown',
    metadata: {},
    source: [
      '## Summary\n',
      `- **Rows:** ${profile.summary.total_rows.toLocaleString()}\n`,
      `- **Columns:** ${profile.summary.total_columns}\n`,
      `- **Memory:** ${profile.summary.memory_usage_mb.toFixed(2)} MB\n`,
      `- **Transformations:** ${transforms.length}\n`,
    ],
  })

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

export default EDAAnalysis
