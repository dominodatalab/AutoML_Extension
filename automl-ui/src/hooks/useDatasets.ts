import { useState, useEffect, useRef, useCallback } from 'react'
import { useQuery, useMutation } from '@tanstack/react-query'
import { getDatasets, getDataset, getDatasetPreview, getDatasetSchema, uploadFile, verifySnapshot } from '../api/datasets'
import { getProjectId } from '../api'
import type { FileUploadResponse } from '../types/dataset'

interface UseDatasetsOptions {
  enabled?: boolean
  includeFiles?: boolean
}

export function useDatasets(options: UseDatasetsOptions = {}) {
  const includeFiles = options.includeFiles ?? true
  const projectId = getProjectId() || ''
  return useQuery({
    queryKey: ['datasets', projectId, includeFiles],
    queryFn: () => getDatasets({ includeFiles }),
    enabled: options.enabled ?? true,
    staleTime: includeFiles ? 60_000 : 30_000,
    gcTime: 5 * 60 * 1000,
  })
}

export function useDataset(datasetId: string) {
  const projectId = getProjectId() || ''
  return useQuery({
    queryKey: ['dataset', projectId, datasetId],
    queryFn: () => getDataset(datasetId),
    enabled: !!datasetId,
    staleTime: 5 * 60 * 1000,
    gcTime: 10 * 60 * 1000,
  })
}

export function useDatasetPreview(filePath: string, limit: number = 100, offset: number = 0) {
  const projectId = getProjectId() || ''
  return useQuery({
    queryKey: ['datasetPreview', projectId, filePath, limit, offset],
    queryFn: () => getDatasetPreview(filePath, limit, offset),
    enabled: !!filePath,
  })
}

export function useDatasetSchema(filePath: string) {
  const projectId = getProjectId() || ''
  return useQuery({
    queryKey: ['datasetSchema', projectId, filePath],
    queryFn: () => getDatasetSchema(filePath),
    enabled: !!filePath,
  })
}

export function useUploadFile() {
  return useMutation({
    mutationFn: (file: File) => uploadFile(file),
  })
}

const VERIFY_INTERVAL_MS = 4000
const VERIFY_MAX_ATTEMPTS = 40

export function useSnapshotVerification(uploadResult: FileUploadResponse | null) {
  const [isVerifying, setIsVerifying] = useState(false)
  const [isVerified, setIsVerified] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const cancelledRef = useRef(false)
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null)

  const cleanup = useCallback(() => {
    cancelledRef.current = true
    if (timerRef.current) {
      clearTimeout(timerRef.current)
      timerRef.current = null
    }
  }, [])

  useEffect(() => {
    cleanup()
    cancelledRef.current = false
    setError(null)

    // No upload, or already verified, or standalone upload (no dataset_id)
    if (!uploadResult || uploadResult.snapshot_verified !== false || !uploadResult.dataset_id) {
      setIsVerifying(false)
      setIsVerified(!!uploadResult)
      return
    }

    // Need to poll
    setIsVerifying(true)
    setIsVerified(false)

    const datasetId = uploadResult.dataset_id
    // Use the relative dataset path for consistent matching with the backend
    const filePath = uploadResult.snapshot_file_path || uploadResult.file_path
    let attempt = 0

    const poll = async () => {
      if (cancelledRef.current) return
      attempt += 1
      try {
        const result = await verifySnapshot(datasetId, filePath)
        if (cancelledRef.current) return
        if (result.verified) {
          setIsVerifying(false)
          setIsVerified(true)
          return
        }
      } catch {
        if (cancelledRef.current) return
      }
      if (attempt >= VERIFY_MAX_ATTEMPTS) {
        setIsVerifying(false)
        setError('Snapshot verification timed out. The file may not be available in Domino Jobs yet.')
        return
      }
      // Schedule next poll only after current one completes
      timerRef.current = setTimeout(poll, VERIFY_INTERVAL_MS)
    }

    // Start first poll after a delay
    timerRef.current = setTimeout(poll, VERIFY_INTERVAL_MS)

    return cleanup
  }, [uploadResult, cleanup])

  return { isVerifying, isVerified, error }
}
