from enum import Enum


class DominoDatasourceModelConnectorType(str, Enum):
    CLICKHOUSE = "clickhouse"
    DB2 = "db2"
    DRUID = "druid"
    GENERICJDBC = "genericJdbc"
    GREENPLUM = "greenplum"
    IGNITE = "ignite"
    MARIADB = "mariadb"
    NETEZZA = "netezza"
    SAPHANA = "sapHana"
    SINGLESTORE = "singlestore"
    SYNAPSE = "synapse"
    VERTICA = "vertica"

    def __str__(self) -> str:
        return str(self.value)
