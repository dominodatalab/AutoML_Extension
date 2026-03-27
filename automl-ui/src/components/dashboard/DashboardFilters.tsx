import { Link } from 'react-router-dom'
import {
  ArchiveBoxXMarkIcon,
  MagnifyingGlassIcon,
  Squares2X2Icon,
  TableCellsIcon,
} from '@heroicons/react/24/outline'
import Dropdown from '../common/Dropdown'
import { buildAppPath } from '../../utils/appPath'

type ViewMode = 'table' | 'card'

interface DashboardFiltersProps {
  search: string
  onSearchChange: (value: string) => void
  statusFilter: string
  onStatusFilterChange: (value: string) => void
  typeFilter: string
  onTypeFilterChange: (value: string) => void
  viewMode: ViewMode
  onViewModeChange: (mode: ViewMode) => void
  showStorageCleanup: boolean
  onStorageCleanupClick: () => void
}

export function DashboardFilters({
  search,
  onSearchChange,
  statusFilter,
  onStatusFilterChange,
  typeFilter,
  onTypeFilterChange,
  viewMode,
  onViewModeChange,
  showStorageCleanup,
  onStorageCleanupClick,
}: DashboardFiltersProps) {
  return (
    <>
      {/* Page header */}
      <div className="flex items-center justify-between flex-wrap mb-5">
        <div>
          <h1 className="text-2xl font-normal text-domino-text-primary leading-tight">AutoML</h1>
        </div>
        <div className="flex items-center gap-3">
          {/*<Link to="/eda">
            <button className="h-[32px] px-[15px] bg-white text-domino-accent-purple text-sm font-normal rounded-[2px] border border-domino-accent-purple hover:bg-domino-accent-purple/5 transition-all duration-200 inline-flex items-center gap-2">
              <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
              Explore Data
            </button>
          </Link>*/}
          <Link to={buildAppPath('/jobs/new')}>
            <button className="h-[32px] px-[15px] bg-domino-accent-purple text-white text-sm font-normal rounded-[2px] hover:bg-domino-accent-purple-hover transition-all duration-200 inline-flex items-center">
              New training job
            </button>
          </Link>
          {showStorageCleanup && (
            <button
              onClick={onStorageCleanupClick}
              className="h-[32px] px-[15px] bg-[#EDECFB] text-[#1820A0] text-sm font-normal rounded-[4px] border border-[#C9C5F2] hover:bg-[#E2E0F8] transition-all duration-200 inline-flex items-center gap-2"
            >
              <ArchiveBoxXMarkIcon className="h-4 w-4" />
              Storage cleanup
            </button>
          )}
        </div>
      </div>

      {/* Toolbar: search, filters, view toggle */}
      <div className="flex items-center gap-4 mb-6">
        {/* Search */}
        <div className="relative">
          <MagnifyingGlassIcon className="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-domino-text-muted" />
          <input
            type="text"
            placeholder="Search job name"
            value={search}
            onChange={(e) => onSearchChange(e.target.value)}
            className="pl-[11px] pr-9 h-[32px] w-[220px] text-sm border border-domino-border rounded-[2px] bg-white text-domino-text-primary placeholder-domino-text-muted focus:outline-none focus:border-domino-accent-purple transition-all duration-200"
          />
        </div>

        {/* Status filter */}
        <Dropdown
          value={statusFilter}
          onChange={onStatusFilterChange}
          placeholder="Filter by status"
          className="w-[160px]"
          options={[
            { value: '', label: 'All statuses' },
            { value: 'running', label: 'Running' },
            { value: 'completed', label: 'Completed' },
            { value: 'failed', label: 'Failed' },
            { value: 'pending', label: 'Pending' },
            { value: 'cancelled', label: 'Cancelled' },
          ]}
        />

        {/* Type filter */}
        <Dropdown
          value={typeFilter}
          onChange={onTypeFilterChange}
          placeholder="Filter by type"
          className="w-[160px]"
          options={[
            { value: '', label: 'All types' },
            { value: 'tabular', label: 'Tabular' },
            { value: 'timeseries', label: 'Time series' },
          ]}
        />

        <div className="flex-1" />

        {/* View toggle */}
        <div className="flex border border-domino-border rounded-[2px] overflow-hidden">
          <button
            onClick={() => onViewModeChange('table')}
            className={`h-[32px] w-[32px] flex items-center justify-center ${viewMode === 'table' ? 'bg-domino-bg-tertiary' : 'bg-white hover:bg-domino-bg-tertiary'}`}
            title="Table view"
          >
            <TableCellsIcon className="h-4 w-4 text-domino-text-secondary" />
          </button>
          <button
            onClick={() => onViewModeChange('card')}
            className={`h-[32px] w-[32px] flex items-center justify-center border-l border-domino-border ${viewMode === 'card' ? 'bg-domino-bg-tertiary' : 'bg-white hover:bg-domino-bg-tertiary'}`}
            title="Card view"
          >
            <Squares2X2Icon className="h-4 w-4 text-domino-text-secondary" />
          </button>
        </div>
      </div>
    </>
  )
}
