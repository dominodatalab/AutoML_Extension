import api from './index'
import { Dataset, DatasetPreview, DatasetSchema, FileUploadResponse, SnapshotVerifyResponse } from '../types/dataset'

interface DatasetListResponse {
  datasets: Dataset[]
  total: number
}

interface DatasetListOptions {
  includeFiles?: boolean
}

export async function getDatasets(options: DatasetListOptions = {}): Promise<DatasetListResponse> {
  const response = await api.get<DatasetListResponse>('/datasets', {
    params: {
      include_files: options.includeFiles ?? true,
    },
  })
  return response.data
}

export async function getDataset(datasetId: string): Promise<Dataset | undefined> {
  try {
    const response = await api.get<Dataset>('/dataset', {
      params: { dataset_id: datasetId }
    })
    return response.data
  } catch (error) {
    if ((error as { status?: number }).status === 404) {
      return undefined
    }
    throw error
  }
}

export async function getDatasetPreview(
  filePath: string,
  limit: number = 100,
  offset: number = 0
): Promise<DatasetPreview> {
  // Use POST with file_path in body (no query params in Domino)
  const response = await api.post<DatasetPreview>('/datasetpreview', {
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

export async function verifySnapshot(datasetId: string, filePath: string): Promise<SnapshotVerifyResponse> {
  const response = await api.get<SnapshotVerifyResponse>('/verify-snapshot', {
    params: { dataset_id: datasetId, file_path: filePath }
  })
  return response.data
}
