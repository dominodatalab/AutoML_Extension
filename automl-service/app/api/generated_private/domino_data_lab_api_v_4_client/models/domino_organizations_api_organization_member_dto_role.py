from enum import Enum


class DominoOrganizationsApiOrganizationMemberDTORole(str, Enum):
    ADMIN = "Admin"
    MEMBER = "Member"

    def __str__(self) -> str:
        return str(self.value)
