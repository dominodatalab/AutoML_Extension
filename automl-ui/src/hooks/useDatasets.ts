import { useState, useEffect, useRef, useCallback } from 'react'
import { useQuery, useMutation } from '@tanstack/react-query'
import { getDatasets, getDataset, getDatasetPreview, getDatasetSchema, uploadFile, verifySnapshot } from '../api/datasets'
import type { FileUploadResponse } from '../types/dataset'

export function useDatasets() {
  return useQuery({
    queryKey: ['datasets'],
    queryFn: getDatasets,
  })
}

export function useDataset(datasetId: string) {
  return useQuery({
    queryKey: ['dataset', datasetId],
    queryFn: () => getDataset(datasetId),
    enabled: !!datasetId,
  })
}

export function useDatasetPreview(filePath: string, limit: number = 100, offset: number = 0) {
  return useQuery({
    queryKey: ['datasetPreview', filePath, limit, offset],
    queryFn: () => getDatasetPreview(filePath, limit, offset),
    enabled: !!filePath,
  })
}

export function useDatasetSchema(filePath: string) {
  return useQuery({
    queryKey: ['datasetSchema', filePath],
    queryFn: () => getDatasetSchema(filePath),
    enabled: !!filePath,
  })
}

export function useUploadFile() {
  return useMutation({
    mutationFn: (file: File) => uploadFile(file),
  })
}

const VERIFY_INTERVAL_MS = 3000
const VERIFY_MAX_ATTEMPTS = 20

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
