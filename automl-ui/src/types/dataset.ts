export interface DatasetFile {
  name: string
  size: number
  path: string
}

export interface Dataset {
  id: string
  name: string
  path: string
  description?: string
  size_bytes: number
  file_count: number
  files: DatasetFile[]
}

export interface DatasetPreview {
  file_path: string
  columns: string[]
  rows: Record<string, unknown>[]
  total_rows: number
  dtypes?: Record<string, string>
}

export interface DatasetSchema {
  columns: { name: string; dtype: string }[]
  row_count: number
}

export interface FileUploadResponse {
  success: boolean
  file_path: string
  file_name: string
  file_size: number
  columns: string[]
  row_count: number
}
