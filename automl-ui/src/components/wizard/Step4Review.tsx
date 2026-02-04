import { CheckIcon } from '@heroicons/react/24/outline'
import { useWizard } from '../../hooks/useWizard'

function ReviewItem({
  label,
  value,
}: {
  label: string
  value: string | number | undefined
}) {
  if (!value) return null

  return (
    <div className="flex justify-between py-2 border-b border-domino-border last:border-0">
      <span className="text-domino-text-secondary">{label}</span>
      <span className="font-medium text-domino-text-primary">{value}</span>
    </div>
  )
}

function Step4Review() {
  const { jobName, jobDescription, dataSource, modelType, training } = useWizard()

  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-lg font-semibold text-domino-text-primary mb-2">
          Review Configuration
        </h2>
        <p className="text-domino-text-secondary">
          Review your settings before starting the training job
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="space-y-4">
          <h3 className="font-semibold text-domino-text-primary flex items-center gap-2">
            <div className="h-6 w-6 rounded-full bg-domino-accent-purple flex items-center justify-center">
              <CheckIcon className="h-4 w-4 text-white" />
            </div>
            Job Details
          </h3>
          <div className="bg-domino-bg-tertiary p-4">
            <ReviewItem label="Name" value={jobName} />
            <ReviewItem label="Description" value={jobDescription} />
          </div>
        </div>

        <div className="space-y-4">
          <h3 className="font-semibold text-domino-text-primary flex items-center gap-2">
            <div className="h-6 w-6 rounded-full bg-domino-accent-purple flex items-center justify-center">
              <CheckIcon className="h-4 w-4 text-white" />
            </div>
            Data Source
          </h3>
          <div className="bg-domino-bg-tertiary p-4">
            <ReviewItem
              label="Type"
              value={dataSource?.type === 'upload' ? 'Uploaded File' : 'Domino Dataset'}
            />
            <ReviewItem label="File" value={dataSource?.fileName} />
            {dataSource?.columns && (
              <ReviewItem label="Columns" value={dataSource.columns.length} />
            )}
            {dataSource?.rowCount && (
              <ReviewItem label="Rows" value={dataSource.rowCount.toLocaleString()} />
            )}
          </div>
        </div>

        <div className="space-y-4">
          <h3 className="font-semibold text-domino-text-primary flex items-center gap-2">
            <div className="h-6 w-6 rounded-full bg-domino-accent-purple flex items-center justify-center">
              <CheckIcon className="h-4 w-4 text-white" />
            </div>
            Model Configuration
          </h3>
          <div className="bg-domino-bg-tertiary p-4">
            <ReviewItem
              label="Model Type"
              value={modelType?.modelType ? modelType.modelType.charAt(0).toUpperCase() + modelType.modelType.slice(1) : ''}
            />
            {modelType?.problemType && (
              <ReviewItem
                label="Problem Type"
                value={modelType.problemType.charAt(0).toUpperCase() + modelType.problemType.slice(1)}
              />
            )}
          </div>
        </div>

        <div className="space-y-4">
          <h3 className="font-semibold text-domino-text-primary flex items-center gap-2">
            <div className="h-6 w-6 rounded-full bg-domino-accent-purple flex items-center justify-center">
              <CheckIcon className="h-4 w-4 text-white" />
            </div>
            Training Settings
          </h3>
          <div className="bg-domino-bg-tertiary p-4">
            <ReviewItem label="Target Column" value={training?.targetColumn} />
            {training?.timeColumn && (
              <ReviewItem label="Time Column" value={training.timeColumn} />
            )}
            {training?.idColumn && (
              <ReviewItem label="ID Column" value={training.idColumn} />
            )}
            {training?.predictionLength && (
              <ReviewItem label="Prediction Length" value={training.predictionLength} />
            )}
            <ReviewItem label="Preset" value={training?.preset?.replace(/_/g, ' ')} />
            {training?.timeLimit && (
              <ReviewItem label="Time Limit" value={`${training.timeLimit}s`} />
            )}
            {training?.evalMetric && (
              <ReviewItem label="Eval Metric" value={training.evalMetric} />
            )}
            {training?.experimentName && (
              <ReviewItem label="Experiment" value={training.experimentName} />
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default Step4Review
