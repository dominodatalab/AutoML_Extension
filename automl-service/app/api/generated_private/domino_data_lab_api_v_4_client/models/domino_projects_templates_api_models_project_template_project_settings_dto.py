from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_templates_api_models_project_template_goal_stages_dto import (
        DominoProjectsTemplatesApiModelsProjectTemplateGoalStagesDto,
    )


T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsProjectTemplateProjectSettingsDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsProjectTemplateProjectSettingsDto:
    """
    Attributes:
        require_commit_message (bool | None | Unset):
        require_e_signature_workflow (bool | None | Unset):
        project_goal_stages (list[DominoProjectsTemplatesApiModelsProjectTemplateGoalStagesDto] | None | Unset):
    """

    require_commit_message: bool | None | Unset = UNSET
    require_e_signature_workflow: bool | None | Unset = UNSET
    project_goal_stages: list[DominoProjectsTemplatesApiModelsProjectTemplateGoalStagesDto] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        require_commit_message: bool | None | Unset
        if isinstance(self.require_commit_message, Unset):
            require_commit_message = UNSET
        else:
            require_commit_message = self.require_commit_message

        require_e_signature_workflow: bool | None | Unset
        if isinstance(self.require_e_signature_workflow, Unset):
            require_e_signature_workflow = UNSET
        else:
            require_e_signature_workflow = self.require_e_signature_workflow

        project_goal_stages: list[dict[str, Any]] | None | Unset
        if isinstance(self.project_goal_stages, Unset):
            project_goal_stages = UNSET
        elif isinstance(self.project_goal_stages, list):
            project_goal_stages = []
            for project_goal_stages_type_0_item_data in self.project_goal_stages:
                project_goal_stages_type_0_item = project_goal_stages_type_0_item_data.to_dict()
                project_goal_stages.append(project_goal_stages_type_0_item)

        else:
            project_goal_stages = self.project_goal_stages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if require_commit_message is not UNSET:
            field_dict["requireCommitMessage"] = require_commit_message
        if require_e_signature_workflow is not UNSET:
            field_dict["requireESignatureWorkflow"] = require_e_signature_workflow
        if project_goal_stages is not UNSET:
            field_dict["projectGoalStages"] = project_goal_stages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_templates_api_models_project_template_goal_stages_dto import (
            DominoProjectsTemplatesApiModelsProjectTemplateGoalStagesDto,
        )

        d = dict(src_dict)

        def _parse_require_commit_message(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        require_commit_message = _parse_require_commit_message(d.pop("requireCommitMessage", UNSET))

        def _parse_require_e_signature_workflow(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        require_e_signature_workflow = _parse_require_e_signature_workflow(d.pop("requireESignatureWorkflow", UNSET))

        def _parse_project_goal_stages(
            data: object,
        ) -> list[DominoProjectsTemplatesApiModelsProjectTemplateGoalStagesDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                project_goal_stages_type_0 = []
                _project_goal_stages_type_0 = data
                for project_goal_stages_type_0_item_data in _project_goal_stages_type_0:
                    project_goal_stages_type_0_item = (
                        DominoProjectsTemplatesApiModelsProjectTemplateGoalStagesDto.from_dict(
                            project_goal_stages_type_0_item_data
                        )
                    )

                    project_goal_stages_type_0.append(project_goal_stages_type_0_item)

                return project_goal_stages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoProjectsTemplatesApiModelsProjectTemplateGoalStagesDto] | None | Unset, data)

        project_goal_stages = _parse_project_goal_stages(d.pop("projectGoalStages", UNSET))

        domino_projects_templates_api_models_project_template_project_settings_dto = cls(
            require_commit_message=require_commit_message,
            require_e_signature_workflow=require_e_signature_workflow,
            project_goal_stages=project_goal_stages,
        )

        domino_projects_templates_api_models_project_template_project_settings_dto.additional_properties = d
        return domino_projects_templates_api_models_project_template_project_settings_dto

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
