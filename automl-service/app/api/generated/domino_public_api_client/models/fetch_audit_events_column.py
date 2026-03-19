from enum import Enum


class FetchAuditEventsColumn(str, Enum):
    AFTER_VALUE = "after_value"
    BEFORE_VALUE = "before_value"
    DATASET_NAME = "dataset_name"
    DATE_TIME = "date_time"
    ELECTRONICALLY_SIGNED = "electronically_signed"
    ENVIRONMENT = "environment"
    EVENT = "event"
    FEATURE_FLAG = "feature_flag"
    FILE_NAME = "file_name"
    FIRST_NAME = "first_name"
    JOBS = "jobs"
    LAST_NAME = "last_name"
    PROJECT_NAME = "project_name"
    REASON_FOR_CHANGE = "reason_for_change"
    REASON_FOR_CHANGE_ADDITIONAL_INFO = "reason_for_change_additional_info"
    TARGET_NAME = "target_name"
    TARGET_USER = "target_user"
    USER_NAME = "user_name"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
