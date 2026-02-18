import { useState, useCallback } from 'react'
import { useAsyncOperation } from './useAsyncOperation'
import type { UseAsyncOperationResult } from './useAsyncOperation'

type AsyncOp = Pick<UseAsyncOperationResult<unknown[], unknown>, 'loading' | 'error' | 'reset'>

export function aggregateAsyncState(operations: AsyncOp[]): { loading: boolean; error: string | null } {
  return {
    loading: operations.some((op) => op.loading),
    error: operations.map((op) => op.error).find((err): err is string => err !== null) ?? null,
  }
}

export async function orNull<T>(promise: Promise<T | undefined>): Promise<T | null> {
  const result = await promise
  return result ?? null
}

export async function orArray<T>(promise: Promise<T[] | undefined>): Promise<T[]> {
  const result = await promise
  return result ?? []
}

export async function orFalse(promise: Promise<boolean | undefined>): Promise<boolean> {
  const result = await promise
  return result ?? false
}

/**
 * Combines useState + useAsyncOperation + useCallback into a single call.
 * Replaces the repeated 3-layer pattern (state, operation, callback wrapper)
 * used across useProfiling and useDiagnostics.
 */
export function useApiState<TResult, TArgs extends unknown[]>(
  apiFn: (...args: TArgs) => Promise<TResult>,
  errorMessage: string,
) {
  const [data, setData] = useState<TResult | null>(null)
  const op = useAsyncOperation(async (...args: TArgs) => {
    const result = await apiFn(...args)
    setData(result)
    return result
  }, { errorMessage })
  const execute = useCallback(async (...args: TArgs) => orNull(op.execute(...args)), [op.execute])
  return { data, setData, execute, loading: op.loading, error: op.error, reset: op.reset }
}
