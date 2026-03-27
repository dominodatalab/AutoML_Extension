from __future__ import annotations
from enum import Enum


class CloudCostMetricsV1(str, Enum):
    AMORTIZEDNETCOST = "AmortizedNetCost"
    INVOICEDCOST = "InvoicedCost"
    LISTCOST = "ListCost"
    NETCOST = "NetCost"

    def __str__(self) -> str:
        return str(self.value)
