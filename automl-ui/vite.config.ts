import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '')

  // Use relative base path for Domino apps - this ensures assets work behind Domino's proxy
  // For production builds, use './' to generate relative asset paths
  const basePath = mode === 'production' ? './' : (env.VITE_BASE_PATH || '/')

  // API target - defaults to localhost for local dev, use VITE_API_URL for Domino
  const apiTarget = env.VITE_API_URL || 'http://localhost:8000'

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
    },
  }
})
