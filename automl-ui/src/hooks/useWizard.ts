import { useMemo } from 'react'
import { useStore } from '../store'
import { useCreateJob } from './useJobs'
import { JobCreateRequest } from '../types/job'

export function useWizard() {
  const wizard = useStore((state) => state.wizard)
  const setWizardStep = useStore((state) => state.setWizardStep)
  const setWizardDataSource = useStore((state) => state.setWizardDataSource)
  const setWizardModelType = useStore((state) => state.setWizardModelType)
  const setWizardTraining = useStore((state) => state.setWizardTraining)
  const setWizardJobInfo = useStore((state) => state.setWizardJobInfo)
  const resetWizard = useStore((state) => state.resetWizard)

  const createJobMutation = useCreateJob()

  const canProceed = useMemo(() => {
    switch (wizard.currentStep) {
      case 0:
        return wizard.dataSource !== null
      case 1:
        return wizard.modelType !== null
      case 2:
        return (
          wizard.training !== null &&
          wizard.training.targetColumn !== '' &&
          wizard.jobName !== ''
        )
      case 3:
        return wizard.jobName !== ''
      default:
        return false
    }
  }, [wizard])

  const canGoBack = wizard.currentStep > 0

  const next = () => {
    if (canProceed && wizard.currentStep < 3) {
      setWizardStep(wizard.currentStep + 1)
    }
  }

  const back = () => {
    if (canGoBack) {
      setWizardStep(wizard.currentStep - 1)
    }
  }

  const goToStep = (step: number) => {
    if (step >= 0 && step <= 3) {
      setWizardStep(step)
    }
  }

  const submit = async (): Promise<string> => {
    if (!wizard.dataSource || !wizard.modelType || !wizard.training) {
      throw new Error('Wizard is not complete')
    }

    const request: JobCreateRequest = {
      name: wizard.jobName,
      description: wizard.jobDescription || undefined,
      model_type: wizard.modelType.modelType,
      problem_type: wizard.modelType.problemType,
      data_source: wizard.dataSource.type,
      dataset_id: wizard.dataSource.datasetId,
      file_path: wizard.dataSource.filePath,
      target_column: wizard.training.targetColumn,
      time_column: wizard.training.timeColumn,
      id_column: wizard.training.idColumn,
      prediction_length: wizard.training.predictionLength,
      preset: wizard.training.preset,
      time_limit: wizard.training.timeLimit,
      eval_metric: wizard.training.evalMetric,
      experiment_name: wizard.training.experimentName,
      advanced_config: wizard.training.advancedConfig,
      timeseries_config: wizard.training.timeseriesConfig,
      multimodal_config: wizard.training.multimodalConfig,
    }

    const job = await createJobMutation.mutateAsync(request)
    resetWizard()
    return job.id
  }

  return {
    ...wizard,
    canProceed,
    canGoBack,
    next,
    back,
    goToStep,
    submit,
    isSubmitting: createJobMutation.isPending,
    submitError: createJobMutation.error?.message,
    setDataSource: setWizardDataSource,
    setModelType: setWizardModelType,
    setTraining: setWizardTraining,
    setJobInfo: setWizardJobInfo,
    reset: resetWizard,
  }
}
