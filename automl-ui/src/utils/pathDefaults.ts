import { getBasePath } from './basePath'

const DOMINO_DATA_ROOT = '/mnt/data'
const LOCAL_EXPORT_ROOT = './local_data/exports'
const DEFAULT_PROJECT = 'default_project'
const DEFAULT_JOB = 'job'

function sanitizeSegment(value: string, fallback: string): string {
  const safe = value.replace(/[^a-zA-Z0-9._-]/g, '_').replace(/^[-._]+|[-._]+$/g, '')
  return safe || fallback
}

export function isDominoRuntime(pathname: string = window.location.pathname): boolean {
  return getBasePath(pathname).length > 0
}

export function getDefaultExportPath(
  projectName: string,
  jobName: string,
  pathname: string = window.location.pathname,
): string {
  const safeProject = sanitizeSegment(projectName || DEFAULT_PROJECT, DEFAULT_PROJECT)
  const safeJob = sanitizeSegment(jobName || DEFAULT_JOB, DEFAULT_JOB)
  if (isDominoRuntime(pathname)) {
    return `${DOMINO_DATA_ROOT}/${safeProject}/exports/${safeJob}`
  }
  return `${LOCAL_EXPORT_ROOT}/${safeProject}/${safeJob}`
}
