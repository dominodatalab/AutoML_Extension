from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_project_id import DominoCommonProjectId
    from ..models.domino_nucleus_gateway_users_models_project_dependency_view import (
        DominoNucleusGatewayUsersModelsProjectDependencyView,
    )


T = TypeVar("T", bound="DominoNucleusGatewayUsersModelsProjectsDependencyGraph")


@_attrs_define
class DominoNucleusGatewayUsersModelsProjectsDependencyGraph:
    """
    Attributes:
        nodes (list[DominoNucleusGatewayUsersModelsProjectDependencyView]):
        selected_project_id (DominoCommonProjectId | Unset):
    """

    nodes: list[DominoNucleusGatewayUsersModelsProjectDependencyView]
    selected_project_id: DominoCommonProjectId | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        selected_project_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selected_project_id, Unset):
            selected_project_id = self.selected_project_id.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodes": nodes,
            }
        )
        if selected_project_id is not UNSET:
            field_dict["selectedProjectId"] = selected_project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_project_id import DominoCommonProjectId
        from ..models.domino_nucleus_gateway_users_models_project_dependency_view import (
            DominoNucleusGatewayUsersModelsProjectDependencyView,
        )

        d = dict(src_dict)
        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = DominoNucleusGatewayUsersModelsProjectDependencyView.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        _selected_project_id = d.pop("selectedProjectId", UNSET)
        selected_project_id: DominoCommonProjectId | Unset
        if isinstance(_selected_project_id, Unset):
            selected_project_id = UNSET
        else:
            selected_project_id = DominoCommonProjectId.from_dict(_selected_project_id)

        domino_nucleus_gateway_users_models_projects_dependency_graph = cls(
            nodes=nodes,
            selected_project_id=selected_project_id,
        )

        domino_nucleus_gateway_users_models_projects_dependency_graph.additional_properties = d
        return domino_nucleus_gateway_users_models_projects_dependency_graph

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
