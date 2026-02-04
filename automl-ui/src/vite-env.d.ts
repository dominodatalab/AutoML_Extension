/// <reference types="vite/client" />

// Asset module declarations
declare module '*.png' {
  const src: string
  export default src
}

declare module '*.svg' {
  const src: string
  export default src
}

interface ImportMetaEnv {
  /** Base path for the application (for Domino proxy support) */
  readonly VITE_BASE_PATH: string
  /** API URL for the FastAPI backend */
  readonly VITE_API_URL: string
  /** Model API URL (optional, for external model endpoints) */
  readonly VITE_MODEL_API_URL?: string
  /** Model API authentication token (optional) */
  readonly VITE_MODEL_API_TOKEN?: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}

declare global {
  interface Window {
    __APP_LOADED__?: boolean
    __APP_LOAD_TIMEOUT__?: ReturnType<typeof setTimeout>
  }
}

export {}
