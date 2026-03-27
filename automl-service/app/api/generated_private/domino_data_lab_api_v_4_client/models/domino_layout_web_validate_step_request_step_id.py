from enum import Enum


class DominoLayoutWebValidateStepRequestStepID(str, Enum):
    AUTHENTICATE = "Authenticate"
    CONFIGURE = "Configure"
    CONFIGUREONLINESTORE = "ConfigureOnlineStore"

    def __str__(self) -> str:
        return str(self.value)
