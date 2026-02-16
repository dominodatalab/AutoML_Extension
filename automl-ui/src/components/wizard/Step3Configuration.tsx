import { useEffect, useState } from 'react'
import { useWizard } from '../../hooks/useWizard'
import Input from '../common/Input'
import Select from '../common/Select'
import { Preset, AdvancedAutoGluonConfig, TimeSeriesAdvancedConfig, MultimodalAdvancedConfig } from '../../types/job'
import { AdvancedConfigPanel } from './AdvancedConfigPanel'

const presetOptions = [
  { value: 'best_quality', label: 'Best Quality (slowest)' },
  { value: 'high_quality', label: 'High Quality' },
  { value: 'good_quality', label: 'Good Quality' },
  { value: 'medium_quality_faster_train', label: 'Medium Quality (faster)' },
  { value: 'optimize_for_deployment', label: 'Optimize for Deployment' },
]

function Step3Configuration() {
  const { modelType, dataSource, training, setTraining, setJobInfo, jobName, jobDescription } = useWizard()
  const isTimeSeries = modelType?.modelType === 'timeseries'
  const isMultimodal = modelType?.modelType === 'multimodal'

  const [localConfig, setLocalConfig] = useState({
    executionTarget: training?.executionTarget || 'local',
    targetColumn: training?.targetColumn || '',
    timeColumn: training?.timeColumn || '',
    idColumn: training?.idColumn || '',
    predictionLength: training?.predictionLength?.toString() || '10',
    preset: training?.preset || 'medium_quality_faster_train',
    timeLimit: training?.timeLimit?.toString() || '3600',
    evalMetric: training?.evalMetric || '',
    experimentName: training?.experimentName || '',
  })

  const [localJobInfo, setLocalJobInfo] = useState({
    name: jobName || '',
    description: jobDescription || '',
  })

  const [advancedConfig, setAdvancedConfig] = useState<AdvancedAutoGluonConfig>(
    training?.advancedConfig || {}
  )
  const [timeseriesConfig, setTimeseriesConfig] = useState<TimeSeriesAdvancedConfig>(
    training?.timeseriesConfig || {}
  )
  const [multimodalConfig, setMultimodalConfig] = useState<MultimodalAdvancedConfig>(
    training?.multimodalConfig || {}
  )

  // Get columns from data source
  const columns = dataSource?.columns || []
  const columnOptions = columns.map((col) => ({ value: col, label: col }))

  // Update wizard state when local config changes
  useEffect(() => {
    setTraining({
      executionTarget: localConfig.executionTarget as 'local' | 'domino_job',
      targetColumn: localConfig.targetColumn,
      timeColumn: localConfig.timeColumn || undefined,
      idColumn: localConfig.idColumn || undefined,
      predictionLength: localConfig.predictionLength
        ? parseInt(localConfig.predictionLength)
        : undefined,
      preset: localConfig.preset as Preset,
      timeLimit: localConfig.timeLimit ? parseInt(localConfig.timeLimit) : undefined,
      evalMetric: localConfig.evalMetric || undefined,
      experimentName: localConfig.experimentName || undefined,
      advancedConfig: Object.keys(advancedConfig).length > 0 ? advancedConfig : undefined,
      timeseriesConfig: isTimeSeries && Object.keys(timeseriesConfig).length > 0 ? timeseriesConfig : undefined,
      multimodalConfig: isMultimodal && Object.keys(multimodalConfig).length > 0 ? multimodalConfig : undefined,
    })
  }, [localConfig, advancedConfig, timeseriesConfig, multimodalConfig, isTimeSeries, isMultimodal, setTraining])

  // Update wizard job info when local info changes
  useEffect(() => {
    setJobInfo(localJobInfo.name, localJobInfo.description)
  }, [localJobInfo, setJobInfo])

  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-lg font-semibold text-domino-text-primary mb-2">
          Configure Training
        </h2>
        <p className="text-domino-text-secondary">
          Set up the training parameters for your AutoGluon model
        </p>
      </div>

      <div className="space-y-6">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <Input
            label="Job Name"
            placeholder="My training job"
            value={localJobInfo.name}
            onChange={(e) =>
              setLocalJobInfo((prev) => ({ ...prev, name: e.target.value }))
            }
          />
          <Input
            label="Description (optional)"
            placeholder="Describe your training job"
            value={localJobInfo.description}
            onChange={(e) =>
              setLocalJobInfo((prev) => ({ ...prev, description: e.target.value }))
            }
          />
        </div>

        <div className="border-t border-domino-border pt-6">
          <h3 className="text-md font-semibold text-domino-text-primary mb-4">
            Data Configuration
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {columns.length > 0 ? (
              <Select
                label="Target Column"
                options={columnOptions}
                placeholder="Select target column"
                value={localConfig.targetColumn}
                onChange={(e) =>
                  setLocalConfig((prev) => ({ ...prev, targetColumn: e.target.value }))
                }
              />
            ) : (
              <Input
                label="Target Column"
                placeholder="Enter target column name"
                value={localConfig.targetColumn}
                onChange={(e) =>
                  setLocalConfig((prev) => ({ ...prev, targetColumn: e.target.value }))
                }
              />
            )}

            {isTimeSeries && (
              <>
                {columns.length > 0 ? (
                  <Select
                    label="Time Column"
                    options={columnOptions}
                    placeholder="Select time column"
                    value={localConfig.timeColumn}
                    onChange={(e) =>
                      setLocalConfig((prev) => ({ ...prev, timeColumn: e.target.value }))
                    }
                  />
                ) : (
                  <Input
                    label="Time Column"
                    placeholder="Enter time column name"
                    value={localConfig.timeColumn}
                    onChange={(e) =>
                      setLocalConfig((prev) => ({ ...prev, timeColumn: e.target.value }))
                    }
                  />
                )}

                {columns.length > 0 ? (
                  <Select
                    label="ID Column (optional)"
                    options={[{ value: '', label: 'None' }, ...columnOptions]}
                    value={localConfig.idColumn}
                    onChange={(e) =>
                      setLocalConfig((prev) => ({ ...prev, idColumn: e.target.value }))
                    }
                  />
                ) : (
                  <Input
                    label="ID Column (optional)"
                    placeholder="Enter ID column name"
                    value={localConfig.idColumn}
                    onChange={(e) =>
                      setLocalConfig((prev) => ({ ...prev, idColumn: e.target.value }))
                    }
                  />
                )}

                <Input
                  label="Prediction Length"
                  type="number"
                  min="1"
                  placeholder="10"
                  value={localConfig.predictionLength}
                  onChange={(e) =>
                    setLocalConfig((prev) => ({
                      ...prev,
                      predictionLength: e.target.value,
                    }))
                  }
                />
              </>
            )}
          </div>
        </div>

        <div className="border-t border-domino-border pt-6">
          <h3 className="text-md font-semibold text-domino-text-primary mb-4">
            AutoGluon Settings
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <Select
              label="Execution Target"
              options={[
                { value: 'local', label: 'Local (In-App Queue)' },
                { value: 'domino_job', label: 'Domino Job (External)' },
              ]}
              value={localConfig.executionTarget}
              onChange={(e) =>
                setLocalConfig((prev) => ({
                  ...prev,
                  executionTarget: e.target.value as 'local' | 'domino_job',
                }))
              }
            />

            <Select
              label="Preset"
              options={presetOptions}
              value={localConfig.preset}
              onChange={(e) =>
                setLocalConfig((prev) => ({ ...prev, preset: e.target.value as Preset }))
              }
            />

            <Input
              label="Time Limit (seconds)"
              type="number"
              min="60"
              placeholder="3600"
              value={localConfig.timeLimit}
              onChange={(e) =>
                setLocalConfig((prev) => ({ ...prev, timeLimit: e.target.value }))
              }
            />

            <Input
              label="Evaluation Metric (optional)"
              placeholder="Auto-detect"
              value={localConfig.evalMetric}
              onChange={(e) =>
                setLocalConfig((prev) => ({ ...prev, evalMetric: e.target.value }))
              }
            />

            <Input
              label="Experiment Name (optional)"
              placeholder="Auto-generated"
              value={localConfig.experimentName}
              onChange={(e) =>
                setLocalConfig((prev) => ({ ...prev, experimentName: e.target.value }))
              }
            />
          </div>
        </div>

        {/* Advanced Configuration */}
        <div className="border-t border-domino-border pt-6">
          <AdvancedConfigPanel
            modelType={modelType?.modelType || 'tabular'}
            advancedConfig={advancedConfig}
            timeseriesConfig={isTimeSeries ? timeseriesConfig : undefined}
            multimodalConfig={isMultimodal ? multimodalConfig : undefined}
            onAdvancedConfigChange={setAdvancedConfig}
            onTimeseriesConfigChange={isTimeSeries ? setTimeseriesConfig : undefined}
            onMultimodalConfigChange={isMultimodal ? setMultimodalConfig : undefined}
          />
        </div>
      </div>
    </div>
  )
}

export default Step3Configuration
