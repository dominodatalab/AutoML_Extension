import { getBasePath } from '../utils/basePath'
import { debug } from '../utils/logger'

/**
 * Extract projectId from a Location-like object (search then hash).
 */
function extractProjectId(loc: { search: string; hash: string }): string | undefined {
  const fromSearch = new URLSearchParams(loc.search).get('projectId')
  if (fromSearch) return fromSearch

  if (loc.hash) {
    const fromHash = new URLSearchParams(loc.hash.slice(1)).get('projectId')
    if (fromHash) return fromHash
  }
  return undefined
}

/**
 * Read projectId from the URL.
 *
 * Domino loads Apps in an iframe whose src is a clean internal URL with
 * no query params or hash. The user's projectId lives on the *parent*
 * frame's URL, so we check:
 *   1. Current iframe URL (query string, then hash)
 *   2. Parent frame URL (same-origin only; query string, then hash)
 */
function getProjectIdFromUrl(): string | undefined {
  try {
    // 1. Current frame
    const fromSelf = extractProjectId(window.location)
    if (fromSelf) return fromSelf

    // 2. Parent frame (Domino iframe is same-origin)
    if (window.parent && window.parent !== window) {
      try {
        const fromParent = extractProjectId(window.parent.location)
        if (fromParent) return fromParent
      } catch {
        // Cross-origin — ignore
      }
    }

    return undefined
  } catch {
    return undefined
  }
}

// Capture projectId eagerly at module load time so it survives React Router
// navigation that may strip query params from window.location.
let _cachedProjectId: string | undefined = getProjectIdFromUrl()

console.log('[ApiClient] module load — href:', window.location.href, 'parentHref:', (() => { try { return window.parent?.location?.href } catch { return '(cross-origin)' } })(), 'cachedProjectId:', _cachedProjectId)

/**
 * Resolve the current project ID.
 * Priority: explicit override > cached value from initial URL > live URL.
 */
export function getProjectId(): string | undefined {
  return _cachedProjectId || getProjectIdFromUrl()
}

/**
 * Allow external code (e.g. React components with useSearchParams) to
 * persist the project ID so it survives across navigations.
 */
export function setProjectId(id: string | undefined) {
  if (id) {
    _cachedProjectId = id
  }
}

// Extend window type for runtime config
declare global {
  interface Window {
    APP_CONFIG?: {
      API_URL?: string
    }
  }
}

// For Domino Apps: use simple single-segment endpoints
const DOMINO_MODE = true

/**
 * Convert an endpoint name to Domino single-segment compat paths.
 */
function toDominoPath(endpoint: string): string {
  const normalized = endpoint.replace(/^\/+|\/+$/g, '')
  if (!normalized) return 'svc'
  const lastSegment = normalized.split('/').filter(Boolean).pop() || normalized
  return `svc${lastSegment.replace(/-/g, '')}`
}

// Fetch-based API client
class ApiClient {
  private defaultHeaders: Record<string, string>

  constructor() {
    this.defaultHeaders = {
      'Content-Type': 'application/json',
    }
  }

  private async request<T>(
    method: string,
    endpoint: string,
    data?: unknown,
    config?: { params?: Record<string, string | number | boolean | undefined> }
  ): Promise<{ data: T }> {
    const cleanEndpoint = endpoint.startsWith('/') ? endpoint.slice(1) : endpoint

    let fullUrl: string
    if (DOMINO_MODE) {
      // Convert to single-segment Domino-safe path (convention: "svc" + endpoint)
      const mappedPath = toDominoPath(cleanEndpoint)
      const basePath = getBasePath()
      fullUrl = `${basePath}/${mappedPath}`
    } else {
      fullUrl = `/api/v1/${cleanEndpoint}`
    }

    // Add query params
    if (config?.params) {
      const searchParams = new URLSearchParams()
      Object.entries(config.params).forEach(([key, value]) => {
        if (value !== undefined) {
          searchParams.append(key, String(value))
        }
      })
      const queryString = searchParams.toString()
      if (queryString) {
        fullUrl += `?${queryString}`
      }
    }

    const headers: Record<string, string> = { ...this.defaultHeaders }

    // Dynamically resolve project ID on every request so it works even
    // when the module loaded before query params were available, or after
    // React Router navigation strips them from the URL.
    const projectId = getProjectId()
    if (projectId) {
      headers['X-Project-Id'] = projectId
    }

    const fetchConfig: RequestInit = {
      method,
      headers,
      credentials: 'include',
    }

    if (data && method !== 'GET') {
      if (data instanceof FormData) {
        delete headers['Content-Type']
        fetchConfig.body = data
      } else {
        fetchConfig.body = JSON.stringify(data)
      }
    }

    const startTime = performance.now()
    debug.request(method, fullUrl, data, headers)

    try {
      const response = await fetch(fullUrl, fetchConfig)
      const elapsed = performance.now() - startTime

      if (!response.ok) {
        // Check if response is HTML (common when Domino intercepts)
        const contentType = response.headers.get('content-type') || ''
        if (contentType.includes('text/html')) {
          console.error(`[API] Received HTML response instead of JSON for ${fullUrl}`)
          console.error('[API] This usually means Domino is intercepting the request')
          debug.error(method, fullUrl, `HTML response (status ${response.status})`, elapsed)
          throw new Error(`API returned HTML instead of JSON (status ${response.status}). Check if endpoint exists.`)
        }
        const errorData = await response.json().catch(() => ({}))
        // Handle Pydantic validation errors (array of objects)
        let message: string
        if (Array.isArray(errorData.detail)) {
          message = errorData.detail.map((e: { msg?: string; loc?: string[] }) =>
            e.msg ? `${e.loc?.join('.')}: ${e.msg}` : JSON.stringify(e)
          ).join('; ')
        } else if (typeof errorData.detail === 'object' && errorData.detail !== null) {
          message = JSON.stringify(errorData.detail)
        } else {
          message = errorData.detail || errorData.error || response.statusText || 'An error occurred'
        }
        console.error('API Error:', message)
        debug.error(method, fullUrl, { status: response.status, message, errorData }, elapsed)
        const error = new Error(message)
        ;(error as any).status = response.status
        throw error
      }

      if (response.status === 204) {
        debug.response(method, fullUrl, 204, '(no content)', elapsed)
        return { data: {} as T }
      }

      // Check content type before parsing JSON
      const contentType = response.headers.get('content-type') || ''
      if (contentType.includes('text/html')) {
        const htmlPreview = await response.text()
        console.error(`[API] Received HTML instead of JSON for ${fullUrl}:`, htmlPreview.substring(0, 200))
        debug.error(method, fullUrl, `HTML response: ${htmlPreview.substring(0, 200)}`, elapsed)
        throw new Error('API returned HTML instead of JSON')
      }

      const responseData = await response.json()
      debug.response(method, fullUrl, response.status, responseData, elapsed)
      return { data: responseData }
    } catch (error) {
      const elapsed = performance.now() - startTime
      if (!debug.enabled) {
        console.error(`[API] Error for ${fullUrl}:`, error)
      }
      debug.error(method, fullUrl, error, elapsed)
      throw error
    }
  }

  async get<T>(url: string, config?: { params?: Record<string, string | number | boolean | undefined> }): Promise<{ data: T }> {
    return this.request<T>('GET', url, undefined, config)
  }

  async post<T>(url: string, data?: unknown): Promise<{ data: T }> {
    return this.request<T>('POST', url, data)
  }

  async put<T>(url: string, data?: unknown): Promise<{ data: T }> {
    return this.request<T>('PUT', url, data)
  }

  async patch<T>(url: string, data?: unknown): Promise<{ data: T }> {
    return this.request<T>('PATCH', url, data)
  }

  async delete<T>(url: string): Promise<{ data: T }> {
    return this.request<T>('DELETE', url)
  }
}

const api = new ApiClient()

export default api
