import { create } from 'zustand'
import { Job, JobStatus } from '../types/job'
import { Dataset } from '../types/dataset'
import { WizardState, DataSourceConfig, ModelTypeConfig, TrainingConfig } from '../types/wizard'

interface JobsState {
  jobs: Job[]
  selectedJob: Job | null
  isLoading: boolean
  error: string | null
}

interface DatasetsState {
  datasets: Dataset[]
  selectedDataset: Dataset | null
  isLoading: boolean
}

interface UIState {
  notifications: { id: string; message: string; type: 'success' | 'error' | 'info' }[]
}

interface SelectedDataFile {
  path: string
  name: string
}

interface AppState {
  // Jobs
  jobs: JobsState
  setJobs: (jobs: Job[]) => void
  setSelectedJob: (job: Job | null) => void
  setJobsLoading: (loading: boolean) => void
  setJobsError: (error: string | null) => void
  updateJobStatus: (jobId: string, status: JobStatus) => void

  // Datasets
  datasets: DatasetsState
  setDatasets: (datasets: Dataset[]) => void
  setSelectedDataset: (dataset: Dataset | null) => void
  setDatasetsLoading: (loading: boolean) => void

  // Wizard
  wizard: WizardState
  setWizardStep: (step: number) => void
  setWizardDataSource: (config: DataSourceConfig | null) => void
  setWizardModelType: (config: ModelTypeConfig | null) => void
  setWizardTraining: (config: TrainingConfig | null) => void
  setWizardJobInfo: (name: string, description: string) => void
  resetWizard: () => void

  // UI
  ui: UIState
  addNotification: (message: string, type: 'success' | 'error' | 'info') => void
  removeNotification: (id: string) => void

  // Selected Data File (for EDA)
  selectedDataFile: SelectedDataFile | null
  setSelectedDataFile: (file: SelectedDataFile | null) => void
}

const initialWizardState: WizardState = {
  currentStep: 0,
  dataSource: null,
  modelType: null,
  training: null,
  jobName: '',
  jobDescription: '',
}

export const useStore = create<AppState>((set) => ({
  // Jobs state
  jobs: {
    jobs: [],
    selectedJob: null,
    isLoading: false,
    error: null,
  },
  setJobs: (jobs) => set((state) => ({ jobs: { ...state.jobs, jobs } })),
  setSelectedJob: (job) => set((state) => ({ jobs: { ...state.jobs, selectedJob: job } })),
  setJobsLoading: (loading) => set((state) => ({ jobs: { ...state.jobs, isLoading: loading } })),
  setJobsError: (error) => set((state) => ({ jobs: { ...state.jobs, error } })),
  updateJobStatus: (jobId, status) =>
    set((state) => ({
      jobs: {
        ...state.jobs,
        jobs: state.jobs.jobs.map((j) => (j.id === jobId ? { ...j, status } : j)),
      },
    })),

  // Datasets state
  datasets: {
    datasets: [],
    selectedDataset: null,
    isLoading: false,
  },
  setDatasets: (datasets) => set((state) => ({ datasets: { ...state.datasets, datasets } })),
  setSelectedDataset: (dataset) =>
    set((state) => ({ datasets: { ...state.datasets, selectedDataset: dataset } })),
  setDatasetsLoading: (loading) =>
    set((state) => ({ datasets: { ...state.datasets, isLoading: loading } })),

  // Wizard state
  wizard: initialWizardState,
  setWizardStep: (step) => set((state) => ({ wizard: { ...state.wizard, currentStep: step } })),
  setWizardDataSource: (config) =>
    set((state) => ({ wizard: { ...state.wizard, dataSource: config } })),
  setWizardModelType: (config) =>
    set((state) => ({ wizard: { ...state.wizard, modelType: config } })),
  setWizardTraining: (config) =>
    set((state) => ({ wizard: { ...state.wizard, training: config } })),
  setWizardJobInfo: (name, description) =>
    set((state) => ({ wizard: { ...state.wizard, jobName: name, jobDescription: description } })),
  resetWizard: () => set({ wizard: initialWizardState }),

  // UI state
  ui: {
    notifications: [],
  },
  addNotification: (message, type) =>
    set((state) => ({
      ui: {
        ...state.ui,
        notifications: [
          ...state.ui.notifications,
          { id: Date.now().toString(), message, type },
        ],
      },
    })),
  removeNotification: (id) =>
    set((state) => ({
      ui: {
        ...state.ui,
        notifications: state.ui.notifications.filter((n) => n.id !== id),
      },
    })),

  // Selected Data File
  selectedDataFile: null,
  setSelectedDataFile: (file) => set({ selectedDataFile: file }),
}))
