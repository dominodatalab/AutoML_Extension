import { useState, useCallback, useRef } from 'react'
import { useStore } from '../store'

/**
 * A generic hook that encapsulates the common async operation pattern:
 *   loading state, error state, try/catch/finally boilerplate.
 *
 * Usage:
 *   const { execute, loading, error, reset } = useAsyncOperation(
 *     async (id: string) => {
 *       const { data } = await api.post<MyType>('endpoint', { id })
 *       return data
 *     }
 *   )
 *
 * The `execute` wrapper handles setLoading/setError automatically.
 * On success it returns the result; on failure it returns undefined.
 *
 * @param operation  The async function to wrap.
 * @param options.errorMessage  Optional default error message used when the
 *                              caught error is not an Error instance.
 */
export interface UseAsyncOperationOptions {
  /** Fallback error message when the thrown value is not an Error */
  errorMessage?: string
}

export interface UseAsyncOperationResult<TArgs extends unknown[], TReturn> {
  /** Call this to run the wrapped operation */
  execute: (...args: TArgs) => Promise<TReturn | undefined>
  /** True while the operation is in-flight */
  loading: boolean
  /** Non-null when the last invocation failed */
  error: string | null
  /** Clear the error state */
  reset: () => void
}

export function useAsyncOperation<TArgs extends unknown[], TReturn>(
  operation: (...args: TArgs) => Promise<TReturn>,
  options?: UseAsyncOperationOptions,
): UseAsyncOperationResult<TArgs, TReturn> {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const addNotification = useStore((state) => state.addNotification)

  // Keep the latest operation reference stable to avoid stale closures
  // while still allowing the caller to pass an inline arrow.
  const operationRef = useRef(operation)
  operationRef.current = operation

  const optionsRef = useRef(options)
  optionsRef.current = options

  const execute = useCallback(async (...args: TArgs): Promise<TReturn | undefined> => {
    setLoading(true)
    setError(null)
    try {
      const result = await operationRef.current(...args)
      return result
    } catch (err) {
      const fallback = optionsRef.current?.errorMessage ?? 'An error occurred'
      const message = err instanceof Error ? err.message : fallback
      setError(message)
      addNotification(message, 'error')
      return undefined
    } finally {
      setLoading(false)
    }
  }, [addNotification])

  const reset = useCallback(() => {
    setError(null)
  }, [])

  return { execute, loading, error, reset }
}
