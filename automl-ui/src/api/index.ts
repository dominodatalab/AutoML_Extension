import { getBasePath } from '../utils/basePath'


/**
 * Read projectId from URL query parameter (?projectId=...).
 * Returns the value when present, undefined otherwise.
 */
export function getProjectIdFromUrl(): string | undefined {
  try {
    const params = new URLSearchParams(window.location.search)
    return params.get('projectId') ?? undefined
  } catch {
    return undefined
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

// Fetch-based API client
class ApiClient {
  private defaultHeaders: Record<string, string>
  private defaultParams: Record<string, string>

  constructor() {
    this.defaultHeaders = {
      'Content-Type': 'application/json',
    }

    this.defaultParams = {}
    const projectId = getProjectIdFromUrl()
    if (projectId) {
      this.defaultParams['projectId'] = projectId
    }
  }

  private async request<T>(
    method: string,
    endpoint: string,
    data?: unknown,
    config?: { params?: Record<string, string | number | boolean | undefined> }
  ): Promise<{ data: T }> {
    const cleanEndpoint = endpoint.startsWith('/') ? endpoint.slice(1) : endpoint

    const basePath = getBasePath()
    let fullUrl = `${basePath}/svc/v1/${cleanEndpoint}`

    // Merge default params (e.g. projectId) with per-call params
    const mergedParams = { ...this.defaultParams, ...(config?.params ?? {}) }
    if (Object.keys(mergedParams).length > 0) {
      const searchParams = new URLSearchParams()
      Object.entries(mergedParams).forEach(([key, value]) => {
        if (value !== undefined) {
          searchParams.append(key, String(value))
        }
      })
      const queryString = searchParams.toString()
      if (queryString) {
        fullUrl += (fullUrl.includes('?') ? '&' : '?') + queryString
      }
    }

    const headers: Record<string, string> = { ...this.defaultHeaders }
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

    try {
      const response = await fetch(fullUrl, fetchConfig)

      if (!response.ok) {
        // Check if response is HTML (common when Domino intercepts)
        const contentType = response.headers.get('content-type') || ''
        if (contentType.includes('text/html')) {
          console.error(`[API] Received HTML response instead of JSON for ${fullUrl}`)
          console.error('[API] This usually means Domino is intercepting the request')
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
        const error = new Error(message)
        ;(error as any).status = response.status
        throw error
      }

      if (response.status === 204) {
        return { data: {} as T }
      }

      // Check content type before parsing JSON
      const contentType = response.headers.get('content-type') || ''
      if (contentType.includes('text/html')) {
        const htmlPreview = await response.text()
        console.error(`[API] Received HTML instead of JSON for ${fullUrl}:`, htmlPreview.substring(0, 200))
        throw new Error('API returned HTML instead of JSON')
      }

      const responseData = await response.json()
      return { data: responseData }
    } catch (error) {
      console.error(`[API] Error for ${fullUrl}:`, error)
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
