from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.linked_goal_v1 import LinkedGoalV1
    from ..models.metadata_v1 import MetadataV1


T = TypeVar("T", bound="PaginatedGoalEnvelopeV1")


@_attrs_define
class PaginatedGoalEnvelopeV1:
    """
    Attributes:
        goals (list[LinkedGoalV1]):
        metadata (MetadataV1):
    """

    goals: list[LinkedGoalV1]
    metadata: MetadataV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goals = []
        for goals_item_data in self.goals:
            goals_item = goals_item_data.to_dict()
            goals.append(goals_item)

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "goals": goals,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linked_goal_v1 import LinkedGoalV1
        from ..models.metadata_v1 import MetadataV1

        d = dict(src_dict)
        goals = []
        _goals = d.pop("goals")
        for goals_item_data in _goals:
            goals_item = LinkedGoalV1.from_dict(goals_item_data)

            goals.append(goals_item)

        metadata = MetadataV1.from_dict(d.pop("metadata"))

        paginated_goal_envelope_v1 = cls(
            goals=goals,
            metadata=metadata,
        )

        paginated_goal_envelope_v1.additional_properties = d
        return paginated_goal_envelope_v1

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
