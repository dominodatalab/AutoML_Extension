import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import Stepper from '../components/common/Stepper'
import Button from '../components/common/Button'
import { useWizard } from '../hooks/useWizard'
import Step1DataSource from '../components/wizard/Step1DataSource'
import Step2ModelType from '../components/wizard/Step2ModelType'
import Step3Configuration from '../components/wizard/Step3Configuration'
import Step4Review from '../components/wizard/Step4Review'

const steps = [
  { name: 'Data Source', description: 'Select your training data' },
  { name: 'Model Type', description: 'Choose the model type' },
  { name: 'Configuration', description: 'Configure training parameters' },
  { name: 'Review', description: 'Review and submit' },
]

function NewJob() {
  const navigate = useNavigate()
  const wizard = useWizard()
  const [submitError, setSubmitError] = useState<string | null>(null)

  const handleSubmit = async () => {
    try {
      setSubmitError(null)
      const jobId = await wizard.submit()
      navigate(`/jobs/${jobId}`)
    } catch (error) {
      setSubmitError(error instanceof Error ? error.message : 'Failed to create job')
    }
  }

  const renderStep = () => {
    switch (wizard.currentStep) {
      case 0:
        return <Step1DataSource />
      case 1:
        return <Step2ModelType />
      case 2:
        return <Step3Configuration />
      case 3:
        return <Step4Review />
      default:
        return null
    }
  }

  return (
    <div className="space-y-8">
      <div>
        <nav className="flex items-center gap-2 text-sm mb-2">
          <Link to="/dashboard" className="text-domino-accent-purple hover:underline">
            AutoML
          </Link>
          <span className="text-domino-text-muted">/</span>
          <span className="text-domino-text-secondary">New training job</span>
        </nav>
        <div className="flex items-center justify-between flex-wrap mb-5">
          <div>
            <h1 className="text-2xl font-normal text-domino-text-primary leading-tight">
              New training job
            </h1>
            <p className="text-sm text-domino-text-secondary mt-1">
              Configure and run an AutoGluon training job
            </p>
          </div>
        </div>
      </div>

      <div className="mb-16">
        <Stepper
          steps={steps}
          currentStep={wizard.currentStep}
          onStepClick={wizard.goToStep}
        />
      </div>

      <div className="py-6">
        {renderStep()}
      </div>

      {submitError && (
        <div className="p-4 bg-domino-accent-red/10 border border-domino-accent-red">
          <p className="text-domino-accent-red">{submitError}</p>
        </div>
      )}

      <div className="flex justify-between">
        <Button
          variant="secondary"
          onClick={wizard.back}
          disabled={!wizard.canGoBack}
        >
          Back
        </Button>

        {wizard.currentStep === 3 ? (
          <Button
            onClick={handleSubmit}
            disabled={!wizard.canProceed}
            isLoading={wizard.isSubmitting}
          >
            Start Training
          </Button>
        ) : (
          <Button onClick={wizard.next} disabled={!wizard.canProceed}>
            Continue
          </Button>
        )}
      </div>
    </div>
  )
}

export default NewJob
