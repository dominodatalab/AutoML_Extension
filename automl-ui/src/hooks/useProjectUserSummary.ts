import { useQuery } from '@tanstack/react-query'
import api, { getProjectIdFromUrl } from '../api'

interface ProjectUserSummary {
    username: string,
    initials: string,
    project_id: string,
    project_name: string,
    project_owner: string,
    is_domino_environment: boolean,
}

export function useProjectUserSummary(): ProjectUserSummary {
  const { data } = useQuery<ProjectUserSummary>({
    queryKey: ['user_summary'],
    queryFn: async () => {
      const { data } = await api.get<ProjectUserSummary>(`user?projectId=${getProjectIdFromUrl()}`)
      return data
    },
    staleTime: Infinity,
    refetchOnMount: false,
    refetchOnWindowFocus: false,
  })

  return data ?? {
    username: '',
    initials: '',
    project_id: '',
    project_name: '',
    project_owner: '',
    is_domino_environment: false,
  };
}

