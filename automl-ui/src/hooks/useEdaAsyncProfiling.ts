import { useCallback, useEffect, useState } from 'react'
import type {
  AsyncProfileStartRequest,
  AsyncProfileStartResponse,
  AsyncProfileStatusResponse,
  DataProfile,
  TimeSeriesProfile,
} from '../types/profiling'
import { useSearchParams } from 'react-router-dom'

type AsyncStatus = 'idle' | 'starting' | 'pending' | 'running' | 'completed' | 'failed'
type ExecutionTarget = 'local' | 'domino_job'

interface UseEdaAsyncProfilingParams {
  edaExecutionTarget: ExecutionTarget
  startAsyncProfile: (request: AsyncProfileStartRequest) => Promise<AsyncProfileStartResponse>
  getAsyncProfileStatus: (requestId: string) => Promise<AsyncProfileStatusResponse>
  setProfileData: (value: DataProfile | null) => void
  setTsProfileData: (value: TimeSeriesProfile | null) => void
  addNotification: (message: string, type: 'success' | 'error' | 'info') => void
}

interface UseEdaAsyncProfilingResult {
  asyncRequestId: string | null
  asyncDominoJobId: string | null
  asyncProfileStatus: AsyncStatus
  asyncProfileError: string | null
  resetAsyncState: () => void
  startAsyncTabularProfiling: (
    filePath: string,
    sampleSize: number,
    samplingStrategy: string,
    stratifyColumn?: string,
    forceRestart?: boolean,
  ) => Promise<void>
  startAsyncTimeSeriesProfiling: (
    filePath: string,
    timeColumn: string,
    targetColumn: string,
    idColumn: string,
    sampleSize: number,
    samplingStrategy: string,
    rollingWindow: string,
    forceRestart?: boolean,
  ) => Promise<void>
}

export function useEdaAsyncProfiling({
  edaExecutionTarget,
  startAsyncProfile,
  getAsyncProfileStatus,
  setProfileData,
  setTsProfileData,
  addNotification,
}: UseEdaAsyncProfilingParams): UseEdaAsyncProfilingResult {
  const [searchParams] = useSearchParams()
  const [asyncRequestId, setAsyncRequestId] = useState<string | null>(null)
  const [asyncDominoJobId, setAsyncDominoJobId] = useState<string | null>(null)
  const [asyncProfileStatus, setAsyncProfileStatus] = useState<AsyncStatus>('idle')
  const [asyncProfileError, setAsyncProfileError] = useState<string | null>(null)

  const resetAsyncState = useCallback(() => {
    setAsyncRequestId(null)
    setAsyncDominoJobId(null)
    setAsyncProfileStatus('idle')
    setAsyncProfileError(null)
  }, [])

  const startAsyncTabularProfiling = useCallback(async (
    filePath: string,
    sampleSize: number,
    samplingStrategy: string,
    stratifyColumn?: string,
    forceRestart?: boolean,
  ) => {
    setAsyncProfileStatus('starting')
    setAsyncProfileError(null)
    setAsyncRequestId(null)
    try {
      const jobId = searchParams.get('job_id');
      const datasetId = searchParams.get('dataset_id');
      if (!jobId) {
        throw new Error("job_id must exist in query parameters in order to start async tabular profiling")
      }
      if (!datasetId) {
        throw new Error("dataset_id must exist in query parameters in order to start async tabular profiling")
      }

      const response = await startAsyncProfile({
        job_id: jobId,
        force_restart: forceRestart,
        mode: 'tabular',
        dataset_id: datasetId,
        file_path: filePath,
        sample_size: sampleSize,
        sampling_strategy: samplingStrategy,
        stratify_column: stratifyColumn || undefined,
      })
      setAsyncRequestId(response.request_id)
      setAsyncDominoJobId(response.domino_job_id || null)
      setAsyncProfileStatus(response.status === 'pending' ? 'pending' : 'running')
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Failed to start async EDA profiling'
      setAsyncProfileError(message)
      setAsyncProfileStatus('failed')
      addNotification(message, 'error')
    }
  }, [addNotification, startAsyncProfile])

  const startAsyncTimeSeriesProfiling = useCallback(async (
    filePath: string,
    timeColumn: string,
    targetColumn: string,
    idColumn: string,
    sampleSize: number,
    samplingStrategy: string,
    rollingWindow: string,
    forceRestart?: boolean,
  ) => {
    setAsyncProfileStatus('starting')
    setAsyncProfileError(null)
    setAsyncRequestId(null)
    try {
      const jobId = searchParams.get('job_id');
      const datasetId = searchParams.get('dataset_id');
      if (!jobId) {
        throw new Error("job_id must exist in query parameters in order to start async timeseries profiling")
      }
      if (!datasetId) {
        throw new Error("dataset_id must exist in query parameters in order to start async timeseries profiling")
      }
      const response = await startAsyncProfile({
        job_id: jobId,
        force_restart: forceRestart,
        mode: 'timeseries',
        dataset_id: datasetId,
        file_path: filePath,
        time_column: timeColumn,
        target_column: targetColumn,
        id_column: idColumn || undefined,
        sample_size: sampleSize,
        sampling_strategy: samplingStrategy,
        rolling_window: Number(rollingWindow) || undefined,
      })
      setAsyncRequestId(response.request_id)
      setAsyncDominoJobId(response.domino_job_id || null)
      setAsyncProfileStatus(response.status === 'pending' ? 'pending' : 'running')
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Failed to start async time series profiling'
      setAsyncProfileError(message)
      setAsyncProfileStatus('failed')
      addNotification(message, 'error')
    }
  }, [addNotification, startAsyncProfile])

  useEffect(() => {
    if (!asyncRequestId || edaExecutionTarget !== 'domino_job') return

    let mounted = true
    let intervalId: number | null = null

    const pollStatus = async () => {
      try {
        const status = await getAsyncProfileStatus(asyncRequestId)
        if (!mounted) return

        setAsyncDominoJobId(status.domino_job_id || asyncDominoJobId)

        if (status.status === 'completed') {
          if (status.mode === 'timeseries' && status.result) {
            setTsProfileData(status.result as TimeSeriesProfile)
          } else if (status.result) {
            setProfileData(status.result as DataProfile)
          }
          setAsyncProfileStatus('completed')
          setAsyncProfileError(null)
          if (intervalId !== null) window.clearInterval(intervalId)
          return
        }

        if (status.status === 'failed') {
          const message = status.error || 'Async profiling failed'
          setAsyncProfileStatus('failed')
          setAsyncProfileError(message)
          addNotification(message, 'error')
          if (intervalId !== null) window.clearInterval(intervalId)
          return
        }

        setAsyncProfileStatus(status.status === 'pending' ? 'pending' : 'running')
      } catch (error) {
        if (!mounted) return
        const message = error instanceof Error ? error.message : 'Failed to poll async profiling status'
        setAsyncProfileStatus('failed')
        setAsyncProfileError(message)
        addNotification(message, 'error')
        if (intervalId !== null) window.clearInterval(intervalId)
      }
    }

    void pollStatus()
    intervalId = window.setInterval(() => {
      void pollStatus()
    }, 4000)

    return () => {
      mounted = false
      if (intervalId !== null) window.clearInterval(intervalId)
    }
  }, [addNotification, asyncDominoJobId, asyncRequestId, edaExecutionTarget, getAsyncProfileStatus, setProfileData, setTsProfileData])

  return {
    asyncRequestId,
    asyncDominoJobId,
    asyncProfileStatus,
    asyncProfileError,
    resetAsyncState,
    startAsyncTabularProfiling,
    startAsyncTimeSeriesProfiling,
  }
}
