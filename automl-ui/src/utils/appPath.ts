import { getProjectIdFromUrl } from '../api'

type AppPathParams = URLSearchParams | Record<string, string | undefined> | undefined

export function buildAppPath(path: string, params?: AppPathParams): string {
  const [pathname, existingQuery = ''] = path.split('?')
  const searchParams = new URLSearchParams(existingQuery)

  if (params instanceof URLSearchParams) {
    params.forEach((value, key) => {
      searchParams.set(key, value)
    })
  } else if (params) {
    Object.entries(params).forEach(([key, value]) => {
      if (value !== undefined) {
        searchParams.set(key, value)
      }
    })
  }

  const projectId = getProjectIdFromUrl()
  if (projectId && !searchParams.has('projectId')) {
    searchParams.set('projectId', projectId)
  }

  const query = searchParams.toString()
  return query ? `${pathname}?${query}` : pathname
}
