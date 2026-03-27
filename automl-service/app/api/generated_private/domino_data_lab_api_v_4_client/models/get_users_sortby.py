from enum import Enum


class GetUsersSortby(str, Enum):
    DOMINOUSERID = "dominouserid"
    EMAIL = "email"
    IDPID = "idpid"
    USERNAME = "username"

    def __str__(self) -> str:
        return str(self.value)
