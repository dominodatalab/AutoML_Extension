import { useQuery } from '@tanstack/react-query'
import api from '../api'

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
  const { data } = useQuery<ProjectUserSummary>({
    queryKey: ['user_summary'],
    queryFn: async () => {
      const { data } = await api.get<ProjectUserSummary>('health/user')
      return data
    },
    staleTime: Infinity,
    refetchOnMount: false,
    refetchOnWindowFocus: false,
  })

  return data ?? EMPTY_PROJECT_USER_SUMMARY
}
