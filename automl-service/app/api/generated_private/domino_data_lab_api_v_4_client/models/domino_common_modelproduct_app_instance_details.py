from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_modelproduct_app_code_info_dto import DominoCommonModelproductAppCodeInfoDto
    from ..models.domino_common_modelproduct_app_external_volume_mount_specification import (
        DominoCommonModelproductAppExternalVolumeMountSpecification,
    )
    from ..models.domino_common_modelproduct_app_instance_autoscaling_details import (
        DominoCommonModelproductAppInstanceAutoscalingDetails,
    )
    from ..models.domino_common_modelproduct_app_net_app_volume_mount_specification import (
        DominoCommonModelproductAppNetAppVolumeMountSpecification,
    )
    from ..models.domino_common_modelproduct_app_resource_usage import DominoCommonModelproductAppResourceUsage
    from ..models.domino_common_modelproduct_environment_details import DominoCommonModelproductEnvironmentDetails
    from ..models.domino_common_modelproduct_executor_details import DominoCommonModelproductExecutorDetails


T = TypeVar("T", bound="DominoCommonModelproductAppInstanceDetails")


@_attrs_define
class DominoCommonModelproductAppInstanceDetails:
    """
    Attributes:
        id (str):
        started (int):
        input_commit_id (str):
        resource_usage (DominoCommonModelproductAppResourceUsage):
        hardware_tier_name (str):
        environment_details (DominoCommonModelproductEnvironmentDetails):
        external_volume_mounts (list[DominoCommonModelproductAppExternalVolumeMountSpecification]):
        net_app_volume_mounts (list[DominoCommonModelproductAppNetAppVolumeMountSpecification]):
        app_code_info (DominoCommonModelproductAppCodeInfoDto):
        status (str):
        output_commit_id (None | str | Unset):
        executor_details (DominoCommonModelproductExecutorDetails | Unset):
        autoscaling_details (DominoCommonModelproductAppInstanceAutoscalingDetails | Unset):
    """

    id: str
    started: int
    input_commit_id: str
    resource_usage: DominoCommonModelproductAppResourceUsage
    hardware_tier_name: str
    environment_details: DominoCommonModelproductEnvironmentDetails
    external_volume_mounts: list[DominoCommonModelproductAppExternalVolumeMountSpecification]
    net_app_volume_mounts: list[DominoCommonModelproductAppNetAppVolumeMountSpecification]
    app_code_info: DominoCommonModelproductAppCodeInfoDto
    status: str
    output_commit_id: None | str | Unset = UNSET
    executor_details: DominoCommonModelproductExecutorDetails | Unset = UNSET
    autoscaling_details: DominoCommonModelproductAppInstanceAutoscalingDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        started = self.started

        input_commit_id = self.input_commit_id

        resource_usage = self.resource_usage.to_dict()

        hardware_tier_name = self.hardware_tier_name

        environment_details = self.environment_details.to_dict()

        external_volume_mounts = []
        for external_volume_mounts_item_data in self.external_volume_mounts:
            external_volume_mounts_item = external_volume_mounts_item_data.to_dict()
            external_volume_mounts.append(external_volume_mounts_item)

        net_app_volume_mounts = []
        for net_app_volume_mounts_item_data in self.net_app_volume_mounts:
            net_app_volume_mounts_item = net_app_volume_mounts_item_data.to_dict()
            net_app_volume_mounts.append(net_app_volume_mounts_item)

        app_code_info = self.app_code_info.to_dict()

        status = self.status

        output_commit_id: None | str | Unset
        if isinstance(self.output_commit_id, Unset):
            output_commit_id = UNSET
        else:
            output_commit_id = self.output_commit_id

        executor_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.executor_details, Unset):
            executor_details = self.executor_details.to_dict()

        autoscaling_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.autoscaling_details, Unset):
            autoscaling_details = self.autoscaling_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "started": started,
                "inputCommitId": input_commit_id,
                "resourceUsage": resource_usage,
                "hardwareTierName": hardware_tier_name,
                "environmentDetails": environment_details,
                "externalVolumeMounts": external_volume_mounts,
                "netAppVolumeMounts": net_app_volume_mounts,
                "appCodeInfo": app_code_info,
                "status": status,
            }
        )
        if output_commit_id is not UNSET:
            field_dict["outputCommitId"] = output_commit_id
        if executor_details is not UNSET:
            field_dict["executorDetails"] = executor_details
        if autoscaling_details is not UNSET:
            field_dict["autoscalingDetails"] = autoscaling_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_modelproduct_app_code_info_dto import DominoCommonModelproductAppCodeInfoDto
        from ..models.domino_common_modelproduct_app_external_volume_mount_specification import (
            DominoCommonModelproductAppExternalVolumeMountSpecification,
        )
        from ..models.domino_common_modelproduct_app_instance_autoscaling_details import (
            DominoCommonModelproductAppInstanceAutoscalingDetails,
        )
        from ..models.domino_common_modelproduct_app_net_app_volume_mount_specification import (
            DominoCommonModelproductAppNetAppVolumeMountSpecification,
        )
        from ..models.domino_common_modelproduct_app_resource_usage import DominoCommonModelproductAppResourceUsage
        from ..models.domino_common_modelproduct_environment_details import DominoCommonModelproductEnvironmentDetails
        from ..models.domino_common_modelproduct_executor_details import DominoCommonModelproductExecutorDetails

        d = dict(src_dict)
        id = d.pop("id")

        started = d.pop("started")

        input_commit_id = d.pop("inputCommitId")

        resource_usage = DominoCommonModelproductAppResourceUsage.from_dict(d.pop("resourceUsage"))

        hardware_tier_name = d.pop("hardwareTierName")

        environment_details = DominoCommonModelproductEnvironmentDetails.from_dict(d.pop("environmentDetails"))

        external_volume_mounts = []
        _external_volume_mounts = d.pop("externalVolumeMounts")
        for external_volume_mounts_item_data in _external_volume_mounts:
            external_volume_mounts_item = DominoCommonModelproductAppExternalVolumeMountSpecification.from_dict(
                external_volume_mounts_item_data
            )

            external_volume_mounts.append(external_volume_mounts_item)

        net_app_volume_mounts = []
        _net_app_volume_mounts = d.pop("netAppVolumeMounts")
        for net_app_volume_mounts_item_data in _net_app_volume_mounts:
            net_app_volume_mounts_item = DominoCommonModelproductAppNetAppVolumeMountSpecification.from_dict(
                net_app_volume_mounts_item_data
            )

            net_app_volume_mounts.append(net_app_volume_mounts_item)

        app_code_info = DominoCommonModelproductAppCodeInfoDto.from_dict(d.pop("appCodeInfo"))

        status = d.pop("status")

        def _parse_output_commit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output_commit_id = _parse_output_commit_id(d.pop("outputCommitId", UNSET))

        _executor_details = d.pop("executorDetails", UNSET)
        executor_details: DominoCommonModelproductExecutorDetails | Unset
        if isinstance(_executor_details, Unset):
            executor_details = UNSET
        else:
            executor_details = DominoCommonModelproductExecutorDetails.from_dict(_executor_details)

        _autoscaling_details = d.pop("autoscalingDetails", UNSET)
        autoscaling_details: DominoCommonModelproductAppInstanceAutoscalingDetails | Unset
        if isinstance(_autoscaling_details, Unset):
            autoscaling_details = UNSET
        else:
            autoscaling_details = DominoCommonModelproductAppInstanceAutoscalingDetails.from_dict(_autoscaling_details)

        domino_common_modelproduct_app_instance_details = cls(
            id=id,
            started=started,
            input_commit_id=input_commit_id,
            resource_usage=resource_usage,
            hardware_tier_name=hardware_tier_name,
            environment_details=environment_details,
            external_volume_mounts=external_volume_mounts,
            net_app_volume_mounts=net_app_volume_mounts,
            app_code_info=app_code_info,
            status=status,
            output_commit_id=output_commit_id,
            executor_details=executor_details,
            autoscaling_details=autoscaling_details,
        )

        domino_common_modelproduct_app_instance_details.additional_properties = d
        return domino_common_modelproduct_app_instance_details

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
