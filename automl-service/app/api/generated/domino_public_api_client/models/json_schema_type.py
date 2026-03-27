from __future__ import annotations
from enum import Enum


class JSONSchemaType(str, Enum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    INTEGER = "integer"
    NULL = "null"
    NUMBER = "number"
    OBJECT = "object"
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)
