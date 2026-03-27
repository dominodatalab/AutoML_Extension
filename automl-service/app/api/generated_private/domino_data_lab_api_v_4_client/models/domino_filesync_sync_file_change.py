from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_filesync_sync_file_signature import DominoFilesyncSyncFileSignature
    from ..models.domino_filesync_sync_relative_file_path import DominoFilesyncSyncRelativeFilePath


T = TypeVar("T", bound="DominoFilesyncSyncFileChange")


@_attrs_define
class DominoFilesyncSyncFileChange:
    """
    Attributes:
        path (DominoFilesyncSyncRelativeFilePath):
        maybe_base_signature (DominoFilesyncSyncFileSignature | Unset):
        maybe_target_signature (DominoFilesyncSyncFileSignature | Unset):
    """

    path: DominoFilesyncSyncRelativeFilePath
    maybe_base_signature: DominoFilesyncSyncFileSignature | Unset = UNSET
    maybe_target_signature: DominoFilesyncSyncFileSignature | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path.to_dict()

        maybe_base_signature: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maybe_base_signature, Unset):
            maybe_base_signature = self.maybe_base_signature.to_dict()

        maybe_target_signature: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maybe_target_signature, Unset):
            maybe_target_signature = self.maybe_target_signature.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if maybe_base_signature is not UNSET:
            field_dict["maybeBaseSignature"] = maybe_base_signature
        if maybe_target_signature is not UNSET:
            field_dict["maybeTargetSignature"] = maybe_target_signature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_filesync_sync_file_signature import DominoFilesyncSyncFileSignature
        from ..models.domino_filesync_sync_relative_file_path import DominoFilesyncSyncRelativeFilePath

        d = dict(src_dict)
        path = DominoFilesyncSyncRelativeFilePath.from_dict(d.pop("path"))

        _maybe_base_signature = d.pop("maybeBaseSignature", UNSET)
        maybe_base_signature: DominoFilesyncSyncFileSignature | Unset
        if isinstance(_maybe_base_signature, Unset):
            maybe_base_signature = UNSET
        else:
            maybe_base_signature = DominoFilesyncSyncFileSignature.from_dict(_maybe_base_signature)

        _maybe_target_signature = d.pop("maybeTargetSignature", UNSET)
        maybe_target_signature: DominoFilesyncSyncFileSignature | Unset
        if isinstance(_maybe_target_signature, Unset):
            maybe_target_signature = UNSET
        else:
            maybe_target_signature = DominoFilesyncSyncFileSignature.from_dict(_maybe_target_signature)

        domino_filesync_sync_file_change = cls(
            path=path,
            maybe_base_signature=maybe_base_signature,
            maybe_target_signature=maybe_target_signature,
        )

        domino_filesync_sync_file_change.additional_properties = d
        return domino_filesync_sync_file_change

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
