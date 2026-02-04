import clsx from 'clsx'
import {
  TableCellsIcon,
  ChartBarIcon,
  PhotoIcon,
  CheckCircleIcon,
} from '@heroicons/react/24/outline'
import { useWizard } from '../../hooks/useWizard'
import { ModelType, ProblemType } from '../../types/job'

interface ModelOption {
  type: ModelType
  name: string
  description: string
  icon: React.ComponentType<{ className?: string }>
  useCases: string[]
}

const modelOptions: ModelOption[] = [
  {
    type: 'tabular',
    name: 'Tabular',
    description: 'For structured data with rows and columns',
    icon: TableCellsIcon,
    useCases: [
      'Classification & regression',
      'Equipment failure prediction',
      'Well log analysis',
    ],
  },
  {
    type: 'timeseries',
    name: 'Time Series',
    description: 'For forecasting sequential data',
    icon: ChartBarIcon,
    useCases: [
      'Production forecasting',
      'Demand prediction',
      'Anomaly detection',
    ],
  },
  {
    type: 'multimodal',
    name: 'Multimodal',
    description: 'For mixed data types including images and text',
    icon: PhotoIcon,
    useCases: [
      'Seismic interpretation',
      'Document analysis',
      'Image + metadata',
    ],
  },
]

const problemTypes: { value: ProblemType; label: string; description: string }[] = [
  {
    value: 'binary',
    label: 'Binary Classification',
    description: 'Predict one of two classes',
  },
  {
    value: 'multiclass',
    label: 'Multiclass Classification',
    description: 'Predict one of multiple classes',
  },
  {
    value: 'regression',
    label: 'Regression',
    description: 'Predict a continuous value',
  },
]

function Step2ModelType() {
  const { modelType, setModelType } = useWizard()

  const handleSelectModelType = (type: ModelType) => {
    setModelType({
      modelType: type,
      problemType: modelType?.modelType === type ? modelType.problemType : undefined,
    })
  }

  const handleSelectProblemType = (problemType: ProblemType) => {
    if (modelType) {
      setModelType({
        ...modelType,
        problemType,
      })
    }
  }

  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-lg font-semibold text-domino-text-primary mb-2">
          Select Model Type
        </h2>
        <p className="text-domino-text-secondary">
          Choose the AutoGluon predictor that best fits your use case
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {modelOptions.map((option) => (
          <button
            key={option.type}
            onClick={() => handleSelectModelType(option.type)}
            className={clsx(
              'p-6 rounded-lg border-2 transition-colors text-left relative',
              modelType?.modelType === option.type
                ? 'border-domino-accent-purple bg-domino-accent-purple/10'
                : 'border-domino-border hover:border-domino-text-muted'
            )}
          >
            {modelType?.modelType === option.type && (
              <CheckCircleIcon className="absolute top-4 right-4 h-6 w-6 text-domino-accent-purple" />
            )}
            <option.icon className="h-8 w-8 text-domino-accent-purple mb-3" />
            <h3 className="font-semibold text-domino-text-primary mb-1">
              {option.name}
            </h3>
            <p className="text-sm text-domino-text-secondary mb-4">
              {option.description}
            </p>
            <ul className="space-y-1">
              {option.useCases.map((useCase) => (
                <li
                  key={useCase}
                  className="text-xs text-domino-text-muted flex items-center gap-2"
                >
                  <span className="h-1 w-1 rounded-full bg-domino-text-muted" />
                  {useCase}
                </li>
              ))}
            </ul>
          </button>
        ))}
      </div>

      {modelType?.modelType && modelType.modelType !== 'timeseries' && (
        <div>
          <h3 className="text-md font-semibold text-domino-text-primary mb-4">
            Problem Type (Optional)
          </h3>
          <p className="text-sm text-domino-text-secondary mb-4">
            AutoGluon can auto-detect this, but you can specify if you know it
          </p>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {problemTypes.map((problem) => (
              <button
                key={problem.value}
                onClick={() => handleSelectProblemType(problem.value)}
                className={clsx(
                  'p-4 rounded-lg border-2 transition-colors text-left',
                  modelType?.problemType === problem.value
                    ? 'border-domino-accent-purple bg-domino-accent-purple/10'
                    : 'border-domino-border hover:border-domino-text-muted'
                )}
              >
                <p className="font-medium text-domino-text-primary">
                  {problem.label}
                </p>
                <p className="text-sm text-domino-text-secondary">
                  {problem.description}
                </p>
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

export default Step2ModelType
