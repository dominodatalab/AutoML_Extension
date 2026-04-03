import {
  CircleStackIcon,
  DocumentIcon,
  CheckCircleIcon,
} from '@heroicons/react/24/outline'
import clsx from 'clsx'
import Spinner from '../common/Spinner'
import { Dataset, DatasetFile } from '../../types/dataset'

interface DataSourceSelectorProps {
  datasets: Dataset[]
  loadingDatasets: boolean
  datasetsError?: string | null
  selectedDataset: Dataset | null
  onSelectDataset: (dataset: Dataset) => void
  onSelectFile: (file: DatasetFile) => void
  formatSize: (bytes: number) => string
  projectName?: string
}

export function DataSourceSelector({
  datasets,
  loadingDatasets,
  datasetsError,
  selectedDataset,
  onSelectDataset,
  onSelectFile,
  formatSize,
  projectName,
}: DataSourceSelectorProps) {
  return (
    <div className="space-y-3">
      {loadingDatasets ? (
        <div className="flex justify-center py-8">
          <Spinner />
        </div>
      ) : datasetsError ? (
        <div className="text-center py-8">
          <CircleStackIcon className="h-12 w-12 text-domino-accent-red mx-auto mb-4" />
          <p className="text-domino-accent-red">Failed to load datasets</p>
          <p className="text-sm text-domino-text-muted mt-2">{datasetsError}</p>
        </div>
      ) : datasets.length === 0 ? (
        <div className="text-center py-8">
          <CircleStackIcon className="h-12 w-12 text-domino-text-muted mx-auto mb-4" />
          <p className="text-domino-text-muted">No datasets found in {projectName || 'this project'}</p>
          <p className="text-sm text-domino-text-muted mt-2">
            Create a dataset in this project and add the data you want to use to get started
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
  )
}
