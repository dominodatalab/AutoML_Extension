from enum import Enum


class DominoActivityApiFileChangeActivityMetaDataAction(str, Enum):
    FILE_CHANGED = "File Changed"
    FILE_CREATEDMODIFIED = "File Created/Modified"
    FILE_FULLY_DELETED = "File Fully Deleted"
    FILE_RENAMED = "File Renamed"
    FOLDER_CREATEDMODIFIED = "Folder Created/Modified"
    FOLDER_RENAMED = "Folder Renamed"
    MOVED_FILEFOLDER = "Moved File/Folder"
    MOVED_FILESFOLDERS = "Moved Files/Folders"
    REMOVED_FILEFOLDER = "Removed File/Folder"
    REMOVED_FILESFOLDERS = "Removed Files/Folders"

    def __str__(self) -> str:
        return str(self.value)
