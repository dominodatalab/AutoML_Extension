import { useDropzone } from 'react-dropzone'
import {
  CloudArrowUpIcon,
  CircleStackIcon,
  DocumentIcon,
  CheckCircleIcon,
} from '@heroicons/react/24/outline'
import clsx from 'clsx'
import Spinner from '../common/Spinner'
import { Dataset, DatasetFile } from '../../types/dataset'

interface DataSourceSelectorProps {
  sourceType: 'upload' | 'dataset'
  setSourceType: (type: 'upload' | 'dataset') => void
  datasets: Dataset[]
  loadingDatasets: boolean
  datasetsError?: string | null
  selectedDataset: Dataset | null
  selectedDatasetFiles?: DatasetFile[]
  loadingSelectedDatasetFiles?: boolean
  uploadIsPending: boolean
  onDrop: (acceptedFiles: File[]) => void
  onSelectDataset: (dataset: Dataset) => void
  onSelectFile: (file: DatasetFile) => void
  formatSize: (bytes: number) => string
  isVerifying?: boolean
  verifyError?: string | null
  uploadedFileName?: string | null
  onProceedAnyway?: () => void
}

export function DataSourceSelector({
  sourceType,
  setSourceType,
  datasets,
  loadingDatasets,
  datasetsError,
  selectedDataset,
  selectedDatasetFiles = [],
  loadingSelectedDatasetFiles = false,
  uploadIsPending,
  onDrop,
  onSelectDataset,
  onSelectFile,
  formatSize,
  isVerifying,
  verifyError,
  uploadedFileName,
  onProceedAnyway,
}: DataSourceSelectorProps) {
  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'text/csv': ['.csv'],
      'application/vnd.apache.parquet': ['.parquet', '.pq'],
    },
    maxFiles: 1,
  })

  const getDatasetSummary = (dataset: Dataset): string => {
    const isSelected = selectedDataset?.id === dataset.id
    const derivedFileCount = isSelected ? selectedDatasetFiles.length : 0
    const derivedSize = isSelected
      ? selectedDatasetFiles.reduce((total, file) => total + (file.size || 0), 0)
      : 0
    const fileCount = dataset.file_count > 0 ? dataset.file_count : derivedFileCount
    const sizeBytes = dataset.size_bytes > 0 ? dataset.size_bytes : derivedSize

    if (fileCount > 0 || sizeBytes > 0) {
      return `${fileCount} files, ${formatSize(sizeBytes)}`
    }

    if (isSelected && !loadingSelectedDatasetFiles) {
      return 'No supported files found'
    }

    return 'Browse to inspect files'
  }

  return (
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
            {uploadIsPending ? (
              <div className="flex flex-col items-center">
                <Spinner className="mb-4" />
                <p className="text-domino-text-secondary">Uploading...</p>
              </div>
            ) : isVerifying ? (
              <div className="flex flex-col items-center">
                <Spinner className="mb-4" />
                <p className="font-medium text-domino-text-primary">{uploadedFileName}</p>
                <p className="text-domino-text-secondary mt-2">Syncing with dataset...</p>
                <div className="w-48 h-1 bg-domino-border rounded mt-3 overflow-hidden">
                  <div className="h-full bg-domino-accent-purple rounded animate-pulse" style={{ width: '60%' }} />
                </div>
              </div>
            ) : verifyError ? (
              <div className="flex flex-col items-center">
                <p className="font-medium text-domino-text-primary">{uploadedFileName}</p>
                <p className="text-sm text-domino-accent-red mt-2">{verifyError}</p>
                {onProceedAnyway && (
                  <button
                    onClick={(e) => { e.stopPropagation(); onProceedAnyway() }}
                    className="mt-3 text-sm text-domino-accent-purple hover:underline"
                  >
                    Proceed Anyway
                  </button>
                )}
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
          ) : datasetsError ? (
            <div className="text-center py-8">
              <CircleStackIcon className="h-12 w-12 text-domino-accent-red mx-auto mb-4" />
              <p className="text-domino-accent-red">Failed to load mounted datasets</p>
              <p className="text-sm text-domino-text-muted mt-2">{datasetsError}</p>
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
                  onClick={() => onSelectDataset(dataset)}
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
                      {getDatasetSummary(dataset)}
                    </p>
                  </div>
                  {selectedDataset?.id === dataset.id && (
                    <CheckCircleIcon className="h-6 w-6 text-domino-accent-green flex-shrink-0" />
                  )}
                </button>

                {selectedDataset?.id === dataset.id && loadingSelectedDatasetFiles && selectedDatasetFiles.length === 0 && (
                  <div className="ml-8 py-3">
                    <Spinner size="sm" />
                  </div>
                )}

                {selectedDataset?.id === dataset.id && selectedDatasetFiles.length > 0 && (
                  <div className="ml-8 space-y-1">
                    {selectedDatasetFiles
                      .filter(f => f.name.endsWith('.csv') || f.name.endsWith('.parquet') || f.name.endsWith('.pq'))
                      .map((file) => (
                        <button
                          key={`${dataset.id}:${file.name}`}
                          onClick={() => onSelectFile(file)}
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
  )
}
