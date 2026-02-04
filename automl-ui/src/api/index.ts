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

export const API_BASE_URL = '/api/v1' // Used for direct API calls (non-Domino)

// Get the app base path from current URL (e.g., /apps/... or /apps-internal/...)
function getAppBasePath(): string {
  const match = window.location.pathname.match(/^(\/apps(?:-internal)?\/[a-z0-9_-]+)/i)
  return match ? match[1] : ''
}

// Map API endpoints to Domino-safe single-segment paths (no 'api' prefix - Domino blocks it)
const ENDPOINT_MAP: Record<string, string> = {
  // Health
  'health': 'svchealth',
  'health/user': 'svcuser',

  // Jobs
  'jobs': 'svcjobs',
  'jobcreate': 'svcjobcreate',
  'jobget': 'svcjobget',
  'jobstatus': 'svcjobstatus',
  'jobmetrics': 'svcjobmetrics',
  'joblogs': 'svcjoblogs',
  'jobcancel': 'svcjobcancel',
  'jobdelete': 'svcjobdelete',
  'jobprogress': 'svcjobprogress',
  'jobregister': 'svcjobregister',

  // Datasets
  'datasets': 'svcdatasets',
  'datasetpreview': 'svcdatasetpreview',
  'upload': 'svcupload',
  'models': 'svcmodels',

  // Predictions
  'predict': 'svcpredict',
  'predictbatch': 'svcpredictbatch',
  'modelinfo': 'svcmodelinfo',
  'featureimportance': 'svcfeatureimportance',
  'leaderboard': 'svcleaderboard',
  'confusionmatrix': 'svcconfusionmatrix',
  'roccurve': 'svcroccurve',
  'precisionrecall': 'svcprecisionrecall',
  'regressiondiagnostics': 'svcregressiondiagnostics',
  'unloadmodel': 'svcunloadmodel',
  'loadedmodels': 'svcloadedmodels',

  // Profiling
  'profile': 'svcprofile',
  'profilequick': 'svcprofilequick',
  'suggesttarget': 'svcsuggesttarget',
  'profilecolumn': 'svcprofilecolumn',
  'metrics': 'svcmetrics',
  'presets': 'svcpresets',

  // Registry
  'registermodel': 'svcregistermodel',
  'registeredmodels': 'svcregisteredmodels',
  'modelversions': 'svcmodelversions',
  'transitionstage': 'svctransitionstage',
  'updatedescription': 'svcupdatedescription',
  'deleteversion': 'svcdeleteversion',
  'deletemodel': 'svcdeletemodel',
  'modelcard': 'svcmodelcard',
  'downloadmodel': 'svcdownloadmodel',

  // Export
  'exportonnx': 'svcexportonnx',
  'exportdeployment': 'svcexportdeployment',
  'learningcurves': 'svclearningcurves',
  'exportformats': 'svcexportformats',
  'exportnotebook': 'svcexportnotebook',

  // Debug
  'ping': 'svcping',

  // Deployments
  'deployments': 'svcdeployments',
  'deploymentcreate': 'svcdeploymentcreate',
  'deploymentget': 'svcdeploymentget',
  'deploymentstart': 'svcdeploymentstart',
  'deploymentstop': 'svcdeploymentstop',
  'deploymentdelete': 'svcdeploymentdelete',
  'deploymentstatus': 'svcdeploymentstatus',
  'deploymentlogs': 'svcdeploymentlogs',
  'quickdeploy': 'svcquickdeploy',
  'deployfromjob': 'svcdeployfromjob',
  'modelapis': 'svcmodelapis',
  'modenapicreate': 'svcmodelapicreate',
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
      // Map to single-segment Domino endpoint
      const mappedPath = ENDPOINT_MAP[cleanEndpoint]
      if (!mappedPath) {
        console.error(`No mapping for endpoint: ${cleanEndpoint}`)
        throw new Error(`Unknown endpoint: ${cleanEndpoint}`)
      }
      const basePath = getAppBasePath()
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
      console.log(`[API] ${method} ${fullUrl}`)
      const response = await fetch(fullUrl, fetchConfig)
      console.log(`[API] Response status: ${response.status}, content-type: ${response.headers.get('content-type')}`)

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
        throw new Error(message)
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
