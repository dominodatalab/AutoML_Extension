import { Suspense, lazy, useEffect } from 'react'
import { BrowserRouter, Routes, Route, Navigate, useLocation } from 'react-router-dom'
import { ErrorBoundary } from './components/ErrorBoundary'
import Layout from './components/layout/Layout'
import Spinner from './components/common/Spinner'
import { getBasePath } from './utils/basePath'
import { getProjectIdFromUrl, setProjectId } from './api'

const Dashboard = lazy(() => import('./pages/Dashboard'))
const NewJob = lazy(() => import('./pages/NewJob'))
const JobDetail = lazy(() => import('./pages/JobDetail'))
const EDAAnalysis = lazy(() => import('./pages/EDAAnalysis'))

/**
 * Sync projectId/project_id from both query string and hash fragment into the API
 * client so the X-Project-Id header is sent on every request.
 * Domino's app proxy strips query params, so #projectId=... is the
 * reliable transport.
 */
function ProjectIdSync() {
  const location = useLocation()
  useEffect(() => {
    const projectId = getProjectIdFromUrl()
    if (projectId) {
      setProjectId(projectId)
    }
  }, [location])
  return null
}

// Fallback for unmatched routes
function NoRouteMatch() {
  const location = useLocation()

  useEffect(() => {
    window.__APP_LOADED__ = true
    if (window.__APP_LOAD_TIMEOUT__) {
      clearTimeout(window.__APP_LOAD_TIMEOUT__)
    }
  }, [location])

  return (
    <div style={{ padding: '40px', fontFamily: 'system-ui', maxWidth: '600px', margin: '40px auto' }}>
      <h1 style={{ color: '#dc2626', marginBottom: '16px' }}>Route Not Found</h1>
      <p><strong>Path:</strong> {location.pathname}</p>
      <p style={{ color: '#6b7280', fontSize: '14px' }}>Full URL: {window.location.href}</p>
      <button
        onClick={() => window.location.href = window.location.origin + getBasePath() + '/dashboard'}
        style={{ marginTop: '16px', padding: '8px 16px', background: '#3b82f6', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
      >
        Go to Dashboard
      </button>
    </div>
  )
}

function App() {
  const basename = getBasePath()

  return (
    <ErrorBoundary>
      <BrowserRouter basename={basename}>
        <ProjectIdSync />
        <Suspense fallback={<RouteLoadingFallback />}>
          <Routes>
            <Route path="/" element={<Layout />}>
              <Route index element={<Navigate to="/dashboard" replace />} />
              <Route path="dashboard" element={<Dashboard />} />
              <Route path="eda" element={<EDAAnalysis />} />
              <Route path="jobs/new" element={<NewJob />} />
              <Route path="jobs/:jobId" element={<JobDetail />} />
            </Route>
            <Route path="*" element={<NoRouteMatch />} />
          </Routes>
        </Suspense>
      </BrowserRouter>
    </ErrorBoundary>
  )
}

function RouteLoadingFallback() {
  return (
    <div className="flex items-center justify-center min-h-[60vh]">
      <Spinner size="lg" />
    </div>
  )
}

export default App
