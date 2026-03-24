import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '')

  const isProduction = mode === 'production';

  // Use relative base path for Domino apps - this ensures assets work behind Domino's proxy
  // For production builds, use './' to generate relative asset paths
  const basePath = isProduction ? './' : (env.VITE_BASE_PATH || '/')

  // API target - defaults to localhost for local dev, use VITE_API_URL for Domino
  const apiTarget = env.VITE_API_URL || 'http://localhost:8000'

  // JWT to allow authing API requests sent to DOMINO_API_HOST
  const devAuthToken = env.DEV_ACCESS_TOKEN;

  return {
    plugins: [react()],
    base: basePath,
    resolve: {
      alias: {
        '@': path.resolve(__dirname, './src'),
      },
    },
    server: {
      port: 3000,
      host: '0.0.0.0', // Allow external connections in Domino workspace
      proxy: {
        '/api': {
          target: apiTarget,
          changeOrigin: true,
          secure: false,
          headers: {
            'Authorization': `Bearer ${devAuthToken}`
          }
        },
        '/svc': {
          target: apiTarget,
          changeOrigin: true,
          secure: false,
          headers: {
            'Authorization': `Bearer ${devAuthToken}`
          }
        },
      },
    },
    preview: {
      port: 3000,
      host: '0.0.0.0',
    },
    build: {
      outDir: 'dist',
      assetsDir: 'assets',
      // Generate relative paths for assets
      rollupOptions: {
        output: {
          manualChunks: undefined,
        },
      },
    },
    // Expose env variables to the client
    define: {
      'import.meta.env.VITE_API_URL': JSON.stringify(apiTarget),
      'import.meta.env.VITE_BASE_PATH': JSON.stringify(basePath),
      'import.meta.env.VITE_DEV_DOMINO_API_HOST': JSON.stringify(!isProduction ? env.DOMINO_API_HOST || '' : '')
    },
  }
})
