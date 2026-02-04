import { useEffect, useRef, useState, useCallback } from 'react'
import type { JobProgress, LeaderboardModel } from '../types/job'

interface WebSocketMessage {
  type: 'initial' | 'progress' | 'log' | 'model_trained' | 'completed' | 'error'
  job_id: string
  status?: string
  progress?: number
  current_step?: string
  models_trained?: number
  current_model?: string
  eta_seconds?: number
  metrics?: Record<string, unknown>
  leaderboard?: LeaderboardModel[]
  error_message?: string
  message?: string
  level?: string
  model_name?: string
  score?: number
  fit_time?: number
  rank?: number
  success?: boolean
}

interface LogEntry {
  level: string
  message: string
  timestamp: Date
}

interface TrainedModel {
  name: string
  score: number
  fit_time: number
  rank: number
  trainedAt: Date
}

interface UseJobWebSocketReturn {
  isConnected: boolean
  progress: JobProgress | null
  logs: LogEntry[]
  trainedModels: TrainedModel[]
  error: string | null
  reconnect: () => void
}

// Configuration
const MAX_RECONNECT_ATTEMPTS = 5
const RECONNECT_DELAY_MS = 3000
const PING_INTERVAL_MS = 30000

export function useJobWebSocket(jobId: string | undefined): UseJobWebSocketReturn {
  const [isConnected, setIsConnected] = useState(false)
  const [progress, setProgress] = useState<JobProgress | null>(null)
  const [logs, setLogs] = useState<LogEntry[]>([])
  const [trainedModels, setTrainedModels] = useState<TrainedModel[]>([])
  const [error, setError] = useState<string | null>(null)

  const wsRef = useRef<WebSocket | null>(null)
  const reconnectTimeoutRef = useRef<ReturnType<typeof setTimeout>>()
  const pingIntervalRef = useRef<ReturnType<typeof setInterval>>()
  const reconnectAttemptsRef = useRef(0)
  const isJobActiveRef = useRef(false)

  const getWebSocketUrl = useCallback((id: string): string => {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:'
    const host = window.location.host

    // Handle Domino proxy path
    const proxyMatch = window.location.pathname.match(/^(\/notebookSession\/[^/]+\/proxy\/\d+)/)
    if (proxyMatch) {
      return `${protocol}//${host}${proxyMatch[1]}/ws/jobs/${id}`
    }

    // Handle Domino Apps path
    const appsMatch = window.location.pathname.match(/^(\/apps\/[a-f0-9-]+)/)
    if (appsMatch) {
      return `${protocol}//${host}${appsMatch[1]}/ws/jobs/${id}`
    }

    // Direct connection (development)
    return `${protocol}//${host}/ws/jobs/${id}`
  }, [])

  const connect = useCallback(() => {
    if (!jobId || wsRef.current?.readyState === WebSocket.OPEN) {
      return
    }

    // Check max reconnect attempts
    if (reconnectAttemptsRef.current >= MAX_RECONNECT_ATTEMPTS) {
      setError('Maximum reconnection attempts reached. Please refresh the page.')
      return
    }

    // Clean up existing connection
    if (wsRef.current) {
      wsRef.current.close()
    }

    const url = getWebSocketUrl(jobId)

    try {
      const ws = new WebSocket(url)
      wsRef.current = ws

      ws.onopen = () => {
        setIsConnected(true)
        setError(null)
        reconnectAttemptsRef.current = 0 // Reset on successful connection

        // Start ping interval
        pingIntervalRef.current = setInterval(() => {
          if (ws.readyState === WebSocket.OPEN) {
            ws.send('ping')
          }
        }, PING_INTERVAL_MS)
      }

      ws.onmessage = (event) => {
        try {
          const data: WebSocketMessage = JSON.parse(event.data)

          switch (data.type) {
            case 'initial':
            case 'progress':
              isJobActiveRef.current = data.status === 'running' || data.status === 'pending'
              setProgress({
                id: data.job_id,
                status: (data.status as JobProgress['status']) || 'pending',
                progress: data.progress || 0,
                current_step: data.current_step,
                models_trained: data.models_trained || 0,
                current_model: data.current_model,
                eta_seconds: data.eta_seconds,
              })
              break

            case 'log':
              if (data.message) {
                const logMessage = data.message
                setLogs((prev) => [
                  ...prev.slice(-99), // Keep last 100 logs
                  {
                    level: data.level || 'info',
                    message: logMessage,
                    timestamp: new Date(),
                  },
                ])
              }
              break

            case 'model_trained':
              if (data.model_name) {
                setTrainedModels((prev) => [
                  ...prev,
                  {
                    name: data.model_name!,
                    score: data.score || 0,
                    fit_time: data.fit_time || 0,
                    rank: data.rank || prev.length + 1,
                    trainedAt: new Date(),
                  },
                ])
              }
              break

            case 'completed':
              isJobActiveRef.current = false
              setProgress((prev) => ({
                ...prev!,
                status: data.success ? 'completed' : 'failed',
                progress: 100,
              }))
              if (data.error_message) {
                setError(data.error_message)
              }
              break

            case 'error':
              setError(data.message || 'Unknown error')
              break
          }
        } catch {
          // Ignore pong responses and parse errors for non-JSON data
        }
      }

      ws.onerror = () => {
        setError('WebSocket connection error')
      }

      ws.onclose = () => {
        setIsConnected(false)

        // Clear ping interval
        if (pingIntervalRef.current) {
          clearInterval(pingIntervalRef.current)
        }

        // Attempt to reconnect if job is still running and within retry limit
        if (isJobActiveRef.current && reconnectAttemptsRef.current < MAX_RECONNECT_ATTEMPTS) {
          reconnectAttemptsRef.current++
          reconnectTimeoutRef.current = setTimeout(() => {
            connect()
          }, RECONNECT_DELAY_MS)
        }
      }
    } catch {
      setError('Failed to connect to WebSocket')
    }
  }, [jobId, getWebSocketUrl])

  const reconnect = useCallback(() => {
    // Reset attempts for manual reconnect
    reconnectAttemptsRef.current = 0
    if (reconnectTimeoutRef.current) {
      clearTimeout(reconnectTimeoutRef.current)
    }
    if (wsRef.current) {
      wsRef.current.close()
    }
    setTimeout(connect, 100)
  }, [connect])

  useEffect(() => {
    if (jobId) {
      // Reset state for new job
      reconnectAttemptsRef.current = 0
      isJobActiveRef.current = true
      connect()
    }

    return () => {
      if (reconnectTimeoutRef.current) {
        clearTimeout(reconnectTimeoutRef.current)
      }
      if (pingIntervalRef.current) {
        clearInterval(pingIntervalRef.current)
      }
      if (wsRef.current) {
        wsRef.current.close()
      }
    }
  }, [jobId, connect])

  return {
    isConnected,
    progress,
    logs,
    trainedModels,
    error,
    reconnect,
  }
}

export default useJobWebSocket
