/**
 * Debug logger for the AutoML frontend.
 *
 * Controlled by VITE_DEBUG_LOGGING env var. When enabled, logs API calls,
 * parameters, responses, and timing to the browser console. When disabled,
 * all calls are no-ops (zero overhead in production).
 *
 * Usage:
 *   import { debug } from '../utils/logger'
 *   debug.request('POST', '/svcprofile', { file_path: '...' })
 *   debug.response('POST', '/svcprofile', 200, data, 142)
 */

const DEBUG_ENABLED =
  import.meta.env.VITE_DEBUG_LOGGING === 'true' ||
  import.meta.env.VITE_DEBUG_LOGGING === '1'

const PREFIX = '%c[AutoML Debug]'
const STYLE = 'color: #3B3BD3; font-weight: bold;'
const STYLE_REQ = 'color: #0a7; font-weight: bold;'
const STYLE_RES = 'color: #07a; font-weight: bold;'
const STYLE_ERR = 'color: #d33; font-weight: bold;'

function noop(..._args: unknown[]) {}

function logRequest(method: string, url: string, body?: unknown, headers?: Record<string, string>) {
  console.groupCollapsed(`${PREFIX} >>> ${method} ${url}`, STYLE_REQ)
  if (headers) {
    // Redact sensitive headers
    const safe = { ...headers }
    for (const key of Object.keys(safe)) {
      if (/^(authorization|cookie|x-api-key)$/i.test(key)) {
        safe[key] = '***'
      }
    }
    console.log('Headers:', safe)
  }
  if (body !== undefined && body !== null) {
    console.log('Body:', body)
  }
  console.log('Time:', new Date().toISOString())
  console.groupEnd()
}

function logResponse(method: string, url: string, status: number, data: unknown, elapsedMs: number) {
  console.groupCollapsed(`${PREFIX} <<< ${method} ${url} [${status}] ${elapsedMs.toFixed(0)}ms`, STYLE_RES)
  console.log('Status:', status)
  console.log('Elapsed:', `${elapsedMs.toFixed(1)}ms`)
  console.log('Data:', data)
  console.groupEnd()
}

function logError(method: string, url: string, error: unknown, elapsedMs: number) {
  console.groupCollapsed(`${PREFIX} !!! ${method} ${url} ERROR ${elapsedMs.toFixed(0)}ms`, STYLE_ERR)
  console.error('Error:', error)
  console.log('Elapsed:', `${elapsedMs.toFixed(1)}ms`)
  console.groupEnd()
}

function logInfo(message: string, ...args: unknown[]) {
  console.log(PREFIX, STYLE, message, ...args)
}

export const debug = {
  enabled: DEBUG_ENABLED,
  request: DEBUG_ENABLED ? logRequest : noop,
  response: DEBUG_ENABLED ? logResponse : noop,
  error: DEBUG_ENABLED ? logError : noop,
  info: DEBUG_ENABLED ? logInfo : noop,
}
