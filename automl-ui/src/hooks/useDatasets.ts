import { useQuery } from '@tanstack/react-query'
import { getDatasets, getDataset, getDatasetPreview, getDatasetSchema } from '../api/datasets'
import { useStore } from '../store'
import { getErrorMessage } from '../utils/errors'

export function useDatasets() {
  const addNotification = useStore((state) => state.addNotification)

  return useQuery({
    queryKey: ['datasets'],
    queryFn: async () => {
      try {
        return await getDatasets()
      } catch (error) {
        addNotification(getErrorMessage(error), 'error')
        throw error
      }
    },
    retry: false,
  })
}

export function useDataset(datasetId: string) {
  const addNotification = useStore((state) => state.addNotification)

  return useQuery({
    queryKey: ['dataset', datasetId],
    queryFn: async () => {
      try {
        return await getDataset(datasetId)
      } catch (error) {
        addNotification(getErrorMessage(error), 'error')
        throw error
      }
    },
    enabled: !!datasetId,
    retry: false,
  })
}

export function useDatasetPreview(filePath: string, limit: number = 100, offset: number = 0, datasetId: string | undefined = undefined) {
  const addNotification = useStore((state) => state.addNotification)

  return useQuery({
    queryKey: ['datasetPreview', filePath, limit, offset],
    queryFn: async () => {
      try {
        return await getDatasetPreview(filePath, limit, offset, datasetId)
      } catch (error) {
        addNotification(getErrorMessage(error), 'error')
        throw error
      }
    },
    enabled: !!filePath,
    retry: false,
  })
}

export function useDatasetSchema(filePath: string) {
  const addNotification = useStore((state) => state.addNotification)

  return useQuery({
    queryKey: ['datasetSchema', filePath],
    queryFn: async () => {
      try {
        return await getDatasetSchema(filePath)
      } catch (error) {
        addNotification(getErrorMessage(error), 'error')
        throw error
      }
    },
    enabled: !!filePath,
    retry: false,
  })
}
