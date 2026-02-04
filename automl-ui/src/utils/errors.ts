/**
 * Utility functions for error handling
 */

/**
 * Extract a user-friendly error message from an unknown error
 */
export function getErrorMessage(error: unknown): string {
  if (error instanceof Error) {
    return error.message
  }
  if (typeof error === 'string') {
    return error
  }
  if (error && typeof error === 'object' && 'message' in error) {
    return String((error as { message: unknown }).message)
  }
  return 'An unexpected error occurred'
}

/**
 * Check if an error is an abort error (e.g., from cancelled requests)
 */
export function isAbortError(error: unknown): boolean {
  return error instanceof Error && error.name === 'AbortError'
}

/**
 * Check if an error is a network error
 */
export function isNetworkError(error: unknown): boolean {
  if (error instanceof Error) {
    return error.message.includes('network') ||
           error.message.includes('Network') ||
           error.message.includes('Failed to fetch')
  }
  return false
}

/**
 * Log an error to console in development, suppress in production
 */
export function logError(context: string, error: unknown): void {
  // In production builds, Vite replaces import.meta.env.PROD with true/false
  if (!import.meta.env.PROD) {
    console.error(`[${context}]`, error)
  }
}
