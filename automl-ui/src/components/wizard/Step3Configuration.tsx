import { useEffect, useState } from 'react'
import { useWizard } from '../../hooks/useWizard'
import { useCapabilities } from '../../hooks/useCapabilities'
import Input from '../common/Input'
import Select from '../common/Select'
import { Preset, AdvancedAutoGluonConfig, TimeSeriesAdvancedConfig } from '../../types/job'
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
  const { modelRegistry } = useCapabilities()
  const isTimeSeries = modelType?.modelType === 'timeseries'

  const [localConfig, setLocalConfig] = useState({
    targetColumn: training?.targetColumn || '',
    timeColumn: training?.timeColumn || '',
    idColumn: training?.idColumn || '',
    predictionLength: training?.predictionLength?.toString() || '10',
    preset: training?.preset || 'medium_quality_faster_train',
    timeLimit: training?.timeLimit?.toString() || '3600',
    evalMetric: training?.evalMetric || '',
    experimentName: training?.experimentName || '',
    autoRegister: training?.autoRegister || false,
    registerName: training?.registerName || '',
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

// Get columns from data source
  const columns = dataSource?.columns || []
  const columnOptions = columns.map((col) => ({ value: col, label: col }))

  // Update wizard state when local config changes
  useEffect(() => {
    setTraining({
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
      autoRegister: localConfig.autoRegister || undefined,
      registerName: localConfig.autoRegister && localConfig.registerName ? localConfig.registerName : undefined,
    })
  }, [localConfig, advancedConfig, timeseriesConfig, isTimeSeries, setTraining])

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
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
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
          <Input
            label="Execution Target"
            value="Domino Job"
            disabled
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

        {/* Model Registry */}
        {modelRegistry && (
          <div className="border-t border-domino-border pt-6">
            <h3 className="text-md font-semibold text-domino-text-primary mb-4">
              Model Registry
            </h3>
            <div className="space-y-4">
              <label className="flex items-center gap-3 cursor-pointer">
                <input
                  type="checkbox"
                  checked={localConfig.autoRegister}
                  onChange={(e) =>
                    setLocalConfig((prev) => ({ ...prev, autoRegister: e.target.checked }))
                  }
                  className="h-4 w-4 rounded border-domino-border text-domino-accent-purple focus:ring-domino-accent-purple"
                />
                <span className="text-sm text-domino-text-primary">
                  Register model in Domino Model Registry after training
                </span>
              </label>
              {localConfig.autoRegister && (
                <div className="ml-7">
                  <Input
                    label="Registered Model Name (optional)"
                    placeholder="Auto-generated from job name"
                    value={localConfig.registerName}
                    onChange={(e) =>
                      setLocalConfig((prev) => ({ ...prev, registerName: e.target.value }))
                    }
                  />
                </div>
              )}
            </div>
          </div>
        )}

        {/* Advanced Configuration */}
        <div className="border-t border-domino-border pt-6">
          <AdvancedConfigPanel
            modelType={modelType?.modelType || 'tabular'}
            advancedConfig={advancedConfig}
            timeseriesConfig={isTimeSeries ? timeseriesConfig : undefined}
            onAdvancedConfigChange={setAdvancedConfig}
            onTimeseriesConfigChange={isTimeSeries ? setTimeseriesConfig : undefined}
          />
        </div>
      </div>
    </div>
  )
}

export default Step3Configuration
