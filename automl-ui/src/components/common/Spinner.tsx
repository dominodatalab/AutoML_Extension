import clsx from 'clsx'
import dominoLogo from '../../assets/domino-logo.png'

interface SpinnerProps {
  size?: 'sm' | 'md' | 'lg'
  className?: string
}

function Spinner({ size = 'md', className }: SpinnerProps) {
  const sizes = {
    sm: 'h-4 w-4',
    md: 'h-8 w-8',
    lg: 'h-12 w-12',
  }

  return (
    <img
      src={dominoLogo}
      alt="Loading"
      className={clsx('animate-spin-clockwise', sizes[size], className)}
    />
  )
}

export default Spinner
