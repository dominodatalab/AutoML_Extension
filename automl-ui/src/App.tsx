import { useEffect } from 'react'
import { BrowserRouter, Routes, Route, Navigate, useLocation } from 'react-router-dom'
import { ErrorBoundary } from './components/ErrorBoundary'
import Layout from './components/layout/Layout'
import Dashboard from './pages/Dashboard'
import NewJob from './pages/NewJob'
import JobDetail from './pages/JobDetail'
import EDAAnalysis from './pages/EDAAnalysis'

const getBasePath = (): string => {
  // Match both /apps/ and /apps-internal/ paths for Domino
  const appsMatch = window.location.pathname.match(/^(\/apps(?:-internal)?\/[a-z0-9_-]+)/i)
  if (appsMatch) {
    console.log('[AutoML] Detected basename:', appsMatch[1])
    return appsMatch[1]
  }
  const proxyMatch = window.location.pathname.match(/^(\/notebookSession\/[^/]+\/proxy\/\d+)/)
  if (proxyMatch) {
    console.log('[AutoML] Detected basename:', proxyMatch[1])
    return proxyMatch[1]
  }
  console.log('[AutoML] No basename detected')
  return ''
}

// Fallback for unmatched routes
function NoRouteMatch() {
  const location = useLocation()

  useEffect(() => {
    console.error('[AutoML] No route matched:', location.pathname)
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
  console.log('[AutoML] App rendering, basename:', basename || '(empty)')

  return (
    <ErrorBoundary>
      <BrowserRouter basename={basename}>
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
