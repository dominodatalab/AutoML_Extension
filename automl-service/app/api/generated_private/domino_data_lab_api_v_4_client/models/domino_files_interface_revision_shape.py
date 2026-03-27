from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_files_interface_author import DominoFilesInterfaceAuthor


T = TypeVar("T", bound="DominoFilesInterfaceRevisionShape")


@_attrs_define
class DominoFilesInterfaceRevisionShape:
    """
    Attributes:
        run_id (str):
        sha (str):
        message (str):
        timestamp (int):
        url (str):
        author (DominoFilesInterfaceAuthor):
        run_number_str (str):
        run_link (str):
    """

    run_id: str
    sha: str
    message: str
    timestamp: int
    url: str
    author: DominoFilesInterfaceAuthor
    run_number_str: str
    run_link: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        sha = self.sha

        message = self.message

        timestamp = self.timestamp

        url = self.url

        author = self.author.to_dict()

        run_number_str = self.run_number_str

        run_link = self.run_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runId": run_id,
                "sha": sha,
                "message": message,
                "timestamp": timestamp,
                "url": url,
                "author": author,
                "runNumberStr": run_number_str,
                "runLink": run_link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_files_interface_author import DominoFilesInterfaceAuthor

        d = dict(src_dict)
        run_id = d.pop("runId")

        sha = d.pop("sha")

        message = d.pop("message")

        timestamp = d.pop("timestamp")

        url = d.pop("url")

        author = DominoFilesInterfaceAuthor.from_dict(d.pop("author"))

        run_number_str = d.pop("runNumberStr")

        run_link = d.pop("runLink")

        domino_files_interface_revision_shape = cls(
            run_id=run_id,
            sha=sha,
            message=message,
            timestamp=timestamp,
            url=url,
            author=author,
            run_number_str=run_number_str,
            run_link=run_link,
        )

        domino_files_interface_revision_shape.additional_properties = d
        return domino_files_interface_revision_shape

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
