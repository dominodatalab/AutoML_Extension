import { useEffect } from 'react'
import { BrowserRouter, Routes, Route, Navigate, useLocation, useSearchParams } from 'react-router-dom'
import { ErrorBoundary } from './components/ErrorBoundary'
import Layout from './components/layout/Layout'
import Dashboard from './pages/Dashboard'
import NewJob from './pages/NewJob'
import JobDetail from './pages/JobDetail'
import EDAAnalysis from './pages/EDAAnalysis'
import { getBasePath } from './utils/basePath'
import { setProjectId } from './api'

/**
 * Sync ?projectId= from the URL into the API client so the X-Project-Id
 * header is sent on every request. Runs inside BrowserRouter so it has
 * access to React Router's search params.
 */
function ProjectIdSync() {
  const [searchParams] = useSearchParams()
  useEffect(() => {
    const id = searchParams.get('projectId')
    if (id) setProjectId(id)
  }, [searchParams])
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
      </BrowserRouter>
    </ErrorBoundary>
  )
}

export default App
