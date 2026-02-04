import { useState, useEffect, useMemo } from 'react'
import {
  ChevronLeftIcon,
  ChevronRightIcon,
  ChevronUpIcon,
  ChevronDownIcon,
  FunnelIcon,
  XMarkIcon,
} from '@heroicons/react/24/outline'
import type { ColumnProfile } from '../../types/profiling'
import api from '../../api'
import Spinner from '../common/Spinner'
import Dropdown from '../common/Dropdown'

interface DataTableProps {
  filePath: string
  columns: ColumnProfile[]
}

interface Filter {
  column: string
  operator: 'equals' | 'contains' | 'greater' | 'less' | 'notEmpty'
  value: string
}

interface PreviewData {
  data: Record<string, unknown>[]
  columns: string[]
  total_rows: number
}

export function DataTable({ filePath, columns }: DataTableProps) {
  const [data, setData] = useState<Record<string, unknown>[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [page, setPage] = useState(0)
  const [pageSize] = useState(25)
  const [totalRows, setTotalRows] = useState(0)
  const [sortColumn, setSortColumn] = useState<string | null>(null)
  const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('asc')
  const [filters, setFilters] = useState<Filter[]>([])
  const [showFilterPanel, setShowFilterPanel] = useState(false)
  const [visibleColumns, setVisibleColumns] = useState<string[]>(
    columns.slice(0, 10).map((c) => c.name)
  )

  // Fetch data
  useEffect(() => {
    const fetchData = async () => {
      setLoading(true)
      setError(null)
      try {
        const { data: response } = await api.post<PreviewData>('datasetpreview', {
          file_path: filePath,
          limit: pageSize,
          offset: page * pageSize,
        })
        setData(response.data || [])
        setTotalRows(response.total_rows || 0)
      } catch (err) {
        const message = err instanceof Error ? err.message : 'Failed to load data'
        setError(message)
        setData([])
      } finally {
        setLoading(false)
      }
    }
    fetchData()
  }, [filePath, page, pageSize])

  // Apply client-side sorting and filtering
  const processedData = useMemo(() => {
    let result = [...data]

    // Apply filters
    filters.forEach((filter) => {
      result = result.filter((row) => {
        const value = row[filter.column]
        const strValue = String(value || '').toLowerCase()
        const filterValue = filter.value.toLowerCase()

        switch (filter.operator) {
          case 'equals':
            return strValue === filterValue
          case 'contains':
            return strValue.includes(filterValue)
          case 'greater':
            return Number(value) > Number(filter.value)
          case 'less':
            return Number(value) < Number(filter.value)
          case 'notEmpty':
            return value !== null && value !== undefined && value !== ''
          default:
            return true
        }
      })
    })

    // Apply sorting
    if (sortColumn) {
      result.sort((a, b) => {
        const aVal = a[sortColumn]
        const bVal = b[sortColumn]
        if (aVal === bVal) return 0
        if (aVal === null || aVal === undefined) return 1
        if (bVal === null || bVal === undefined) return -1

        const comparison = aVal < bVal ? -1 : 1
        return sortDirection === 'asc' ? comparison : -comparison
      })
    }

    return result
  }, [data, filters, sortColumn, sortDirection])

  const handleSort = (column: string) => {
    if (sortColumn === column) {
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc')
    } else {
      setSortColumn(column)
      setSortDirection('asc')
    }
  }

  const addFilter = () => {
    setFilters([
      ...filters,
      { column: columns[0]?.name || '', operator: 'contains', value: '' },
    ])
  }

  const updateFilter = (index: number, updates: Partial<Filter>) => {
    setFilters(filters.map((f, i) => (i === index ? { ...f, ...updates } : f)))
  }

  const removeFilter = (index: number) => {
    setFilters(filters.filter((_, i) => i !== index))
  }

  const toggleColumn = (columnName: string) => {
    if (visibleColumns.includes(columnName)) {
      setVisibleColumns(visibleColumns.filter((c) => c !== columnName))
    } else {
      setVisibleColumns([...visibleColumns, columnName])
    }
  }

  const totalPages = Math.ceil(totalRows / pageSize)

  return (
    <div className="space-y-4">
      {/* Toolbar */}
      <div className="flex items-center justify-between gap-4">
        <div className="flex items-center gap-2">
          <button
            onClick={() => setShowFilterPanel(!showFilterPanel)}
            className={`flex items-center gap-2 px-3 py-2 text-sm border rounded transition-colors ${
              showFilterPanel || filters.length > 0
                ? 'border-domino-accent-purple bg-domino-accent-purple/10 text-domino-accent-purple'
                : 'border-domino-border hover:border-domino-text-muted'
            }`}
          >
            <FunnelIcon className="h-4 w-4" />
            Filters
            {filters.length > 0 && (
              <span className="px-1.5 py-0.5 bg-domino-accent-purple text-white text-xs rounded-full">
                {filters.length}
              </span>
            )}
          </button>
        </div>

        {/* Column Visibility Dropdown */}
        <div className="relative group">
          <button className="flex items-center gap-2 px-3 py-2 text-sm border border-domino-border rounded hover:border-domino-text-muted">
            Columns ({visibleColumns.length}/{columns.length})
          </button>
          <div className="absolute right-0 top-full mt-1 w-64 max-h-64 overflow-y-auto bg-white border border-domino-border rounded shadow-lg z-20 hidden group-hover:block">
            <div className="p-2 space-y-1">
              {columns.map((col) => (
                <label
                  key={col.name}
                  className="flex items-center gap-2 px-2 py-1 hover:bg-domino-bg-tertiary rounded cursor-pointer"
                >
                  <input
                    type="checkbox"
                    checked={visibleColumns.includes(col.name)}
                    onChange={() => toggleColumn(col.name)}
                    className="rounded border-domino-border text-domino-accent-purple"
                  />
                  <span className="text-sm text-domino-text-primary truncate">
                    {col.name}
                  </span>
                </label>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Filter Panel */}
      {showFilterPanel && (
        <div className="border border-domino-border bg-domino-bg-tertiary rounded p-4 space-y-3">
          {filters.map((filter, index) => (
            <div key={index} className="flex items-center gap-2">
              <Dropdown
                value={filter.column}
                onChange={(val) => updateFilter(index, { column: val })}
                className="w-[150px]"
                options={columns.map((col) => ({ value: col.name, label: col.name }))}
              />

              <Dropdown
                value={filter.operator}
                onChange={(val) => updateFilter(index, { operator: val as Filter['operator'] })}
                className="w-[140px]"
                options={[
                  { value: 'contains', label: 'contains' },
                  { value: 'equals', label: 'equals' },
                  { value: 'greater', label: 'greater than' },
                  { value: 'less', label: 'less than' },
                  { value: 'notEmpty', label: 'is not empty' },
                ]}
              />

              {filter.operator !== 'notEmpty' && (
                <input
                  type="text"
                  value={filter.value}
                  onChange={(e) => updateFilter(index, { value: e.target.value })}
                  placeholder="Value..."
                  className="flex-1 px-3 py-2 text-sm border border-domino-border rounded focus:outline-none focus:border-domino-accent-purple"
                />
              )}

              <button
                onClick={() => removeFilter(index)}
                className="p-2 text-domino-text-muted hover:text-domino-accent-red"
              >
                <XMarkIcon className="h-4 w-4" />
              </button>
            </div>
          ))}

          <button
            onClick={addFilter}
            className="text-sm text-domino-accent-purple hover:underline"
          >
            + Add Filter
          </button>
        </div>
      )}

      {/* Table */}
      <div className="border border-domino-border rounded overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="bg-domino-bg-tertiary border-b border-domino-border">
                {visibleColumns.map((colName) => (
                  <th
                    key={colName}
                    className="px-4 py-3 text-left text-xs font-medium text-domino-text-secondary uppercase tracking-wide cursor-pointer hover:bg-gray-200 transition-colors"
                    onClick={() => handleSort(colName)}
                  >
                    <div className="flex items-center gap-1">
                      <span className="truncate max-w-[150px]" title={colName}>
                        {colName}
                      </span>
                      <span className="flex flex-col -space-y-1">
                        <ChevronUpIcon className={`h-3 w-3 ${sortColumn === colName && sortDirection === 'asc' ? 'text-domino-accent-purple' : 'text-domino-text-muted'}`} />
                        <ChevronDownIcon className={`h-3 w-3 ${sortColumn === colName && sortDirection === 'desc' ? 'text-domino-accent-purple' : 'text-domino-text-muted'}`} />
                      </span>
                    </div>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {loading ? (
                <tr>
                  <td colSpan={visibleColumns.length} className="px-4 py-8 text-center">
                    <Spinner className="mx-auto" />
                  </td>
                </tr>
              ) : error ? (
                <tr>
                  <td colSpan={visibleColumns.length} className="px-4 py-8 text-center text-domino-accent-red">
                    {error}
                  </td>
                </tr>
              ) : processedData.length === 0 ? (
                <tr>
                  <td colSpan={visibleColumns.length} className="px-4 py-8 text-center text-domino-text-muted">
                    No data matching filters
                  </td>
                </tr>
              ) : (
                processedData.map((row, rowIdx) => (
                  <tr
                    key={rowIdx}
                    className="border-b border-domino-border hover:bg-domino-bg-tertiary transition-colors"
                  >
                    {visibleColumns.map((colName) => (
                      <td
                        key={colName}
                        className="px-4 py-2 text-domino-text-primary truncate max-w-[200px]"
                        title={String(row[colName] ?? '')}
                      >
                        {row[colName] === null || row[colName] === undefined ? (
                          <span className="text-domino-text-muted italic">null</span>
                        ) : (
                          String(row[colName])
                        )}
                      </td>
                    ))}
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Pagination */}
      <div className="flex items-center justify-between">
        <p className="text-sm text-domino-text-muted">
          Showing {page * pageSize + 1} - {Math.min((page + 1) * pageSize, totalRows)} of{' '}
          {totalRows.toLocaleString()} rows
          {filters.length > 0 && ` (${processedData.length} after filters)`}
        </p>
        <div className="flex items-center gap-2">
          <button
            onClick={() => setPage(Math.max(0, page - 1))}
            disabled={page === 0}
            className="p-2 border border-domino-border rounded hover:bg-domino-bg-tertiary disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <ChevronLeftIcon className="h-4 w-4" />
          </button>
          <span className="text-sm text-domino-text-secondary">
            Page {page + 1} of {totalPages}
          </span>
          <button
            onClick={() => setPage(Math.min(totalPages - 1, page + 1))}
            disabled={page >= totalPages - 1}
            className="p-2 border border-domino-border rounded hover:bg-domino-bg-tertiary disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <ChevronRightIcon className="h-4 w-4" />
          </button>
        </div>
      </div>
    </div>
  )
}
