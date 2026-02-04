import ReactDOM from 'react-dom/client'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import App from './App'
import './styles/globals.css'

console.log('[AutoML] index.tsx executing')
console.log('[AutoML] Pathname:', window.location.pathname)

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 5000,
      refetchOnWindowFocus: false,
    },
  },
})

ReactDOM.createRoot(document.getElementById('root')!).render(
  <QueryClientProvider client={queryClient}>
    <App />
  </QueryClientProvider>,
)

// NOTE: __APP_LOADED__ is now set in Layout.tsx useEffect
console.log('[AutoML] React render() called, waiting for Layout mount...')
