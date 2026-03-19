from enum import Enum


class GetAllGatewayEndpointsSortByField(str, Enum):
    CREATIONDATE = "creationDate"
    ENDPOINTNAME = "endpointName"
    ENDPOINTTYPE = "endpointType"
    MODELNAME = "modelName"
    MODELPROVIDER = "modelProvider"

    def __str__(self) -> str:
        return str(self.value)
