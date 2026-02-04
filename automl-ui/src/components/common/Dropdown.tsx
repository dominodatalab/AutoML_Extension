import { useState, useRef, useEffect } from 'react'
import clsx from 'clsx'

interface DropdownOption {
  value: string
  label: string
}

interface DropdownProps {
  value: string
  onChange: (value: string) => void
  options: DropdownOption[]
  placeholder?: string
  className?: string
  disabled?: boolean
  label?: string
}

export function Dropdown({
  value,
  onChange,
  options,
  placeholder = 'Select...',
  className,
  disabled = false,
  label,
}: DropdownProps) {
  const [isOpen, setIsOpen] = useState(false)
  const dropdownRef = useRef<HTMLDivElement>(null)

  const selectedOption = options.find(opt => opt.value === value)

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  const handleSelect = (optionValue: string) => {
    onChange(optionValue)
    setIsOpen(false)
  }

  return (
    <div className={clsx('relative', className)} ref={dropdownRef}>
      {label && (
        <label className="block text-sm font-medium text-domino-text-secondary mb-1">
          {label}
        </label>
      )}
      <button
        type="button"
        onClick={() => !disabled && setIsOpen(!isOpen)}
        disabled={disabled}
        className={clsx(
          'w-full h-[32px] px-3 bg-white text-left text-sm',
          'border border-[#d9d9d9] flex items-center justify-between',
          'transition-all duration-200',
          'hover:border-domino-accent-purple focus:outline-none focus:border-domino-accent-purple',
          disabled && 'opacity-50 cursor-not-allowed',
          !disabled && 'cursor-pointer'
        )}
      >
        <span className={selectedOption ? 'text-domino-text-primary' : 'text-domino-text-muted'}>
          {selectedOption?.label || placeholder}
        </span>
        <svg
          className={clsx(
            'w-4 h-4 text-domino-text-muted transition-transform',
            isOpen && 'rotate-180'
          )}
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      {isOpen && (
        <div className="absolute top-full left-0 right-0 mt-1 bg-white border border-gray-200 shadow-lg z-50 max-h-60 overflow-auto">
          {options.map((option) => (
            <button
              key={option.value}
              type="button"
              onClick={() => handleSelect(option.value)}
              className={clsx(
                'w-full px-3 py-2 text-left text-sm transition-colors',
                'hover:bg-domino-bg-tertiary',
                option.value === value
                  ? 'text-domino-accent-purple bg-domino-bg-tertiary'
                  : 'text-domino-text-primary'
              )}
            >
              {option.label}
            </button>
          ))}
        </div>
      )}
    </div>
  )
}

export default Dropdown
