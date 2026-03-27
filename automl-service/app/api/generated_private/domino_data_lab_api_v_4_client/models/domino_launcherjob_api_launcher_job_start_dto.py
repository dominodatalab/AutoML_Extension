from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_launcherjob_api_launcher_job_uploaded_file import DominoLauncherjobApiLauncherJobUploadedFile
    from ..models.domino_launcherjob_api_post_parameter import DominoLauncherjobApiPostParameter


T = TypeVar("T", bound="DominoLauncherjobApiLauncherJobStartDto")


@_attrs_define
class DominoLauncherjobApiLauncherJobStartDto:
    """
    Attributes:
        project (str):
        post_parameters (list[DominoLauncherjobApiPostParameter]):
        uploaded_files (list[DominoLauncherjobApiLauncherJobUploadedFile]):
        notify_on_complete_email_addresses (list[str]):
        job_title (None | str | Unset):
        starting_user_id (None | str | Unset):
    """

    project: str
    post_parameters: list[DominoLauncherjobApiPostParameter]
    uploaded_files: list[DominoLauncherjobApiLauncherJobUploadedFile]
    notify_on_complete_email_addresses: list[str]
    job_title: None | str | Unset = UNSET
    starting_user_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project = self.project

        post_parameters = []
        for post_parameters_item_data in self.post_parameters:
            post_parameters_item = post_parameters_item_data.to_dict()
            post_parameters.append(post_parameters_item)

        uploaded_files = []
        for uploaded_files_item_data in self.uploaded_files:
            uploaded_files_item = uploaded_files_item_data.to_dict()
            uploaded_files.append(uploaded_files_item)

        notify_on_complete_email_addresses = self.notify_on_complete_email_addresses

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        else:
            job_title = self.job_title

        starting_user_id: None | str | Unset
        if isinstance(self.starting_user_id, Unset):
            starting_user_id = UNSET
        else:
            starting_user_id = self.starting_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project": project,
                "postParameters": post_parameters,
                "uploadedFiles": uploaded_files,
                "notifyOnCompleteEmailAddresses": notify_on_complete_email_addresses,
            }
        )
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if starting_user_id is not UNSET:
            field_dict["startingUserId"] = starting_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_launcherjob_api_launcher_job_uploaded_file import (
            DominoLauncherjobApiLauncherJobUploadedFile,
        )
        from ..models.domino_launcherjob_api_post_parameter import DominoLauncherjobApiPostParameter

        d = dict(src_dict)
        project = d.pop("project")

        post_parameters = []
        _post_parameters = d.pop("postParameters")
        for post_parameters_item_data in _post_parameters:
            post_parameters_item = DominoLauncherjobApiPostParameter.from_dict(post_parameters_item_data)

            post_parameters.append(post_parameters_item)

        uploaded_files = []
        _uploaded_files = d.pop("uploadedFiles")
        for uploaded_files_item_data in _uploaded_files:
            uploaded_files_item = DominoLauncherjobApiLauncherJobUploadedFile.from_dict(uploaded_files_item_data)

            uploaded_files.append(uploaded_files_item)

        notify_on_complete_email_addresses = cast(list[str], d.pop("notifyOnCompleteEmailAddresses"))

        def _parse_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))

        def _parse_starting_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        starting_user_id = _parse_starting_user_id(d.pop("startingUserId", UNSET))

        domino_launcherjob_api_launcher_job_start_dto = cls(
            project=project,
            post_parameters=post_parameters,
            uploaded_files=uploaded_files,
            notify_on_complete_email_addresses=notify_on_complete_email_addresses,
            job_title=job_title,
            starting_user_id=starting_user_id,
        )

        domino_launcherjob_api_launcher_job_start_dto.additional_properties = d
        return domino_launcherjob_api_launcher_job_start_dto

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
