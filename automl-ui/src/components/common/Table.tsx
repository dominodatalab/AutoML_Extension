import { HTMLAttributes, TdHTMLAttributes, ThHTMLAttributes, forwardRef } from 'react'
import clsx from 'clsx'
import { ChevronUpIcon, ChevronDownIcon } from '@heroicons/react/24/outline'

interface TableProps extends HTMLAttributes<HTMLTableElement> {
  pagination?: {
    currentPage: number
    totalPages: number
    totalItems: number
    itemsPerPage: number
    onPageChange: (page: number) => void
  }
}

const Table = forwardRef<HTMLTableElement, TableProps>(
  ({ className, pagination, children, ...props }, ref) => (
    <div className="w-full">
      <div className="overflow-auto">
        <table
          ref={ref}
          className={clsx('w-full caption-bottom text-sm', className)}
          {...props}
        >
          {children}
        </table>
      </div>
      {pagination && (
        <TablePagination {...pagination} />
      )}
    </div>
  )
)
Table.displayName = 'Table'

const TableHeader = forwardRef<HTMLTableSectionElement, HTMLAttributes<HTMLTableSectionElement>>(
  ({ className, ...props }, ref) => (
    <thead ref={ref} className={clsx('border-b border-domino-border bg-white', className)} {...props} />
  )
)
TableHeader.displayName = 'TableHeader'

const TableBody = forwardRef<HTMLTableSectionElement, HTMLAttributes<HTMLTableSectionElement>>(
  ({ className, ...props }, ref) => (
    <tbody ref={ref} className={clsx('[&_tr:last-child]:border-0 bg-white', className)} {...props} />
  )
)
TableBody.displayName = 'TableBody'

const TableRow = forwardRef<HTMLTableRowElement, HTMLAttributes<HTMLTableRowElement>>(
  ({ className, ...props }, ref) => (
    <tr
      ref={ref}
      className={clsx(
        'border-b border-domino-border transition-colors hover:bg-domino-bg-hover',
        className
      )}
      {...props}
    />
  )
)
TableRow.displayName = 'TableRow'

interface TableHeadProps extends ThHTMLAttributes<HTMLTableCellElement> {
  sortable?: boolean
  sorted?: 'asc' | 'desc' | null
  onSort?: () => void
}

const TableHead = forwardRef<HTMLTableCellElement, TableHeadProps>(
  ({ className, sortable, sorted, onSort, children, ...props }, ref) => (
    <th
      ref={ref}
      className={clsx(
        'h-10 px-4 text-left align-middle font-normal text-domino-text-secondary text-xs uppercase tracking-wider',
        sortable && 'cursor-pointer select-none hover:text-domino-text-primary',
        className
      )}
      onClick={sortable ? onSort : undefined}
      {...props}
    >
      <div className="flex items-center gap-1">
        {children}
        {sortable && (
          <span className="flex flex-col -space-y-1">
            <ChevronUpIcon className={clsx('h-3 w-3', sorted === 'asc' ? 'text-domino-accent-purple' : 'text-domino-text-muted')} />
            <ChevronDownIcon className={clsx('h-3 w-3', sorted === 'desc' ? 'text-domino-accent-purple' : 'text-domino-text-muted')} />
          </span>
        )}
      </div>
    </th>
  )
)
TableHead.displayName = 'TableHead'

const TableCell = forwardRef<HTMLTableCellElement, TdHTMLAttributes<HTMLTableCellElement>>(
  ({ className, ...props }, ref) => (
    <td
      ref={ref}
      className={clsx('px-4 py-3 align-middle text-domino-text-primary', className)}
      {...props}
    />
  )
)
TableCell.displayName = 'TableCell'

// Pagination component matching Domino style
interface TablePaginationProps {
  currentPage: number
  totalPages: number
  totalItems: number
  itemsPerPage: number
  onPageChange: (page: number) => void
}

function TablePagination({ currentPage, totalPages, totalItems, itemsPerPage, onPageChange }: TablePaginationProps) {
  const startItem = (currentPage - 1) * itemsPerPage + 1
  const endItem = Math.min(currentPage * itemsPerPage, totalItems)

  return (
    <div className="flex items-center justify-end gap-4 py-4 px-4 text-sm text-domino-text-secondary">
      <span>
        Showing {startItem} - {endItem} out of {totalItems}
      </span>
      <div className="flex items-center gap-1">
        <button
          onClick={() => onPageChange(currentPage - 1)}
          disabled={currentPage <= 1}
          className="px-2 py-1 text-domino-text-muted hover:text-domino-text-primary disabled:opacity-50 disabled:cursor-not-allowed"
        >
          &lt;
        </button>
        {Array.from({ length: Math.min(totalPages, 5) }, (_, i) => i + 1).map((page) => (
          <button
            key={page}
            onClick={() => onPageChange(page)}
            className={clsx(
              'w-8 h-8 flex items-center justify-center border',
              page === currentPage
                ? 'border-domino-accent-purple text-domino-accent-purple'
                : 'border-transparent text-domino-text-secondary hover:text-domino-text-primary'
            )}
          >
            {page}
          </button>
        ))}
        <button
          onClick={() => onPageChange(currentPage + 1)}
          disabled={currentPage >= totalPages}
          className="px-2 py-1 text-domino-text-muted hover:text-domino-text-primary disabled:opacity-50 disabled:cursor-not-allowed"
        >
          &gt;
        </button>
      </div>
    </div>
  )
}

export { Table, TableHeader, TableBody, TableRow, TableHead, TableCell, TablePagination }
