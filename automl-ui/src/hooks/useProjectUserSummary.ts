import { useQuery } from '@tanstack/react-query'
import api from '../api'
import { useStore } from '../store'
import { getErrorMessage } from '../utils/errors'

interface ProjectUserSummary {
    username: string,
    initials: string,
    project_id: string,
    project_name: string,
    project_owner: string,
    is_domino_environment: boolean,
}

const EMPTY_PROJECT_USER_SUMMARY: ProjectUserSummary = {
  username: '',
  initials: '',
  project_id: '',
  project_name: '',
  project_owner: '',
  is_domino_environment: false,
}

export function useProjectUserSummary(): ProjectUserSummary {
  const addNotification = useStore((state) => state.addNotification)

  const { data } = useQuery<ProjectUserSummary>({
    queryKey: ['user_summary'],
    queryFn: async () => {
      try {
        const { data } = await api.get<ProjectUserSummary>('health/user')
        return data
      } catch (error) {
        addNotification(getErrorMessage(error), 'error')
        throw error
      }
    },
    staleTime: Infinity,
    refetchOnMount: false,
    refetchOnWindowFocus: false,
    retry: false,
  })

  return data ?? EMPTY_PROJECT_USER_SUMMARY
}
