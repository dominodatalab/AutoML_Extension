import { useState } from 'react'
import {
  DocumentIcon,
  ArrowDownTrayIcon,
  ArrowPathIcon,
  ExclamationTriangleIcon,
} from '@heroicons/react/24/outline'
import clsx from 'clsx'
import Spinner from '../common/Spinner'
import Dropdown from '../common/Dropdown'
import { ColumnExplorer } from './ColumnExplorer'
import { CorrelationMatrix } from './CorrelationMatrix'
import { MissingValuesChart } from './MissingValuesChart'
import { DataQualityPanel } from './DataQualityPanel'
import { TimeSeriesOverview } from './TimeSeriesOverview'
import { StationarityTrendPanel } from './StationarityTrendPanel'
import { ACFPanel } from './ACFPanel'
import type { TransformConfig } from '../../types/eda'
import type { DataProfile, TimeSeriesProfile } from '../../types/profiling'
import { formatCompactNumber } from '../../utils/formatters'

type EDATab = 'data' | 'columns' | 'correlations' | 'quality' | 'transforms' | 'ts-overview' | 'ts-stationarity' | 'ts-acf'

function TabContent({ loading, error, data, emptyMessage, children }: {
  loading: boolean
  error: string | null
  data: unknown
  emptyMessage?: string
  children: React.ReactNode
}) {
  if (loading) return <div className="flex items-center justify-center py-20"><Spinner /></div>
  if (error) return <div className="text-center py-20 text-domino-accent-red">{error}</div>
  if (!data && emptyMessage) return <div className="text-center py-20 text-domino-text-muted">{emptyMessage}</div>
  if (!data) return null
  return <>{children}</>
}

interface ProfiledDataViewProps {
  selectedFilePath: string
  selectedFileName: string
  preview: { columns?: string[]; rows?: Record<string, unknown>[]; total_rows?: number } | undefined
  previewLoading: boolean
  previewError: unknown
  profile: DataProfile | null
  profilingLoading: boolean
  profilingError: string | null
  transforms: TransformConfig[]
  isExporting: boolean
  currentPage: number
  pageSize: number
  samplingStrategy: string
  sampleSize: number
  stratifyColumn: string
  onChangeFile: () => void
  onExportNotebook: () => void
  onAddTransform: (transform: TransformConfig) => void
  onRemoveTransform: (index: number) => void
  onPageChange: (page: number) => void
  onPageSizeChange: (size: number) => void
  onReanalyze: (strategy: string, size: number, stratifyCol: string) => void
  edaMode?: 'tabular' | 'timeseries'
  tsProfile?: TimeSeriesProfile | null
  tsLoading?: boolean
  tsError?: string | null
}


export function ProfiledDataView({
  selectedFilePath,
  selectedFileName,
  preview,
  previewLoading,
  previewError,
  profile,
  profilingLoading,
  profilingError,
  transforms,
  isExporting,
  currentPage,
  pageSize,
  samplingStrategy,
  sampleSize,
  stratifyColumn,
  onChangeFile,
  onExportNotebook,
  onAddTransform,
  onRemoveTransform,
  onPageChange,
  onPageSizeChange,
  onReanalyze,
  edaMode = 'tabular',
  tsProfile,
  tsLoading,
  tsError,
}: ProfiledDataViewProps) {
  const [activeTab, setActiveTab] = useState<EDATab>('data')
  const [localStrategy, setLocalStrategy] = useState(samplingStrategy)
  const [localSampleSize, setLocalSampleSize] = useState(String(sampleSize))
  const [localStratifyCol, setLocalStratifyCol] = useState(stratifyColumn)

  const tabularTabs = [
    { id: 'data' as const, label: 'Data Preview' },
    { id: 'columns' as const, label: 'Column Analysis' },
    { id: 'correlations' as const, label: 'Correlations' },
    { id: 'quality' as const, label: 'Data Quality' },
    { id: 'transforms' as const, label: 'Transformations' },
  ]

  const tsTabs: { id: EDATab; label: string }[] = [
    { id: 'data' as const, label: 'Data Preview' },
    { id: 'ts-overview' as const, label: 'Temporal Overview' },
    { id: 'ts-stationarity' as const, label: 'Stationarity & Trends' },
    { id: 'ts-acf' as const, label: 'Seasonality & ACF' },
    { id: 'columns' as const, label: 'Column Analysis' },
    { id: 'quality' as const, label: 'Data Quality' },
  ]

  const tabs = edaMode === 'timeseries' ? tsTabs : tabularTabs

  const isSampled = profile?.summary && profile.summary.total_rows > profile.summary.sample_size

  return (
    <>
      {/* Page Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-normal text-domino-text-primary">Data Exploration</h1>
          <p className="text-sm text-domino-text-secondary mt-1">
            Analyze data quality, distributions, and prepare transformations
          </p>
        </div>
        {profile && (
          <button
            onClick={onExportNotebook}
            disabled={isExporting}
            className="h-[32px] px-[15px] bg-domino-accent-purple text-white text-sm font-normal rounded-[2px] hover:bg-domino-accent-purple-hover transition-all duration-200 inline-flex items-center gap-2 disabled:opacity-50"
          >
            {isExporting ? (
              <ArrowPathIcon className="h-4 w-4 animate-spin" />
            ) : (
              <ArrowDownTrayIcon className="h-4 w-4" />
            )}
            Export Notebook
          </button>
        )}
      </div>

      {/* Selected File Info */}
      <div className="bg-domino-accent-purple/5 border border-domino-accent-purple p-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <DocumentIcon className="h-6 w-6 text-domino-accent-purple" />
          <div>
            <p className="font-medium text-domino-text-primary">{selectedFileName}</p>
            {preview && (
              <p className="text-sm text-domino-text-secondary">
                {preview.columns?.length || 0} columns, {preview.total_rows?.toLocaleString() || 0} rows
              </p>
            )}
          </div>
        </div>
        <button
          onClick={onChangeFile}
          className="text-sm text-domino-accent-purple hover:underline"
        >
          Change File
        </button>
      </div>

      {/* Sampling Config Bar */}
      {isSampled && edaMode === 'tabular' && (
        <div className="bg-amber-50 border border-amber-200 p-4">
          <div className="flex items-center gap-4 flex-wrap">
            <span className="text-sm text-amber-800 font-medium">
              Sampled {profile!.summary.sample_size.toLocaleString()} of {profile!.summary.total_rows.toLocaleString()} rows
            </span>
            <div className="flex items-center gap-2">
              <label className="text-xs text-domino-text-secondary">Strategy:</label>
              <select
                value={localStrategy}
                onChange={(e) => setLocalStrategy(e.target.value)}
                className="h-[28px] px-2 text-xs border border-domino-border rounded-[2px] bg-white"
              >
                <option value="random">Random</option>
                <option value="stratified">Stratified</option>
                <option value="head">First N</option>
                <option value="full">Full Dataset</option>
              </select>
            </div>
            <div className="flex items-center gap-2">
              <label className="text-xs text-domino-text-secondary">Sample size:</label>
              <input
                type="number"
                value={localSampleSize}
                onChange={(e) => setLocalSampleSize(e.target.value)}
                className="h-[28px] w-[100px] px-2 text-xs border border-domino-border rounded-[2px]"
                disabled={localStrategy === 'full'}
              />
            </div>
            {localStrategy === 'stratified' && profile?.columns && (
              <div className="flex items-center gap-2">
                <label className="text-xs text-domino-text-secondary">Stratify by:</label>
                <select
                  value={localStratifyCol}
                  onChange={(e) => setLocalStratifyCol(e.target.value)}
                  className="h-[28px] px-2 text-xs border border-domino-border rounded-[2px] bg-white"
                >
                  <option value="">Select column...</option>
                  {profile.columns.map((col) => (
                    <option key={col.name} value={col.name}>{col.name}</option>
                  ))}
                </select>
              </div>
            )}
            <button
              onClick={() => onReanalyze(localStrategy, Number(localSampleSize) || 50000, localStratifyCol)}
              className="h-[28px] px-3 text-xs bg-domino-accent-purple text-white rounded-[2px] hover:bg-domino-accent-purple-hover"
            >
              Re-analyze
            </button>
            {localStrategy === 'full' && profile!.summary.total_rows > 500000 && (
              <span className="flex items-center gap-1 text-xs text-amber-700">
                <ExclamationTriangleIcon className="h-3.5 w-3.5" />
                Large dataset — analysis may take longer
              </span>
            )}
          </div>
        </div>
      )}

      {/* EDA Tabs */}
      <div className="border-b border-domino-border">
        <nav className="flex">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={clsx(
                'px-6 py-3 text-sm border-b-2 -mb-px transition-colors',
                activeTab === tab.id
                  ? 'border-domino-accent-purple text-domino-accent-purple font-medium'
                  : 'border-transparent text-domino-text-secondary hover:text-domino-text-primary'
              )}
            >
              {tab.label}
            </button>
          ))}
        </nav>
      </div>

      {/* Tab Content */}
      <div className="bg-white border border-domino-border p-6">
        {activeTab === 'data' && (
          <TabContent loading={previewLoading} error={previewError ? String(previewError) : null} data={preview} emptyMessage="Select an execution target and click Analyze to preview your data">
            {preview && (
              <DataPreviewContent
                preview={preview}
                previewLoading={false}
                previewError={null}
                currentPage={currentPage}
                pageSize={pageSize}
                onPageChange={onPageChange}
                onPageSizeChange={onPageSizeChange}
              />
            )}
          </TabContent>
        )}

        {activeTab === 'columns' && (
          <TabContent loading={profilingLoading} error={profilingError} data={profile} emptyMessage="Select an execution target and click Analyze to profile your data">
            {profile && <ColumnExplorer columns={profile.columns} filePath={selectedFilePath} />}
          </TabContent>
        )}

        {activeTab === 'correlations' && (
          <TabContent loading={profilingLoading} error={profilingError} data={profile?.correlations} emptyMessage="Select an execution target and click Analyze to view correlations">
            {profile?.correlations && <CorrelationMatrix correlations={profile.correlations} columns={profile.columns} />}
          </TabContent>
        )}

        {activeTab === 'quality' && (
          <TabContent loading={profilingLoading} error={profilingError} data={profile} emptyMessage="Select an execution target and click Analyze to assess data quality">
            {profile && (
              <div className="space-y-6">
                <MissingValuesChart columns={profile.columns} />
                <DataQualityPanel warnings={profile.warnings} recommendations={profile.recommendations} columns={profile.columns} />
              </div>
            )}
          </TabContent>
        )}

        {activeTab === 'transforms' && (
          <TabContent loading={profilingLoading} error={profilingError} data={profile} emptyMessage="Select an execution target and click Analyze before applying transforms">
            {profile && (
              <TransformsContent
                profile={profile}
                transforms={transforms}
                onAddTransform={onAddTransform}
                onRemoveTransform={onRemoveTransform}
              />
            )}
          </TabContent>
        )}

        {activeTab === 'ts-overview' && (
          <TabContent loading={!!tsLoading} error={tsError ?? null} data={tsProfile} emptyMessage="Configure time series columns and run analysis to see temporal overview">
            {tsProfile && <TimeSeriesOverview profile={tsProfile} />}
          </TabContent>
        )}

        {activeTab === 'ts-stationarity' && (
          <TabContent loading={!!tsLoading} error={tsError ?? null} data={tsProfile} emptyMessage="Configure time series columns and run analysis to see stationarity results">
            {tsProfile && <StationarityTrendPanel profile={tsProfile} />}
          </TabContent>
        )}

        {activeTab === 'ts-acf' && (
          <TabContent loading={!!tsLoading} error={tsError ?? null} data={tsProfile} emptyMessage="Configure time series columns and run analysis to see ACF results">
            {tsProfile && <ACFPanel profile={tsProfile} />}
          </TabContent>
        )}
      </div>
    </>
  )
}

function DataPreviewContent({
  preview,
  previewLoading,
  previewError,
  currentPage,
  pageSize,
  onPageChange,
  onPageSizeChange,
}: {
  preview: { columns?: string[]; rows?: Record<string, unknown>[]; total_rows?: number } | undefined
  previewLoading: boolean
  previewError: unknown
  currentPage: number
  pageSize: number
  onPageChange: (page: number) => void
  onPageSizeChange: (size: number) => void
}) {
  const totalRows = preview?.total_rows || 0
  const totalPages = Math.ceil(totalRows / pageSize)
  const startRow = (currentPage - 1) * pageSize + 1
  const endRow = Math.min(currentPage * pageSize, totalRows)

  if (previewError) {
    return (
      <div className="text-center py-20 text-domino-accent-red">
        <p className="font-medium">Failed to load data</p>
        <p className="text-sm mt-1">{previewError instanceof Error ? previewError.message : 'Unknown error'}</p>
      </div>
    )
  }

  if (!preview && !previewLoading) return null

  return (
    <div>
      {/* Page size selector */}
      <div className="flex items-center justify-between mb-3">
        <div className="flex items-center gap-2 text-sm text-domino-text-secondary">
          <span>Rows per page:</span>
          <Dropdown
            value={String(pageSize)}
            onChange={(val) => onPageSizeChange(Number(val))}
            className="w-[80px]"
            options={[
              { value: '25', label: '25' },
              { value: '50', label: '50' },
              { value: '100', label: '100' },
              { value: '250', label: '250' },
              { value: '500', label: '500' },
            ]}
          />
        </div>
        <div className="text-sm text-domino-text-muted">
          {totalRows > 0 ? `${startRow.toLocaleString()}–${endRow.toLocaleString()} of ${totalRows.toLocaleString()} rows` : '0 rows'}
        </div>
      </div>

      {/* Data table */}
      <div className="overflow-auto border border-domino-border relative" style={{ maxHeight: '500px' }}>
        {previewLoading && (
          <div className="absolute inset-0 bg-white/70 flex items-center justify-center z-10">
            <Spinner />
          </div>
        )}
        <table className="w-full text-sm">
          <thead className="sticky top-0 bg-domino-bg-tertiary">
            <tr>
              <th className="px-3 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase border-b border-domino-border w-12">
                #
              </th>
              {preview?.columns?.map((col: string) => (
                <th
                  key={col}
                  className="px-3 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase border-b border-domino-border whitespace-nowrap"
                >
                  {col}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {preview?.rows?.map((row: Record<string, unknown>, idx: number) => (
              <tr key={idx} className="hover:bg-domino-bg-tertiary border-b border-domino-border">
                <td className="px-3 py-2 text-domino-text-muted">{startRow + idx}</td>
                {preview?.columns?.map((col: string) => {
                  const value = row[col]
                  const displayValue = value === null || value === undefined
                    ? '-'
                    : typeof value === 'number'
                    ? formatCompactNumber(value)
                    : String(value)
                  return (
                    <td
                      key={col}
                      className="px-3 py-2 text-domino-text-primary whitespace-nowrap max-w-[200px] truncate"
                      title={String(value ?? '')}
                    >
                      {value === null || value === undefined ? (
                        <span className="text-domino-text-muted italic">null</span>
                      ) : (
                        displayValue
                      )}
                    </td>
                  )
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Pagination controls */}
      {totalPages > 1 && (
        <div className="flex items-center justify-end gap-2 mt-4">
          <button
            onClick={() => onPageChange(1)}
            disabled={currentPage === 1}
            className="h-[32px] px-3 text-sm border border-domino-border rounded-[2px] text-domino-text-secondary disabled:opacity-50 disabled:cursor-not-allowed hover:bg-domino-bg-tertiary"
          >
            First
          </button>
          <button
            onClick={() => onPageChange(currentPage - 1)}
            disabled={currentPage === 1}
            className="h-[32px] w-[32px] flex items-center justify-center border border-domino-border rounded-[2px] text-domino-text-secondary disabled:opacity-50 disabled:cursor-not-allowed hover:bg-domino-bg-tertiary"
          >
            &lt;
          </button>
          <span className="text-sm text-domino-text-secondary px-2">
            Page {currentPage} of {totalPages}
          </span>
          <button
            onClick={() => onPageChange(currentPage + 1)}
            disabled={currentPage === totalPages}
            className="h-[32px] w-[32px] flex items-center justify-center border border-domino-border rounded-[2px] text-domino-text-secondary disabled:opacity-50 disabled:cursor-not-allowed hover:bg-domino-bg-tertiary"
          >
            &gt;
          </button>
          <button
            onClick={() => onPageChange(totalPages)}
            disabled={currentPage === totalPages}
            className="h-[32px] px-3 text-sm border border-domino-border rounded-[2px] text-domino-text-secondary disabled:opacity-50 disabled:cursor-not-allowed hover:bg-domino-bg-tertiary"
          >
            Last
          </button>
        </div>
      )}
    </div>
  )
}

function TransformsContent({
  profile,
  transforms,
  onAddTransform,
  onRemoveTransform,
}: {
  profile: DataProfile
  transforms: TransformConfig[]
  onAddTransform: (transform: TransformConfig) => void
  onRemoveTransform: (index: number) => void
}) {
  const [selectedColumn, setSelectedColumn] = useState<string>('')
  const [selectedType, setSelectedType] = useState<TransformConfig['type']>('fillna')

  const transformTypes: { value: TransformConfig['type']; label: string }[] = [
    { value: 'fillna', label: 'Fill Missing Values' },
    { value: 'scale', label: 'Standardize/Scale' },
    { value: 'encode', label: 'One-Hot Encode' },
    { value: 'log', label: 'Log Transform' },
    { value: 'clip', label: 'Clip Outliers' },
    { value: 'drop', label: 'Drop Column' },
  ]

  const addSelectedTransform = () => {
    if (!selectedColumn) return
    onAddTransform({ column: selectedColumn, type: selectedType })
    setSelectedColumn('')
  }

  const columnsWithIssues = profile.columns.filter(
    col => col.missing_percentage > 5 || (col.issues && col.issues.length > 0)
  )

  return (
    <div className="space-y-6">
      {columnsWithIssues.length > 0 && (
        <div>
          <h3 className="text-sm font-medium text-domino-text-primary mb-3">Recommended Transformations</h3>
          <div className="space-y-2">
            {columnsWithIssues.slice(0, 5).map((col) => (
              <div key={col.name} className="flex items-center justify-between p-3 bg-domino-bg-tertiary border border-domino-border">
                <div>
                  <span className="text-sm font-medium text-domino-text-primary">{col.name}</span>
                  <span className="text-xs text-domino-text-muted ml-2">
                    {col.missing_percentage > 5 && `${col.missing_percentage.toFixed(1)}% missing`}
                    {col.issues?.length ? ` - ${col.issues[0]}` : ''}
                  </span>
                </div>
                <button
                  onClick={() => onAddTransform({
                    column: col.name,
                    type: col.missing_percentage > 5 ? 'fillna' : 'scale'
                  })}
                  className="text-sm text-domino-accent-purple hover:underline"
                >
                  Add
                </button>
              </div>
            ))}
          </div>
        </div>
      )}

      <div>
        <h3 className="text-sm font-medium text-domino-text-primary mb-3">Add Transformation</h3>
        <div className="flex gap-4 items-end">
          <div className="flex-1">
            <label className="block text-xs text-domino-text-muted mb-1">Column</label>
            <Dropdown
              value={selectedColumn}
              onChange={setSelectedColumn}
              placeholder="Select column..."
              options={profile.columns.map((col) => ({ value: col.name, label: col.name }))}
            />
          </div>
          <div className="flex-1">
            <label className="block text-xs text-domino-text-muted mb-1">Transformation</label>
            <Dropdown
              value={selectedType}
              onChange={(val) => setSelectedType(val as TransformConfig['type'])}
              options={transformTypes}
            />
          </div>
          <button
            onClick={addSelectedTransform}
            disabled={!selectedColumn}
            className="h-[32px] px-4 text-sm bg-domino-accent-purple text-white rounded-[2px] hover:bg-domino-accent-purple-hover disabled:opacity-50"
          >
            Add
          </button>
        </div>
      </div>

      <div>
        <h3 className="text-sm font-medium text-domino-text-primary mb-3">
          Selected Transformations ({transforms.length})
        </h3>
        {transforms.length === 0 ? (
          <div className="p-6 text-center text-domino-text-muted text-sm bg-domino-bg-tertiary border border-domino-border">
            No transformations selected. Add transformations to include in the exported notebook.
          </div>
        ) : (
          <div className="border border-domino-border divide-y divide-domino-border">
            {transforms.map((t, idx) => (
              <div key={idx} className="px-4 py-3 flex items-center justify-between bg-white">
                <div className="flex items-center gap-4">
                  <span className="text-xs text-domino-text-muted w-6">{idx + 1}.</span>
                  <span className="text-sm font-medium text-domino-text-primary">{t.column}</span>
                  <span className="text-xs px-2 py-1 bg-domino-bg-tertiary text-domino-text-secondary">
                    {transformTypes.find(tt => tt.value === t.type)?.label}
                  </span>
                </div>
                <button
                  onClick={() => onRemoveTransform(idx)}
                  className="text-xs text-domino-accent-red hover:underline"
                >
                  Remove
                </button>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
