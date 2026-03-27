from enum import Enum


class DominoGruzApiRawRunCommandRunCommandType(str, Enum):
    APP = "App"
    ARGV = "Argv"
    DIRECT = "Direct"
    INTERACTIVESESSION = "InteractiveSession"
    LAUNCHER = "Launcher"

    def __str__(self) -> str:
        return str(self.value)
