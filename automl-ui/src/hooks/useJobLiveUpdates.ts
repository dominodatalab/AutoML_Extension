import { useEffect, useMemo, useRef, useState } from 'react'
import { getBasePath } from '../utils/basePath'

type LiveJobStatus = 'pending' | 'running' | 'completed' | 'failed' | 'cancelled'

export interface JobLiveUpdate {
  status?: LiveJobStatus
  progress?: number
  current_step?: string | null
  models_trained?: number
  current_model?: string | null
  eta_seconds?: number | null
  domino_job_status?: string | null
  started_at?: string | null
  completed_at?: string | null
  log?: {
    id: number
    job_id: string
    level: string
    message: string
    timestamp: string | null
  }
}

interface UseJobLiveUpdatesOptions {
  enabled?: boolean
  onTerminal?: () => void
}

function buildWebSocketUrl(jobId: string): string {
  const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:'
  const basePath = getBasePath()
  return `${protocol}//${window.location.host}${basePath}/ws/jobs/${jobId}`
}

export function useJobLiveUpdates(
  jobId: string | undefined,
  options: UseJobLiveUpdatesOptions = {},
) {
  const { enabled = true, onTerminal } = options
  const [liveUpdate, setLiveUpdate] = useState<JobLiveUpdate | null>(null)
  const [isConnected, setIsConnected] = useState(false)
  const terminalHandledRef = useRef(false)
  const onTerminalRef = useRef(onTerminal)
  onTerminalRef.current = onTerminal

  const wsUrl = useMemo(() => {
    if (!jobId) return null
    return buildWebSocketUrl(jobId)
  }, [jobId])

  useEffect(() => {
    setLiveUpdate(null)
    setIsConnected(false)
    terminalHandledRef.current = false
  }, [jobId])

  useEffect(() => {
    if (!wsUrl || !enabled) {
      return
    }

    let socket: WebSocket | null = new WebSocket(wsUrl)
    let retryTimer: ReturnType<typeof setTimeout> | null = null
    let closedByHook = false

    const cleanupSocket = () => {
      if (retryTimer) {
        clearTimeout(retryTimer)
        retryTimer = null
      }
      if (socket) {
        socket.close()
        socket = null
      }
    }

    const scheduleRetry = () => {
      if (closedByHook) {
        return
      }
      retryTimer = setTimeout(() => {
        socket = new WebSocket(wsUrl)
        attachHandlers()
      }, 3000)
    }

    const attachHandlers = () => {
      if (!socket) {
        return
      }

      socket.onopen = () => {
        setIsConnected(true)
      }

      socket.onmessage = (event) => {
        try {
          const message = JSON.parse(event.data) as JobLiveUpdate & { type?: string }
          setLiveUpdate((prev) => ({ ...prev, ...message }))
          if (
            message.status &&
            ['completed', 'failed', 'cancelled'].includes(message.status) &&
            !terminalHandledRef.current
          ) {
            terminalHandledRef.current = true
            onTerminalRef.current?.()
          }
        } catch (error) {
          console.error('Failed to parse job websocket message:', error)
        }
      }

      socket.onclose = () => {
        setIsConnected(false)
        scheduleRetry()
      }

      socket.onerror = () => {
        setIsConnected(false)
      }
    }

    attachHandlers()

    return () => {
      closedByHook = true
      cleanupSocket()
    }
  }, [enabled, wsUrl])

  return { liveUpdate, isConnected }
}
