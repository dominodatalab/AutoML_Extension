from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_datasetrw_web_presigned_url import DominoDatasetrwWebPresignedUrl


T = TypeVar("T", bound="DominoDatasetrwWebCreateSnapshotFromFlowsArtifactsRequest")


@_attrs_define
class DominoDatasetrwWebCreateSnapshotFromFlowsArtifactsRequest:
    """
    Attributes:
        presigned_urls (list[DominoDatasetrwWebPresignedUrl]):
        signature (str):
        artifact_id (str):
        project (str):
        domain (str):
        name (str):
    """

    presigned_urls: list[DominoDatasetrwWebPresignedUrl]
    signature: str
    artifact_id: str
    project: str
    domain: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        presigned_urls = []
        for presigned_urls_item_data in self.presigned_urls:
            presigned_urls_item = presigned_urls_item_data.to_dict()
            presigned_urls.append(presigned_urls_item)

        signature = self.signature

        artifact_id = self.artifact_id

        project = self.project

        domain = self.domain

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "presignedUrls": presigned_urls,
                "signature": signature,
                "artifactId": artifact_id,
                "project": project,
                "domain": domain,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasetrw_web_presigned_url import DominoDatasetrwWebPresignedUrl

        d = dict(src_dict)
        presigned_urls = []
        _presigned_urls = d.pop("presignedUrls")
        for presigned_urls_item_data in _presigned_urls:
            presigned_urls_item = DominoDatasetrwWebPresignedUrl.from_dict(presigned_urls_item_data)

            presigned_urls.append(presigned_urls_item)

        signature = d.pop("signature")

        artifact_id = d.pop("artifactId")

        project = d.pop("project")

        domain = d.pop("domain")

        name = d.pop("name")

        domino_datasetrw_web_create_snapshot_from_flows_artifacts_request = cls(
            presigned_urls=presigned_urls,
            signature=signature,
            artifact_id=artifact_id,
            project=project,
            domain=domain,
            name=name,
        )

        domino_datasetrw_web_create_snapshot_from_flows_artifacts_request.additional_properties = d
        return domino_datasetrw_web_create_snapshot_from_flows_artifacts_request

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
