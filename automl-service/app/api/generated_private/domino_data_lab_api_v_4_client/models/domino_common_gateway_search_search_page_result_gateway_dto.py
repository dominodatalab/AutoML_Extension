from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_gateway_search_feature_view_search_result_dto import (
        DominoCommonGatewaySearchFeatureViewSearchResultDTO,
    )
    from ..models.domino_common_gateway_search_search_comment_dto import DominoCommonGatewaySearchSearchCommentDTO
    from ..models.domino_common_gateway_search_search_dataset_dto import DominoCommonGatewaySearchSearchDatasetDTO
    from ..models.domino_common_gateway_search_search_environment_dto import (
        DominoCommonGatewaySearchSearchEnvironmentDTO,
    )
    from ..models.domino_common_gateway_search_search_file_dto import DominoCommonGatewaySearchSearchFileDTO
    from ..models.domino_common_gateway_search_search_model_dto import DominoCommonGatewaySearchSearchModelDTO
    from ..models.domino_common_gateway_search_search_project_dto import DominoCommonGatewaySearchSearchProjectDTO
    from ..models.domino_common_gateway_search_search_run_dto import DominoCommonGatewaySearchSearchRunDTO


T = TypeVar("T", bound="DominoCommonGatewaySearchSearchPageResultGatewayDTO")


@_attrs_define
class DominoCommonGatewaySearchSearchPageResultGatewayDTO:
    """
    Attributes:
        link (str):
        area (str):
        id (None | str | Unset):
        project_id (None | str | Unset):
        display_text (None | str | Unset):
        owner_id (None | str | Unset):
        path (None | str | Unset):
        feature_view_info (DominoCommonGatewaySearchFeatureViewSearchResultDTO | Unset):
        project_info (DominoCommonGatewaySearchSearchProjectDTO | Unset):
        model_info (DominoCommonGatewaySearchSearchModelDTO | Unset):
        environment_info (DominoCommonGatewaySearchSearchEnvironmentDTO | Unset):
        comment_info (DominoCommonGatewaySearchSearchCommentDTO | Unset):
        run_info (DominoCommonGatewaySearchSearchRunDTO | Unset):
        dataset_info (DominoCommonGatewaySearchSearchDatasetDTO | Unset):
        file_info (DominoCommonGatewaySearchSearchFileDTO | Unset):
    """

    link: str
    area: str
    id: None | str | Unset = UNSET
    project_id: None | str | Unset = UNSET
    display_text: None | str | Unset = UNSET
    owner_id: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    feature_view_info: DominoCommonGatewaySearchFeatureViewSearchResultDTO | Unset = UNSET
    project_info: DominoCommonGatewaySearchSearchProjectDTO | Unset = UNSET
    model_info: DominoCommonGatewaySearchSearchModelDTO | Unset = UNSET
    environment_info: DominoCommonGatewaySearchSearchEnvironmentDTO | Unset = UNSET
    comment_info: DominoCommonGatewaySearchSearchCommentDTO | Unset = UNSET
    run_info: DominoCommonGatewaySearchSearchRunDTO | Unset = UNSET
    dataset_info: DominoCommonGatewaySearchSearchDatasetDTO | Unset = UNSET
    file_info: DominoCommonGatewaySearchSearchFileDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        link = self.link

        area = self.area

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        display_text: None | str | Unset
        if isinstance(self.display_text, Unset):
            display_text = UNSET
        else:
            display_text = self.display_text

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        feature_view_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_view_info, Unset):
            feature_view_info = self.feature_view_info.to_dict()

        project_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_info, Unset):
            project_info = self.project_info.to_dict()

        model_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_info, Unset):
            model_info = self.model_info.to_dict()

        environment_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.environment_info, Unset):
            environment_info = self.environment_info.to_dict()

        comment_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comment_info, Unset):
            comment_info = self.comment_info.to_dict()

        run_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.run_info, Unset):
            run_info = self.run_info.to_dict()

        dataset_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dataset_info, Unset):
            dataset_info = self.dataset_info.to_dict()

        file_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_info, Unset):
            file_info = self.file_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "link": link,
                "area": area,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if display_text is not UNSET:
            field_dict["displayText"] = display_text
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if path is not UNSET:
            field_dict["path"] = path
        if feature_view_info is not UNSET:
            field_dict["featureViewInfo"] = feature_view_info
        if project_info is not UNSET:
            field_dict["projectInfo"] = project_info
        if model_info is not UNSET:
            field_dict["modelInfo"] = model_info
        if environment_info is not UNSET:
            field_dict["environmentInfo"] = environment_info
        if comment_info is not UNSET:
            field_dict["commentInfo"] = comment_info
        if run_info is not UNSET:
            field_dict["runInfo"] = run_info
        if dataset_info is not UNSET:
            field_dict["datasetInfo"] = dataset_info
        if file_info is not UNSET:
            field_dict["fileInfo"] = file_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_gateway_search_feature_view_search_result_dto import (
            DominoCommonGatewaySearchFeatureViewSearchResultDTO,
        )
        from ..models.domino_common_gateway_search_search_comment_dto import DominoCommonGatewaySearchSearchCommentDTO
        from ..models.domino_common_gateway_search_search_dataset_dto import DominoCommonGatewaySearchSearchDatasetDTO
        from ..models.domino_common_gateway_search_search_environment_dto import (
            DominoCommonGatewaySearchSearchEnvironmentDTO,
        )
        from ..models.domino_common_gateway_search_search_file_dto import DominoCommonGatewaySearchSearchFileDTO
        from ..models.domino_common_gateway_search_search_model_dto import DominoCommonGatewaySearchSearchModelDTO
        from ..models.domino_common_gateway_search_search_project_dto import DominoCommonGatewaySearchSearchProjectDTO
        from ..models.domino_common_gateway_search_search_run_dto import DominoCommonGatewaySearchSearchRunDTO

        d = dict(src_dict)
        link = d.pop("link")

        area = d.pop("area")

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("projectId", UNSET))

        def _parse_display_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_text = _parse_display_text(d.pop("displayText", UNSET))

        def _parse_owner_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_id = _parse_owner_id(d.pop("ownerId", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        _feature_view_info = d.pop("featureViewInfo", UNSET)
        feature_view_info: DominoCommonGatewaySearchFeatureViewSearchResultDTO | Unset
        if isinstance(_feature_view_info, Unset):
            feature_view_info = UNSET
        else:
            feature_view_info = DominoCommonGatewaySearchFeatureViewSearchResultDTO.from_dict(_feature_view_info)

        _project_info = d.pop("projectInfo", UNSET)
        project_info: DominoCommonGatewaySearchSearchProjectDTO | Unset
        if isinstance(_project_info, Unset):
            project_info = UNSET
        else:
            project_info = DominoCommonGatewaySearchSearchProjectDTO.from_dict(_project_info)

        _model_info = d.pop("modelInfo", UNSET)
        model_info: DominoCommonGatewaySearchSearchModelDTO | Unset
        if isinstance(_model_info, Unset):
            model_info = UNSET
        else:
            model_info = DominoCommonGatewaySearchSearchModelDTO.from_dict(_model_info)

        _environment_info = d.pop("environmentInfo", UNSET)
        environment_info: DominoCommonGatewaySearchSearchEnvironmentDTO | Unset
        if isinstance(_environment_info, Unset):
            environment_info = UNSET
        else:
            environment_info = DominoCommonGatewaySearchSearchEnvironmentDTO.from_dict(_environment_info)

        _comment_info = d.pop("commentInfo", UNSET)
        comment_info: DominoCommonGatewaySearchSearchCommentDTO | Unset
        if isinstance(_comment_info, Unset):
            comment_info = UNSET
        else:
            comment_info = DominoCommonGatewaySearchSearchCommentDTO.from_dict(_comment_info)

        _run_info = d.pop("runInfo", UNSET)
        run_info: DominoCommonGatewaySearchSearchRunDTO | Unset
        if isinstance(_run_info, Unset):
            run_info = UNSET
        else:
            run_info = DominoCommonGatewaySearchSearchRunDTO.from_dict(_run_info)

        _dataset_info = d.pop("datasetInfo", UNSET)
        dataset_info: DominoCommonGatewaySearchSearchDatasetDTO | Unset
        if isinstance(_dataset_info, Unset):
            dataset_info = UNSET
        else:
            dataset_info = DominoCommonGatewaySearchSearchDatasetDTO.from_dict(_dataset_info)

        _file_info = d.pop("fileInfo", UNSET)
        file_info: DominoCommonGatewaySearchSearchFileDTO | Unset
        if isinstance(_file_info, Unset):
            file_info = UNSET
        else:
            file_info = DominoCommonGatewaySearchSearchFileDTO.from_dict(_file_info)

        domino_common_gateway_search_search_page_result_gateway_dto = cls(
            link=link,
            area=area,
            id=id,
            project_id=project_id,
            display_text=display_text,
            owner_id=owner_id,
            path=path,
            feature_view_info=feature_view_info,
            project_info=project_info,
            model_info=model_info,
            environment_info=environment_info,
            comment_info=comment_info,
            run_info=run_info,
            dataset_info=dataset_info,
            file_info=file_info,
        )

        domino_common_gateway_search_search_page_result_gateway_dto.additional_properties = d
        return domino_common_gateway_search_search_page_result_gateway_dto

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
