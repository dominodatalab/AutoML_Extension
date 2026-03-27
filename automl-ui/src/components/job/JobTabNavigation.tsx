type DetailTab = 'overview' | 'leaderboard' | 'diagnostics' | 'learning' | 'export' | 'domino' | 'logs'

interface TabConfig {
  key: DetailTab
  label: string
  showWhenDone?: boolean
}

interface JobTabNavigationProps {
  activeTab: DetailTab
  onTabChange: (tab: DetailTab) => void
  currentStatus: string
  dominoEnabled?: boolean
}

const allTabs: TabConfig[] = [
  { key: 'overview', label: 'Overview' },
  { key: 'leaderboard', label: 'Leaderboard', showWhenDone: true },
  { key: 'diagnostics', label: 'Diagnostics', showWhenDone: true },
  { key: 'learning', label: 'Metrics', showWhenDone: true },
  { key: 'export', label: 'Outputs', showWhenDone: true },
  { key: 'domino', label: 'Deployments', showWhenDone: true },
  { key: 'logs', label: 'Logs' },
]

export function JobTabNavigation({ activeTab, onTabChange, currentStatus, dominoEnabled }: JobTabNavigationProps) {
  const tabs = allTabs.filter((tab) => {
    if (tab.showWhenDone && currentStatus !== 'completed') return false
    if (tab.key === 'domino' && !dominoEnabled) return false
    return true
  })

  return (
    <div className="border-b border-domino-border mb-6">
      <nav className="flex gap-6">
        {tabs.map((tab) => (
          <button
            key={tab.key}
            onClick={() => onTabChange(tab.key)}
            className={`pb-3 text-sm border-b-2 -mb-px transition-colors ${
              activeTab === tab.key
                ? 'border-domino-accent-purple text-domino-accent-purple font-medium'
                : 'border-transparent text-domino-text-secondary hover:text-domino-text-primary font-normal'
            }`}
          >
            {tab.label}
          </button>
        ))}
      </nav>
    </div>
  )
}

export type { DetailTab }
