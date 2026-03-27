from enum import Enum


class DominoComputegridExecutionEventDtoResourceKind(str, Enum):
    CONFIGMAP = "ConfigMap"
    DEPLOYMENT = "Deployment"
    EVENT = "Event"
    HORIZONTALPODAUTOSCALER = "HorizontalPodAutoscaler"
    INGRESS = "Ingress"
    JOB = "Job"
    NETWORKPOLICY = "NetworkPolicy"
    NODE = "Node"
    OTHER = "Other"
    PERSISTENTVOLUME = "PersistentVolume"
    PERSISTENTVOLUMECLAIM = "PersistentVolumeClaim"
    POD = "Pod"
    PRIORITYCLASS = "PriorityClass"
    ROLE = "Role"
    ROLEBINDING = "RoleBinding"
    SECRET = "Secret"
    SERVICE = "Service"
    SERVICEACCOUNT = "ServiceAccount"
    STATEFULSET = "StatefulSet"

    def __str__(self) -> str:
        return str(self.value)
