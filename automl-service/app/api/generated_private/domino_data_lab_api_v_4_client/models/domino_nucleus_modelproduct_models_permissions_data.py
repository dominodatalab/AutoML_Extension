from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_nucleus_modelproduct_models_permissions_data_app_access_status import (
    DominoNucleusModelproductModelsPermissionsDataAppAccessStatus,
)
from ..models.domino_nucleus_modelproduct_models_permissions_data_visibility import (
    DominoNucleusModelproductModelsPermissionsDataVisibility,
)

if TYPE_CHECKING:
    from ..models.domino_nucleus_modelproduct_models_permissions_data_access_request_statuses import (
        DominoNucleusModelproductModelsPermissionsDataAccessRequestStatuses,
    )


T = TypeVar("T", bound="DominoNucleusModelproductModelsPermissionsData")


@_attrs_define
class DominoNucleusModelproductModelsPermissionsData:
    """ModelProduct permissions

    Attributes:
        app_access_status (DominoNucleusModelproductModelsPermissionsDataAppAccessStatus):
        pending_invitations (list[str]):
        visibility (DominoNucleusModelproductModelsPermissionsDataVisibility):
        discoverable (bool):
        access_request_statuses (DominoNucleusModelproductModelsPermissionsDataAccessRequestStatuses):
    """

    app_access_status: DominoNucleusModelproductModelsPermissionsDataAppAccessStatus
    pending_invitations: list[str]
    visibility: DominoNucleusModelproductModelsPermissionsDataVisibility
    discoverable: bool
    access_request_statuses: DominoNucleusModelproductModelsPermissionsDataAccessRequestStatuses
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_access_status = self.app_access_status.value

        pending_invitations = self.pending_invitations

        visibility = self.visibility.value

        discoverable = self.discoverable

        access_request_statuses = self.access_request_statuses.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appAccessStatus": app_access_status,
                "pendingInvitations": pending_invitations,
                "visibility": visibility,
                "discoverable": discoverable,
                "accessRequestStatuses": access_request_statuses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_nucleus_modelproduct_models_permissions_data_access_request_statuses import (
            DominoNucleusModelproductModelsPermissionsDataAccessRequestStatuses,
        )

        d = dict(src_dict)
        app_access_status = DominoNucleusModelproductModelsPermissionsDataAppAccessStatus(d.pop("appAccessStatus"))

        pending_invitations = cast(list[str], d.pop("pendingInvitations"))

        visibility = DominoNucleusModelproductModelsPermissionsDataVisibility(d.pop("visibility"))

        discoverable = d.pop("discoverable")

        access_request_statuses = DominoNucleusModelproductModelsPermissionsDataAccessRequestStatuses.from_dict(
            d.pop("accessRequestStatuses")
        )

        domino_nucleus_modelproduct_models_permissions_data = cls(
            app_access_status=app_access_status,
            pending_invitations=pending_invitations,
            visibility=visibility,
            discoverable=discoverable,
            access_request_statuses=access_request_statuses,
        )

        domino_nucleus_modelproduct_models_permissions_data.additional_properties = d
        return domino_nucleus_modelproduct_models_permissions_data

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
