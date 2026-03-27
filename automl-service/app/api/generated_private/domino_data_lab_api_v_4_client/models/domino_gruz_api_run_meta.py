from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_gruz_api_dataset_mount import DominoGruzApiDatasetMount
    from ..models.domino_gruz_api_prepared_repository import DominoGruzApiPreparedRepository
    from ..models.domino_gruz_api_run_dependency_project import DominoGruzApiRunDependencyProject
    from ..models.domino_gruz_api_run_post_processing import DominoGruzApiRunPostProcessing
    from ..models.domino_gruz_api_status_change import DominoGruzApiStatusChange
    from ..models.domino_gruz_api_stop_request import DominoGruzApiStopRequest


T = TypeVar("T", bound="DominoGruzApiRunMeta")


@_attrs_define
class DominoGruzApiRunMeta:
    """
    Attributes:
        queued (datetime.datetime):
        dependency_projects (list[DominoGruzApiRunDependencyProject]):
        post_processing (DominoGruzApiRunPostProcessing):
        priority (int):
        status_changes (list[DominoGruzApiStatusChange]):
        publicly_visible (bool):
        started (datetime.datetime | None | Unset):
        completed (datetime.datetime | None | Unset):
        title (None | str | Unset):
        number (int | None | Unset):
        override_hardware_tier_id (None | str | Unset):
        cents_per_minute (float | None | Unset):
        isolated_output_commit (bool | None | Unset):
        repositories (list[DominoGruzApiPreparedRepository] | None | Unset):
        stop_request (DominoGruzApiStopRequest | Unset):
        dataset_mounts (list[DominoGruzApiDatasetMount] | None | Unset):
    """

    queued: datetime.datetime
    dependency_projects: list[DominoGruzApiRunDependencyProject]
    post_processing: DominoGruzApiRunPostProcessing
    priority: int
    status_changes: list[DominoGruzApiStatusChange]
    publicly_visible: bool
    started: datetime.datetime | None | Unset = UNSET
    completed: datetime.datetime | None | Unset = UNSET
    title: None | str | Unset = UNSET
    number: int | None | Unset = UNSET
    override_hardware_tier_id: None | str | Unset = UNSET
    cents_per_minute: float | None | Unset = UNSET
    isolated_output_commit: bool | None | Unset = UNSET
    repositories: list[DominoGruzApiPreparedRepository] | None | Unset = UNSET
    stop_request: DominoGruzApiStopRequest | Unset = UNSET
    dataset_mounts: list[DominoGruzApiDatasetMount] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queued = self.queued.isoformat()

        dependency_projects = []
        for dependency_projects_item_data in self.dependency_projects:
            dependency_projects_item = dependency_projects_item_data.to_dict()
            dependency_projects.append(dependency_projects_item)

        post_processing = self.post_processing.to_dict()

        priority = self.priority

        status_changes = []
        for status_changes_item_data in self.status_changes:
            status_changes_item = status_changes_item_data.to_dict()
            status_changes.append(status_changes_item)

        publicly_visible = self.publicly_visible

        started: None | str | Unset
        if isinstance(self.started, Unset):
            started = UNSET
        elif isinstance(self.started, datetime.datetime):
            started = self.started.isoformat()
        else:
            started = self.started

        completed: None | str | Unset
        if isinstance(self.completed, Unset):
            completed = UNSET
        elif isinstance(self.completed, datetime.datetime):
            completed = self.completed.isoformat()
        else:
            completed = self.completed

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        number: int | None | Unset
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        override_hardware_tier_id: None | str | Unset
        if isinstance(self.override_hardware_tier_id, Unset):
            override_hardware_tier_id = UNSET
        else:
            override_hardware_tier_id = self.override_hardware_tier_id

        cents_per_minute: float | None | Unset
        if isinstance(self.cents_per_minute, Unset):
            cents_per_minute = UNSET
        else:
            cents_per_minute = self.cents_per_minute

        isolated_output_commit: bool | None | Unset
        if isinstance(self.isolated_output_commit, Unset):
            isolated_output_commit = UNSET
        else:
            isolated_output_commit = self.isolated_output_commit

        repositories: list[dict[str, Any]] | None | Unset
        if isinstance(self.repositories, Unset):
            repositories = UNSET
        elif isinstance(self.repositories, list):
            repositories = []
            for repositories_type_0_item_data in self.repositories:
                repositories_type_0_item = repositories_type_0_item_data.to_dict()
                repositories.append(repositories_type_0_item)

        else:
            repositories = self.repositories

        stop_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_request, Unset):
            stop_request = self.stop_request.to_dict()

        dataset_mounts: list[dict[str, Any]] | None | Unset
        if isinstance(self.dataset_mounts, Unset):
            dataset_mounts = UNSET
        elif isinstance(self.dataset_mounts, list):
            dataset_mounts = []
            for dataset_mounts_type_0_item_data in self.dataset_mounts:
                dataset_mounts_type_0_item = dataset_mounts_type_0_item_data.to_dict()
                dataset_mounts.append(dataset_mounts_type_0_item)

        else:
            dataset_mounts = self.dataset_mounts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queued": queued,
                "dependencyProjects": dependency_projects,
                "postProcessing": post_processing,
                "priority": priority,
                "statusChanges": status_changes,
                "publiclyVisible": publicly_visible,
            }
        )
        if started is not UNSET:
            field_dict["started"] = started
        if completed is not UNSET:
            field_dict["completed"] = completed
        if title is not UNSET:
            field_dict["title"] = title
        if number is not UNSET:
            field_dict["number"] = number
        if override_hardware_tier_id is not UNSET:
            field_dict["overrideHardwareTierId"] = override_hardware_tier_id
        if cents_per_minute is not UNSET:
            field_dict["centsPerMinute"] = cents_per_minute
        if isolated_output_commit is not UNSET:
            field_dict["isolatedOutputCommit"] = isolated_output_commit
        if repositories is not UNSET:
            field_dict["repositories"] = repositories
        if stop_request is not UNSET:
            field_dict["stopRequest"] = stop_request
        if dataset_mounts is not UNSET:
            field_dict["datasetMounts"] = dataset_mounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_gruz_api_dataset_mount import DominoGruzApiDatasetMount
        from ..models.domino_gruz_api_prepared_repository import DominoGruzApiPreparedRepository
        from ..models.domino_gruz_api_run_dependency_project import DominoGruzApiRunDependencyProject
        from ..models.domino_gruz_api_run_post_processing import DominoGruzApiRunPostProcessing
        from ..models.domino_gruz_api_status_change import DominoGruzApiStatusChange
        from ..models.domino_gruz_api_stop_request import DominoGruzApiStopRequest

        d = dict(src_dict)
        queued = isoparse(d.pop("queued"))

        dependency_projects = []
        _dependency_projects = d.pop("dependencyProjects")
        for dependency_projects_item_data in _dependency_projects:
            dependency_projects_item = DominoGruzApiRunDependencyProject.from_dict(dependency_projects_item_data)

            dependency_projects.append(dependency_projects_item)

        post_processing = DominoGruzApiRunPostProcessing.from_dict(d.pop("postProcessing"))

        priority = d.pop("priority")

        status_changes = []
        _status_changes = d.pop("statusChanges")
        for status_changes_item_data in _status_changes:
            status_changes_item = DominoGruzApiStatusChange.from_dict(status_changes_item_data)

            status_changes.append(status_changes_item)

        publicly_visible = d.pop("publiclyVisible")

        def _parse_started(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_type_0 = isoparse(data)

                return started_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started = _parse_started(d.pop("started", UNSET))

        def _parse_completed(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_type_0 = isoparse(data)

                return completed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed = _parse_completed(d.pop("completed", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_override_hardware_tier_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        override_hardware_tier_id = _parse_override_hardware_tier_id(d.pop("overrideHardwareTierId", UNSET))

        def _parse_cents_per_minute(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cents_per_minute = _parse_cents_per_minute(d.pop("centsPerMinute", UNSET))

        def _parse_isolated_output_commit(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        isolated_output_commit = _parse_isolated_output_commit(d.pop("isolatedOutputCommit", UNSET))

        def _parse_repositories(data: object) -> list[DominoGruzApiPreparedRepository] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                repositories_type_0 = []
                _repositories_type_0 = data
                for repositories_type_0_item_data in _repositories_type_0:
                    repositories_type_0_item = DominoGruzApiPreparedRepository.from_dict(repositories_type_0_item_data)

                    repositories_type_0.append(repositories_type_0_item)

                return repositories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoGruzApiPreparedRepository] | None | Unset, data)

        repositories = _parse_repositories(d.pop("repositories", UNSET))

        _stop_request = d.pop("stopRequest", UNSET)
        stop_request: DominoGruzApiStopRequest | Unset
        if isinstance(_stop_request, Unset):
            stop_request = UNSET
        else:
            stop_request = DominoGruzApiStopRequest.from_dict(_stop_request)

        def _parse_dataset_mounts(data: object) -> list[DominoGruzApiDatasetMount] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dataset_mounts_type_0 = []
                _dataset_mounts_type_0 = data
                for dataset_mounts_type_0_item_data in _dataset_mounts_type_0:
                    dataset_mounts_type_0_item = DominoGruzApiDatasetMount.from_dict(dataset_mounts_type_0_item_data)

                    dataset_mounts_type_0.append(dataset_mounts_type_0_item)

                return dataset_mounts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoGruzApiDatasetMount] | None | Unset, data)

        dataset_mounts = _parse_dataset_mounts(d.pop("datasetMounts", UNSET))

        domino_gruz_api_run_meta = cls(
            queued=queued,
            dependency_projects=dependency_projects,
            post_processing=post_processing,
            priority=priority,
            status_changes=status_changes,
            publicly_visible=publicly_visible,
            started=started,
            completed=completed,
            title=title,
            number=number,
            override_hardware_tier_id=override_hardware_tier_id,
            cents_per_minute=cents_per_minute,
            isolated_output_commit=isolated_output_commit,
            repositories=repositories,
            stop_request=stop_request,
            dataset_mounts=dataset_mounts,
        )

        domino_gruz_api_run_meta.additional_properties = d
        return domino_gruz_api_run_meta

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
