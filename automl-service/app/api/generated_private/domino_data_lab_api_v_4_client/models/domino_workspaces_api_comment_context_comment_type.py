from enum import Enum


class DominoWorkspacesApiCommentContextCommentType(str, Enum):
    WORKSPACECOMMENTTHREAD = "WorkspaceCommentThread"
    WORKSPACERESULTFILECOMMENTTHREAD = "WorkspaceResultFileCommentThread"

    def __str__(self) -> str:
        return str(self.value)
