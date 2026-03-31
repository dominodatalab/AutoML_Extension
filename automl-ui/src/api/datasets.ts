import api from './index'
import { Dataset, DatasetPreview, DatasetSchema, FileUploadResponse } from '../types/dataset'

interface DatasetListResponse {
  datasets: Dataset[]
  total: number
}

export async function getDatasets(): Promise<DatasetListResponse> {
  const response = await api.get<DatasetListResponse>('datasets')
  return response.data
}

export async function getDataset(datasetId: string): Promise<Dataset | undefined> {
  const { datasets } = await getDatasets()
  return datasets.find(d => d.id === datasetId)
}

export async function getDatasetFiles(datasetId: string): Promise<Dataset | undefined> {
  const response = await api.get<DatasetListResponse>(`datasets/${encodeURIComponent(datasetId)}/files`)
  return response.data.datasets[0]
}

export async function getDatasetPreview(
  filePath: string,
  limit: number = 100,
  offset: number = 0,
  datasetId: string | undefined = undefined,
): Promise<DatasetPreview> {
  const response = await api.post<DatasetPreview>('datasets/preview', {
    dataset_id: datasetId,
    file_path: filePath,
    limit,
    offset
  })
  return response.data
}

export async function getDatasetSchema(filePath: string): Promise<DatasetSchema> {
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
  const response = await api.post<FileUploadResponse>('datasets/upload', formData)
  return response.data
}
