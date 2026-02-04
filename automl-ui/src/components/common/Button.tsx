import { ButtonHTMLAttributes, forwardRef } from 'react'
import clsx from 'clsx'

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'danger' | 'ghost' | 'outline'
  size?: 'sm' | 'md' | 'lg'
  isLoading?: boolean
}

const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = 'primary', size = 'md', isLoading, children, disabled, ...props }, ref) => {
    const baseStyles = 'inline-flex items-center justify-center font-medium whitespace-nowrap text-center transition-all duration-200 select-none rounded disabled:cursor-not-allowed'

    const variants = {
      primary: 'bg-domino-accent-purple text-white hover:bg-domino-accent-purple-hover border border-transparent disabled:opacity-60',
      secondary: 'bg-white text-domino-text-primary hover:border-domino-accent-purple hover:text-domino-accent-purple border border-[#d9d9d9] disabled:opacity-50',
      outline: 'bg-white text-domino-accent-purple hover:bg-domino-accent-purple/5 border border-domino-accent-purple disabled:opacity-50',
      danger: 'bg-domino-accent-red text-white hover:bg-domino-accent-red/90 border border-transparent disabled:opacity-60',
      ghost: 'text-domino-text-secondary hover:text-domino-text-primary hover:bg-domino-bg-tertiary border border-transparent disabled:opacity-50',
    }

    const sizes = {
      sm: 'h-[24px] px-[10px] text-xs',
      md: 'h-[32px] px-[16px] text-sm',
      lg: 'h-[40px] px-[20px] text-base',
    }

    return (
      <button
        ref={ref}
        className={clsx(baseStyles, variants[variant], sizes[size], className)}
        disabled={disabled || isLoading}
        {...props}
      >
        {isLoading && (
          <svg
            className="animate-spin -ml-1 mr-2 h-4 w-4"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle
              className="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              strokeWidth="4"
            />
            <path
              className="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            />
          </svg>
        )}
        {children}
      </button>
    )
  }
)

Button.displayName = 'Button'

export default Button
