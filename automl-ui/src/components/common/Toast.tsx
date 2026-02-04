import { useEffect } from 'react'
import { XMarkIcon, CheckCircleIcon, ExclamationCircleIcon, InformationCircleIcon } from '@heroicons/react/24/outline'
import { useStore } from '../../store'

export function Toast() {
  const notifications = useStore((state) => state.ui.notifications)
  const removeNotification = useStore((state) => state.removeNotification)

  return (
    <div className="fixed bottom-4 right-4 z-50 flex flex-col gap-2 max-w-sm">
      {notifications.map((notification) => (
        <ToastItem
          key={notification.id}
          id={notification.id}
          message={notification.message}
          type={notification.type}
          onDismiss={removeNotification}
        />
      ))}
    </div>
  )
}

interface ToastItemProps {
  id: string
  message: string
  type: 'success' | 'error' | 'info'
  onDismiss: (id: string) => void
}

function ToastItem({ id, message, type, onDismiss }: ToastItemProps) {
  useEffect(() => {
    const timer = setTimeout(() => {
      onDismiss(id)
    }, 5000)

    return () => clearTimeout(timer)
  }, [id, onDismiss])

  const styles = {
    success: {
      bg: 'bg-green-50 border-green-200',
      icon: 'text-green-500',
      text: 'text-green-800',
    },
    error: {
      bg: 'bg-red-50 border-red-200',
      icon: 'text-red-500',
      text: 'text-red-800',
    },
    info: {
      bg: 'bg-blue-50 border-blue-200',
      icon: 'text-blue-500',
      text: 'text-blue-800',
    },
  }

  const style = styles[type]

  const Icon = type === 'success'
    ? CheckCircleIcon
    : type === 'error'
      ? ExclamationCircleIcon
      : InformationCircleIcon

  return (
    <div
      className={`flex items-start gap-3 p-4 rounded-lg border shadow-lg animate-slide-in ${style.bg}`}
      role="alert"
    >
      <Icon className={`w-5 h-5 flex-shrink-0 ${style.icon}`} />
      <p className={`text-sm flex-1 ${style.text}`}>{message}</p>
      <button
        onClick={() => onDismiss(id)}
        className={`flex-shrink-0 ${style.text} hover:opacity-70`}
      >
        <XMarkIcon className="w-5 h-5" />
      </button>
    </div>
  )
}
