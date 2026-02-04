import clsx from 'clsx'
import { CheckIcon } from '@heroicons/react/24/solid'

interface Step {
  name: string
  description?: string
}

interface StepperProps {
  steps: Step[]
  currentStep: number
  onStepClick?: (step: number) => void
}

function Stepper({ steps, currentStep, onStepClick }: StepperProps) {
  return (
    <nav aria-label="Progress" className="w-full">
      {/* Grid container - 4 equal columns for 4 steps */}
      <ol
        className="grid gap-0"
        style={{ gridTemplateColumns: `repeat(${steps.length}, 1fr)` }}
      >
        {steps.map((step, index) => {
          const isCompleted = index < currentStep
          const isCurrent = index === currentStep
          const isLast = index === steps.length - 1

          return (
            <li key={step.name} className="relative flex flex-col items-center">
              {/* Connector line (before circle, except first) */}
              {index > 0 && (
                <div
                  className="absolute top-5 right-1/2 w-full h-0.5 -translate-y-1/2"
                  aria-hidden="true"
                >
                  <div
                    className={clsx(
                      'h-full w-full',
                      index <= currentStep ? 'bg-domino-accent-purple' : 'bg-domino-border'
                    )}
                  />
                </div>
              )}

              {/* Connector line (after circle, except last) */}
              {!isLast && (
                <div
                  className="absolute top-5 left-1/2 w-full h-0.5 -translate-y-1/2"
                  aria-hidden="true"
                >
                  <div
                    className={clsx(
                      'h-full w-full',
                      isCompleted ? 'bg-domino-accent-purple' : 'bg-domino-border'
                    )}
                  />
                </div>
              )}

              {/* Step circle */}
              <button
                onClick={() => onStepClick?.(index)}
                disabled={index > currentStep}
                className={clsx(
                  'relative z-10 flex h-10 w-10 items-center justify-center rounded-full transition-colors',
                  isCompleted && 'bg-domino-accent-purple hover:bg-domino-accent-purple/80 cursor-pointer',
                  isCurrent && 'border-2 border-domino-accent-purple bg-domino-bg-primary',
                  !isCompleted && !isCurrent && 'border-2 border-domino-border bg-domino-bg-primary'
                )}
                aria-current={isCurrent ? 'step' : undefined}
              >
                {isCompleted ? (
                  <CheckIcon className="h-5 w-5 text-white" aria-hidden="true" />
                ) : (
                  <span
                    className={clsx(
                      'h-3 w-3 rounded-full',
                      isCurrent ? 'bg-domino-accent-purple' : 'bg-domino-border'
                    )}
                  />
                )}
              </button>

              {/* Step label */}
              <span
                className={clsx(
                  'mt-3 text-xs font-medium text-center',
                  isCompleted || isCurrent
                    ? 'text-domino-text-primary'
                    : 'text-domino-text-muted'
                )}
              >
                {step.name}
              </span>
            </li>
          )
        })}
      </ol>
    </nav>
  )
}

export default Stepper
