import { InputHTMLAttributes, forwardRef } from 'react'
import clsx from 'clsx'

interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label?: string
  error?: string
}

const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ className, label, error, id, ...props }, ref) => {
    const inputId = id || label?.toLowerCase().replace(/\s+/g, '-')

    return (
      <div className="w-full">
        {label && (
          <label
            htmlFor={inputId}
            className="block text-sm font-medium text-domino-text-secondary mb-1"
          >
            {label}
          </label>
        )}
        <input
          ref={ref}
          id={inputId}
          className={clsx(
            'w-full h-[32px] px-[11px] bg-white rounded-[2px] text-domino-text-primary placeholder-domino-text-muted text-sm',
            'border transition-all duration-200',
            'focus:outline-none focus:border-domino-accent-purple',
            'disabled:opacity-50 disabled:cursor-not-allowed',
            error ? 'border-domino-accent-red' : 'border-[#d9d9d9]',
            className
          )}
          {...props}
        />
        {error && (
          <p className="mt-1 text-sm text-domino-accent-red">{error}</p>
        )}
      </div>
    )
  }
)

Input.displayName = 'Input'

export default Input
