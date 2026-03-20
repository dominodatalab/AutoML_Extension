from enum import Enum


class JSONSchemaFormat(str, Enum):
    BINARY = "binary"
    BYTE = "byte"
    DATE = "date"
    DATE_TIME = "date-time"
    DOUBLE = "double"
    DURATION = "duration"
    EMAIL = "email"
    FLOAT = "float"
    HOSTNAME = "hostname"
    IDN_EMAIL = "idn-email"
    IDN_HOSTNAME = "idn-hostname"
    INT32 = "int32"
    INT64 = "int64"
    IPV4 = "ipv4"
    IPV6 = "ipv6"
    IRI = "iri"
    IRI_REFERENCE = "iri-reference"
    JSON_POINTER = "json-pointer"
    MULTILINE = "multiline"
    PASSWORD = "password"
    PASSWORD_MULTILINE = "password-multiline"
    REGEX = "regex"
    RELATIVE_JSON_POINTER = "relative-json-pointer"
    TIME = "time"
    URI = "uri"
    URI_REFERENCE = "uri-reference"
    URI_TEMPLATE = "uri-template"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
