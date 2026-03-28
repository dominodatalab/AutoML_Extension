import { useCallback, useEffect, useMemo, useState } from 'react'
import { useDropzone } from 'react-dropzone'
import { CloudArrowUpIcon, CircleStackIcon, CheckCircleIcon, DocumentIcon } from '@heroicons/react/24/outline'
import clsx from 'clsx'
import { useWizard } from '../../hooks/useWizard'
import { useDatasets, useUploadFile, useDatasetPreview } from '../../hooks/useDatasets'
import { useStore } from '../../store'
import Spinner from '../common/Spinner'
import { Dataset, DatasetFile } from '../../types/dataset'
import { getDatasetFiles } from '../../api/datasets'
import { toDominoTenantUrl } from '../../utils/dominoLinks'
import { useProjectUserSummary } from '@/hooks/useProjectUserSummary'

function Step1DataSource() {
  const userSummary = useProjectUserSummary()
  const { dataSource, setDataSource } = useWizard()
  const { data: datasetsData, isLoading: loadingDatasets, error: datasetsError } = useDatasets()
  const uploadMutation = useUploadFile()
  const addNotification = useStore((state) => state.addNotification)
  const [sourceType, setSourceType] = useState<'upload' | 'domino_dataset'>(
    dataSource?.type || 'domino_dataset'
  )
  const [openDatasetId, setOpenDatasetId] = useState<string | null>(
    dataSource?.type === 'domino_dataset' ? dataSource.datasetId ?? null : null
  )
  const [datasetDetailsById, setDatasetDetailsById] = useState<Record<string, Dataset>>({})
  const [loadingDatasetIds, setLoadingDatasetIds] = useState<Record<string, boolean>>({})
  const [datasetErrorsById, setDatasetErrorsById] = useState<Record<string, string>>({})

  const baseDatasets = datasetsData?.datasets || []
  const datasets = useMemo(
    () =>
      baseDatasets.map((dataset) => {
        const mergedDataset = datasetDetailsById[dataset.id]
        return mergedDataset
          ? {
              ...dataset,
              ...mergedDataset,
              files: mergedDataset.files,
              file_count: mergedDataset.file_count,
              size_bytes: mergedDataset.size_bytes,
            }
          : dataset
      }),
    [baseDatasets, datasetDetailsById]
  )
  const selectedDatasetId = dataSource?.type === 'domino_dataset' ? dataSource.datasetId ?? null : null
  const datasetLoadError = datasetsError instanceof Error ? datasetsError.message : null

  // Fetch preview/schema only for Domino datasets (uploaded files already have columns from upload response)
  const previewFilePath = dataSource?.type === 'domino_dataset' && dataSource?.filePath ? dataSource.filePath : ''
  const { data: previewData, isLoading: loadingPreview } = useDatasetPreview(
    previewFilePath,
    10, // Only fetch 10 rows to get columns
    undefined, // no offset
    selectedDatasetId || undefined
  )

  const onDrop = useCallback(
    async (acceptedFiles: File[]) => {
      if (acceptedFiles.length === 0) return

      const file = acceptedFiles[0]
      try {
        const result = await uploadMutation.mutateAsync(file)
        setDataSource({
          type: 'upload',
          filePath: result.file_path,
          fileName: result.file_name,
          columns: result.columns,
          rowCount: result.row_count,
        })
      } catch (error) {
        console.error('Upload failed:', error)
        addNotification(
          error instanceof Error ? error.message : 'File upload failed. Please try again.',
          'error'
        )
      }
    },
    [uploadMutation, setDataSource, addNotification]
  )

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'text/csv': ['.csv'],
      'application/vnd.apache.parquet': ['.parquet', '.pq'],
    },
    maxFiles: 1,
  })

  const handleSelectDataset = async (dataset: Dataset) => {
    const shouldOpen = openDatasetId !== dataset.id
    setOpenDatasetId(shouldOpen ? dataset.id : null)

    if (selectedDatasetId !== dataset.id) {
      setDataSource({
        type: 'domino_dataset',
        datasetId: dataset.id,
        fileName: dataset.name,
      })
    }

    if (!shouldOpen || datasetDetailsById[dataset.id] || loadingDatasetIds[dataset.id]) {
      return
    }

    setLoadingDatasetIds((current) => ({ ...current, [dataset.id]: true }))
    setDatasetErrorsById((current) => {
      const next = { ...current }
      delete next[dataset.id]
      return next
    })

    try {
      const detailedDataset = await getDatasetFiles(dataset.id)
      if (detailedDataset) {
        setDatasetDetailsById((current) => ({ ...current, [dataset.id]: detailedDataset }))
      }
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Failed to load dataset files'
      setDatasetErrorsById((current) => ({ ...current, [dataset.id]: message }))
      addNotification(message, 'error')
    } finally {
      setLoadingDatasetIds((current) => {
        const next = { ...current }
        delete next[dataset.id]
        return next
      })
    }
  }

  const handleSelectFile = async (dataset: Dataset, file: DatasetFile) => {
    // Set the file path - the useDatasetPreview hook will fetch columns
    setDataSource({
      type: 'domino_dataset',
      datasetId: dataset.id,
      fileName: file.name,
      filePath: file.path,
    })
  }

  // Update dataSource with columns when preview data is loaded
  useEffect(() => {
    if (previewData?.columns && dataSource?.type === 'domino_dataset' && dataSource?.filePath) {
      // Only update if columns are different
      const currentColumns = dataSource.columns?.join(',') || ''
      const newColumns = previewData.columns.join(',')
      if (currentColumns !== newColumns) {
        setDataSource({
          ...dataSource,
          columns: previewData.columns,
          rowCount: previewData.total_rows,
        })
      }
    }
  }, [previewData, dataSource?.filePath])

  const formatSize = (bytes: number): string => {
    if (bytes < 1024) return `${bytes} B`
    if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`
    return `${(bytes / (1024 * 1024)).toFixed(1)} MB`
  }

  return (
    <div className="space-y-6">
      {/*<div>
        <h2 className="text-lg font-normal text-domino-text-primary mb-2">
          Select Data Source
        </h2>
        <p className="text-domino-text-secondary">
          Upload a file or select from mounted Domino datasets
        </p>
      </div>*/}

      <div className="flex gap-4">
        {/*<button
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
          <p className="text-sm text-domino-text-secondary">
            Upload a CSV or Parquet file
          </p>
        </button>*/}

        <button
          onClick={() => setSourceType('domino_dataset')}
          className={clsx(
            'flex-1 p-4 border transition-colors text-left',
            sourceType === 'domino_dataset'
              ? 'border-domino-accent-purple bg-domino-accent-purple/5'
              : 'border-domino-border bg-white hover:border-domino-text-muted'
          )}
        >
          <CircleStackIcon className="h-6 w-6 text-domino-accent-purple mb-2" />
          <p className="font-medium text-domino-text-primary">Domino Dataset</p>
          <p className="text-sm text-domino-text-secondary">
            Select from your Domino datasets.
            <button className="text-domino-accent-purple hover:underline" onClick={() => window.open(toDominoTenantUrl(`/u/${userSummary.project_owner}/${userSummary.project_name}/data?tab=datasets`), '_blank')}>
              Click here to upload new files to your datasets
            </button>
          </p>
        </button>
      </div>

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
            ) : dataSource?.type === 'upload' && dataSource.fileName ? (
              <div className="flex flex-col items-center">
                <CheckCircleIcon className="h-12 w-12 text-domino-accent-green mb-4" />
                <p className="font-medium text-domino-text-primary">
                  {dataSource.fileName}
                </p>
                <p className="text-sm text-domino-text-secondary">
                  {dataSource.columns?.length} columns, {dataSource.rowCount?.toLocaleString()} rows
                </p>
                <button className="mt-4 text-sm text-domino-accent-purple hover:underline">
                  Choose Different File
                </button>
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

      {sourceType === 'domino_dataset' && (
        <div className="space-y-3">
          {loadingDatasets ? (
            <div className="flex justify-center py-8">
              <Spinner />
            </div>
          ) : datasetLoadError ? (
            <div className="text-center py-8">
              <CircleStackIcon className="h-12 w-12 text-domino-accent-red mx-auto mb-4" />
              <p className="text-domino-accent-red">Failed to load mounted datasets</p>
              <p className="text-sm text-domino-text-muted mt-2">{datasetLoadError}</p>
            </div>
          ) : datasets.length === 0 ? (
            <div className="text-center py-8">
              <CircleStackIcon className="h-12 w-12 text-domino-text-muted mx-auto mb-4" />
              <p className="text-domino-text-muted">No datasets found in {userSummary.project_name || 'this project'}</p>
              <p className="text-sm text-domino-text-muted mt-2">
                Create a dataset in this project and add the data you want to use to get started
              </p>
            </div>
          ) : (
            datasets.map((dataset: Dataset) => {
              const isOpen = openDatasetId === dataset.id
              const isSelected = selectedDatasetId === dataset.id
              const isLoadingFiles = Boolean(loadingDatasetIds[dataset.id])
              const datasetFiles = dataset.files.filter(
                (file) =>
                  file.name.endsWith('.csv') ||
                  file.name.endsWith('.parquet') ||
                  file.name.endsWith('.pq')
              )

              return (
                <div key={dataset.id} className="space-y-2">
                  <button
                    onClick={() => {
                      void handleSelectDataset(dataset)
                    }}
                    className={clsx(
                      'w-full p-4 rounded-lg border-2 transition-colors text-left flex items-center gap-4',
                      isOpen || isSelected
                        ? 'border-domino-accent-purple bg-domino-accent-purple/10'
                        : 'border-domino-border hover:border-domino-text-muted'
                    )}
                  >
                    <CircleStackIcon className="h-8 w-8 text-domino-accent-purple flex-shrink-0" />
                    <div className="flex-1 min-w-0">
                      <p className="font-medium text-domino-text-primary truncate">
                        {dataset.name}
                      </p>
                      <p className="text-sm text-domino-text-secondary">
                        {dataset.file_count ? `${dataset.file_count} files, ` : ''}{dataset.size_bytes ? formatSize(dataset.size_bytes) : ''}
                      </p>
                    </div>
                    {isLoadingFiles ? (
                      <Spinner size="sm" />
                    ) : (isOpen || isSelected) && (
                      <CheckCircleIcon className="h-6 w-6 text-domino-accent-green flex-shrink-0" />
                    )}
                  </button>

                  {isOpen && datasetErrorsById[dataset.id] && (
                    <div className="ml-8 rounded-lg border border-domino-accent-red/30 bg-domino-accent-red/5 px-3 py-2">
                      <p className="text-sm text-domino-accent-red">{datasetErrorsById[dataset.id]}</p>
                    </div>
                  )}

                  {isOpen && isLoadingFiles && (
                    <div className="ml-8 flex items-center gap-2 py-2 text-sm text-domino-text-secondary">
                      <Spinner size="sm" />
                      <span>Loading dataset files...</span>
                    </div>
                  )}

                  {isOpen && !isLoadingFiles && datasetFiles.length > 0 && (
                    <div className="ml-8 space-y-1">
                      {datasetFiles.map((file) => (
                        <button
                          key={file.path}
                          onClick={() => handleSelectFile(dataset, file)}
                          className={clsx(
                            'w-full p-3 rounded-lg border transition-colors text-left flex items-center gap-3',
                            dataSource?.filePath === file.path
                              ? 'border-domino-accent-purple bg-domino-accent-purple/10'
                              : 'border-domino-border hover:border-domino-text-muted'
                          )}
                        >
                          <DocumentIcon className="h-5 w-5 text-domino-text-muted flex-shrink-0" />
                          <div className="flex-1 min-w-0">
                            <p className="text-sm text-domino-text-primary truncate">
                              {file.name}
                            </p>
                            <p className="text-xs text-domino-text-muted">
                              {formatSize(file.size)}
                              {dataSource?.filePath === file.path && dataSource?.columns && (
                                <span className="ml-2">• {dataSource.columns.length} columns</span>
                              )}
                            </p>
                          </div>
                          {dataSource?.filePath === file.path && (
                            loadingPreview ? (
                              <Spinner size="sm" />
                            ) : (
                              <CheckCircleIcon className="h-5 w-5 text-domino-accent-green flex-shrink-0" />
                            )
                          )}
                        </button>
                      ))}
                    </div>
                  )}

                  {isOpen && !isLoadingFiles && !datasetErrorsById[dataset.id] && datasetFiles.length === 0 && (
                    <div className="ml-8 rounded-lg border border-domino-border px-3 py-2">
                      <p className="text-sm text-domino-text-muted">No supported CSV or Parquet files found.</p>
                    </div>
                  )}
                </div>
              )
            })
          )}
        </div>
      )}

    </div>
  )
}

export default Step1DataSource
