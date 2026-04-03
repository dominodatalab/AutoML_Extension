import { useQuery } from '@tanstack/react-query'
import { getDatasets, getDataset, getDatasetPreview, getDatasetSchema } from '../api/datasets'

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

export function useDatasetPreview(filePath: string, limit: number = 100, offset: number = 0, datasetId: string | undefined = undefined) {
  return useQuery({
    queryKey: ['datasetPreview', filePath, limit, offset],
    queryFn: () => getDatasetPreview(filePath, limit, offset, datasetId),
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
