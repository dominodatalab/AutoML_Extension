import { useEffect } from 'react'
import { Outlet } from 'react-router-dom'
import { Toast } from '../common/Toast'

function Layout() {
  // Signal successful render AFTER React has painted the DOM
  useEffect(() => {
    console.log('[AutoML] Layout mounted and visible')
    window.__APP_LOADED__ = true
    if (window.__APP_LOAD_TIMEOUT__) {
      clearTimeout(window.__APP_LOAD_TIMEOUT__)
    }
  }, [])

  return (
    <div className="min-h-screen bg-domino-bg-secondary font-sans">
      <main className="px-10 py-8">
        <Outlet />
      </main>
      <Toast />
    </div>
  )
}

export default Layout
