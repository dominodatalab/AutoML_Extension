import api, { getProjectIdFromUrl } from './index'
import { Dataset, DatasetPreview, DatasetSchema, FileUploadResponse } from '../types/dataset'

interface DatasetListResponse {
  datasets: Dataset[]
  total: number
}

export async function getDatasets(): Promise<DatasetListResponse> {
  const allParams = window.location.search
  const response = await api.get<DatasetListResponse>(`/datasets${allParams}`)
  return response.data
}

export async function getDataset(datasetId: string): Promise<Dataset | undefined> {
  // Datasets are listed from mounted paths, find by id
  const { datasets } = await getDatasets()
  return datasets.find(d => d.id === datasetId)
}

export async function getDatasetFiles(datasetId: string): Promise<Dataset | undefined> {
  const projectId = getProjectIdFromUrl()
  const response = await api.get<DatasetListResponse>(`/svcdataset/${encodeURIComponent(datasetId)}/files`, {
    params: { projectId }
  })
  return response.data.datasets[0]
}

export async function getDatasetPreview(
  filePath: string,
  limit: number = 100,
  offset: number = 0,
  datasetId: string | undefined = undefined,
): Promise<DatasetPreview> {
  // Use POST with file_path in body (no query params in Domino)
  const response = await api.post<DatasetPreview>('/datasetpreview', {
    dataset_id: datasetId,
    file_path: filePath,
    limit,
    offset
  })
  return response.data
}

export async function getDatasetSchema(filePath: string): Promise<DatasetSchema> {
  // Get schema by previewing with 1 row
  const preview = await getDatasetPreview(filePath, 1)
  return {
    columns: Object.entries(preview.dtypes || {}).map(([name, dtype]) => ({
      name,
      dtype: dtype as string
    })),
    row_count: preview.total_rows
  }
}

export async function uploadFile(file: File): Promise<FileUploadResponse> {
  const formData = new FormData()
  formData.append('file', file)
  const response = await api.post<FileUploadResponse>('/upload', formData)
  return response.data
}
