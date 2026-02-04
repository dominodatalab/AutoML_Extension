import api from './index'
import { RegisteredModel, ModelVersion, DeploymentRequest, Deployment } from '../types/model'

export async function getModels(): Promise<RegisteredModel[]> {
  // Use models endpoint for local trained models
  const response = await api.get<RegisteredModel[]>('models')
  return response.data
}

export async function getModel(modelName: string): Promise<RegisteredModel> {
  const response = await api.post<RegisteredModel>('modelversions', { model_name: modelName })
  return response.data
}

export async function getModelVersions(modelName: string): Promise<ModelVersion[]> {
  const response = await api.post<ModelVersion[]>('modelversions', { model_name: modelName })
  return response.data
}

export async function deployModel(modelName: string, request: DeploymentRequest): Promise<Deployment> {
  const response = await api.post<Deployment>('registermodel', { model_name: modelName, ...request })
  return response.data
}

export async function getModelDeployments(modelName: string): Promise<{ model_name: string; deployments: Deployment[] }> {
  const response = await api.post<{ model_name: string; deployments: Deployment[] }>('registeredmodels', { model_name: modelName })
  return response.data
}
