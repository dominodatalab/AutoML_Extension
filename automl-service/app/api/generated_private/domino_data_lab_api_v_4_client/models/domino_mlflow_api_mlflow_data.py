from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_mlflow_api_mlflow_data_mlflow_source_type import DominoMlflowApiMlflowDataMlflowSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasource_api_data_source_accessed_info import DominoDatasourceApiDataSourceAccessedInfo
    from ..models.domino_mlflow_api_mlflow_app_info import DominoMlflowApiMlflowAppInfo
    from ..models.domino_provenance_api_provenance_checkpoint_dto import DominoProvenanceApiProvenanceCheckpointDto


T = TypeVar("T", bound="DominoMlflowApiMlflowData")


@_attrs_define
class DominoMlflowApiMlflowData:
    """
    Attributes:
        project_id (str):
        execution_id (str):
        project_name (str):
        environment_id (str):
        environment_revision_id (str):
        hardware_tier_id (str):
        mlflow_source_type (DominoMlflowApiMlflowDataMlflowSourceType):
        run_number (int):
        dataset_info (str):
        data_sources (str):
        accessed_data_sources (list[DominoDatasourceApiDataSourceAccessedInfo]):
        latest_checkpoint (DominoProvenanceApiProvenanceCheckpointDto | Unset):
        app (DominoMlflowApiMlflowAppInfo | Unset):
    """

    project_id: str
    execution_id: str
    project_name: str
    environment_id: str
    environment_revision_id: str
    hardware_tier_id: str
    mlflow_source_type: DominoMlflowApiMlflowDataMlflowSourceType
    run_number: int
    dataset_info: str
    data_sources: str
    accessed_data_sources: list[DominoDatasourceApiDataSourceAccessedInfo]
    latest_checkpoint: DominoProvenanceApiProvenanceCheckpointDto | Unset = UNSET
    app: DominoMlflowApiMlflowAppInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        execution_id = self.execution_id

        project_name = self.project_name

        environment_id = self.environment_id

        environment_revision_id = self.environment_revision_id

        hardware_tier_id = self.hardware_tier_id

        mlflow_source_type = self.mlflow_source_type.value

        run_number = self.run_number

        dataset_info = self.dataset_info

        data_sources = self.data_sources

        accessed_data_sources = []
        for accessed_data_sources_item_data in self.accessed_data_sources:
            accessed_data_sources_item = accessed_data_sources_item_data.to_dict()
            accessed_data_sources.append(accessed_data_sources_item)

        latest_checkpoint: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest_checkpoint, Unset):
            latest_checkpoint = self.latest_checkpoint.to_dict()

        app: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app, Unset):
            app = self.app.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "executionId": execution_id,
                "projectName": project_name,
                "environmentId": environment_id,
                "environmentRevisionId": environment_revision_id,
                "hardwareTierId": hardware_tier_id,
                "mlflowSourceType": mlflow_source_type,
                "runNumber": run_number,
                "datasetInfo": dataset_info,
                "dataSources": data_sources,
                "accessedDataSources": accessed_data_sources,
            }
        )
        if latest_checkpoint is not UNSET:
            field_dict["latestCheckpoint"] = latest_checkpoint
        if app is not UNSET:
            field_dict["app"] = app

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasource_api_data_source_accessed_info import DominoDatasourceApiDataSourceAccessedInfo
        from ..models.domino_mlflow_api_mlflow_app_info import DominoMlflowApiMlflowAppInfo
        from ..models.domino_provenance_api_provenance_checkpoint_dto import DominoProvenanceApiProvenanceCheckpointDto

        d = dict(src_dict)
        project_id = d.pop("projectId")

        execution_id = d.pop("executionId")

        project_name = d.pop("projectName")

        environment_id = d.pop("environmentId")

        environment_revision_id = d.pop("environmentRevisionId")

        hardware_tier_id = d.pop("hardwareTierId")

        mlflow_source_type = DominoMlflowApiMlflowDataMlflowSourceType(d.pop("mlflowSourceType"))

        run_number = d.pop("runNumber")

        dataset_info = d.pop("datasetInfo")

        data_sources = d.pop("dataSources")

        accessed_data_sources = []
        _accessed_data_sources = d.pop("accessedDataSources")
        for accessed_data_sources_item_data in _accessed_data_sources:
            accessed_data_sources_item = DominoDatasourceApiDataSourceAccessedInfo.from_dict(
                accessed_data_sources_item_data
            )

            accessed_data_sources.append(accessed_data_sources_item)

        _latest_checkpoint = d.pop("latestCheckpoint", UNSET)
        latest_checkpoint: DominoProvenanceApiProvenanceCheckpointDto | Unset
        if isinstance(_latest_checkpoint, Unset):
            latest_checkpoint = UNSET
        else:
            latest_checkpoint = DominoProvenanceApiProvenanceCheckpointDto.from_dict(_latest_checkpoint)

        _app = d.pop("app", UNSET)
        app: DominoMlflowApiMlflowAppInfo | Unset
        if isinstance(_app, Unset):
            app = UNSET
        else:
            app = DominoMlflowApiMlflowAppInfo.from_dict(_app)

        domino_mlflow_api_mlflow_data = cls(
            project_id=project_id,
            execution_id=execution_id,
            project_name=project_name,
            environment_id=environment_id,
            environment_revision_id=environment_revision_id,
            hardware_tier_id=hardware_tier_id,
            mlflow_source_type=mlflow_source_type,
            run_number=run_number,
            dataset_info=dataset_info,
            data_sources=data_sources,
            accessed_data_sources=accessed_data_sources,
            latest_checkpoint=latest_checkpoint,
            app=app,
        )

        domino_mlflow_api_mlflow_data.additional_properties = d
        return domino_mlflow_api_mlflow_data

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
