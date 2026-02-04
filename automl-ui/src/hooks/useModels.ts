import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { getModels, getModel, getModelVersions, deployModel, getModelDeployments } from '../api/models'
import { DeploymentRequest } from '../types/model'

export function useModels() {
  return useQuery({
    queryKey: ['models'],
    queryFn: getModels,
  })
}

export function useModel(modelName: string) {
  return useQuery({
    queryKey: ['model', modelName],
    queryFn: () => getModel(modelName),
    enabled: !!modelName,
  })
}

export function useModelVersions(modelName: string) {
  return useQuery({
    queryKey: ['modelVersions', modelName],
    queryFn: () => getModelVersions(modelName),
    enabled: !!modelName,
  })
}

export function useModelDeployments(modelName: string) {
  return useQuery({
    queryKey: ['modelDeployments', modelName],
    queryFn: () => getModelDeployments(modelName),
    enabled: !!modelName,
  })
}

export function useDeployModel() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: ({ modelName, request }: { modelName: string; request: DeploymentRequest }) =>
      deployModel(modelName, request),
    onSuccess: (_data, variables) => {
      queryClient.invalidateQueries({ queryKey: ['modelDeployments', variables.modelName] })
    },
  })
}
