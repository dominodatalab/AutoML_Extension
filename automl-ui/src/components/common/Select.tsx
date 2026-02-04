import { ChangeEvent } from 'react'
import Dropdown from './Dropdown'

interface SelectOption {
  value: string
  label: string
}

interface SelectProps {
  label?: string
  error?: string
  options: SelectOption[]
  placeholder?: string
  value?: string
  onChange?: (e: ChangeEvent<HTMLSelectElement>) => void
  disabled?: boolean
  className?: string
}

function Select({
  label,
  error,
  options,
  placeholder,
  value,
  onChange,
  disabled,
  className,
}: SelectProps) {
  const handleChange = (newValue: string) => {
    if (onChange) {
      // Create a synthetic event to maintain backward compatibility
      const syntheticEvent = {
        target: { value: newValue },
      } as ChangeEvent<HTMLSelectElement>
      onChange(syntheticEvent)
    }
  }

  return (
    <div className="w-full">
      {label && (
        <label className="block text-sm font-medium text-domino-text-secondary mb-1">
          {label}
        </label>
      )}
      <Dropdown
        value={value || ''}
        onChange={handleChange}
        options={options}
        placeholder={placeholder}
        disabled={disabled}
        className={className}
      />
      {error && (
        <p className="mt-1 text-sm text-domino-accent-red">{error}</p>
      )}
    </div>
  )
}

export default Select
