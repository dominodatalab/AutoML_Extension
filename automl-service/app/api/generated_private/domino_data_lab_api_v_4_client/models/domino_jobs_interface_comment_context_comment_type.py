from enum import Enum


class DominoJobsInterfaceCommentContextCommentType(str, Enum):
    JOBCOMMENTTHREAD = "JobCommentThread"
    JOBRESULTFILECOMMENTTHREAD = "JobResultFileCommentThread"

    def __str__(self) -> str:
        return str(self.value)
