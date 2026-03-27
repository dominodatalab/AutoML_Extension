from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_activity_api_all_model_reviewers_approved_metadata import (
        DominoActivityApiAllModelReviewersApprovedMetadata,
    )
    from ..models.domino_activity_api_app_status_activity_meta_data import DominoActivityApiAppStatusActivityMetaData
    from ..models.domino_activity_api_comment_activity_meta_data import DominoActivityApiCommentActivityMetaData
    from ..models.domino_activity_api_commented_on_bundle_meta_data import DominoActivityApiCommentedOnBundleMetaData
    from ..models.domino_activity_api_commented_on_file_meta_data import DominoActivityApiCommentedOnFileMetaData
    from ..models.domino_activity_api_commented_on_job_meta_data import DominoActivityApiCommentedOnJobMetaData
    from ..models.domino_activity_api_commented_on_project_goal_meta_data import (
        DominoActivityApiCommentedOnProjectGoalMetaData,
    )
    from ..models.domino_activity_api_commented_on_workspace_meta_data import (
        DominoActivityApiCommentedOnWorkspaceMetaData,
    )
    from ..models.domino_activity_api_file_change_activity_meta_data import DominoActivityApiFileChangeActivityMetaData
    from ..models.domino_activity_api_job_status_activity_meta_data import DominoActivityApiJobStatusActivityMetaData
    from ..models.domino_activity_api_model_review_activity_with_notes_metadata import (
        DominoActivityApiModelReviewActivityWithNotesMetadata,
    )
    from ..models.domino_activity_api_model_version_status_activity_meta_data import (
        DominoActivityApiModelVersionStatusActivityMetaData,
    )
    from ..models.domino_activity_api_project_goal_app_link_activity_metadata import (
        DominoActivityApiProjectGoalAppLinkActivityMetadata,
    )
    from ..models.domino_activity_api_project_goal_assignment_change_activity_metadata import (
        DominoActivityApiProjectGoalAssignmentChangeActivityMetadata,
    )
    from ..models.domino_activity_api_project_goal_bulk_delete_activity_metadata import (
        DominoActivityApiProjectGoalBulkDeleteActivityMetadata,
    )
    from ..models.domino_activity_api_project_goal_bulk_update_activity_metadata import (
        DominoActivityApiProjectGoalBulkUpdateActivityMetadata,
    )
    from ..models.domino_activity_api_project_goal_create_activity_metadata import (
        DominoActivityApiProjectGoalCreateActivityMetadata,
    )
    from ..models.domino_activity_api_project_goal_file_link_activity_metadata import (
        DominoActivityApiProjectGoalFileLinkActivityMetadata,
    )
    from ..models.domino_activity_api_project_goal_job_link_activity_metadata import (
        DominoActivityApiProjectGoalJobLinkActivityMetadata,
    )
    from ..models.domino_activity_api_project_goal_model_link_activity_metadata import (
        DominoActivityApiProjectGoalModelLinkActivityMetadata,
    )
    from ..models.domino_activity_api_project_goal_stage_change_activity_metadata import (
        DominoActivityApiProjectGoalStageChangeActivityMetadata,
    )
    from ..models.domino_activity_api_project_goal_status_change_activity_metadata import (
        DominoActivityApiProjectGoalStatusChangeActivityMetadata,
    )
    from ..models.domino_activity_api_project_goal_update_description_activity_metadata import (
        DominoActivityApiProjectGoalUpdateDescriptionActivityMetadata,
    )
    from ..models.domino_activity_api_project_goal_update_title_activity_metadata import (
        DominoActivityApiProjectGoalUpdateTitleActivityMetadata,
    )
    from ..models.domino_activity_api_project_goal_workspace_link_activity_metadata import (
        DominoActivityApiProjectGoalWorkspaceLinkActivityMetadata,
    )
    from ..models.domino_activity_api_project_link_change_activity_metadata import (
        DominoActivityApiProjectLinkChangeActivityMetadata,
    )
    from ..models.domino_activity_api_project_stage_change_activity_meta_data import (
        DominoActivityApiProjectStageChangeActivityMetaData,
    )
    from ..models.domino_activity_api_project_status_change_activity_meta_data import (
        DominoActivityApiProjectStatusChangeActivityMetaData,
    )
    from ..models.domino_activity_api_registered_model_stage_transitioned_metadata import (
        DominoActivityApiRegisteredModelStageTransitionedMetadata,
    )
    from ..models.domino_activity_api_schedule_job_activity_meta_data import (
        DominoActivityApiScheduleJobActivityMetaData,
    )
    from ..models.domino_activity_api_schedule_job_edit_activity_meta_data import (
        DominoActivityApiScheduleJobEditActivityMetaData,
    )
    from ..models.domino_activity_api_workspace_status_activity_meta_data import (
        DominoActivityApiWorkspaceStatusActivityMetaData,
    )


T = TypeVar("T", bound="DominoActivityApiAllMetadata")


@_attrs_define
class DominoActivityApiAllMetadata:
    """
    Attributes:
        job_status_activity_meta_data (DominoActivityApiJobStatusActivityMetaData):
        workspace_status_activity_meta_data (DominoActivityApiWorkspaceStatusActivityMetaData):
        comment_activity_meta_data (DominoActivityApiCommentActivityMetaData):
        commented_on_job_meta_data (DominoActivityApiCommentedOnJobMetaData):
        commented_on_workspace_meta_data (DominoActivityApiCommentedOnWorkspaceMetaData):
        commented_on_file_meta_data (DominoActivityApiCommentedOnFileMetaData):
        commented_on_project_goal_meta_data (DominoActivityApiCommentedOnProjectGoalMetaData):
        commented_on_bundle_meta_data (DominoActivityApiCommentedOnBundleMetaData):
        project_stage_change_activity_meta_data (DominoActivityApiProjectStageChangeActivityMetaData):
        project_status_change_activity_meta_data (DominoActivityApiProjectStatusChangeActivityMetaData):
        app_status_activity_meta_data (DominoActivityApiAppStatusActivityMetaData):
        model_version_status_activity_meta_data (DominoActivityApiModelVersionStatusActivityMetaData):
        schedule_job_activity_meta_data (DominoActivityApiScheduleJobActivityMetaData):
        schedule_job_edit_activity_meta_data (DominoActivityApiScheduleJobEditActivityMetaData):
        file_change_activity_meta_data (DominoActivityApiFileChangeActivityMetaData):
        project_goal_create_activity_metadata (DominoActivityApiProjectGoalCreateActivityMetadata):
        project_goal_status_change_activity_metadata (DominoActivityApiProjectGoalStatusChangeActivityMetadata):
        project_goal_stage_change_activity_meta_data (DominoActivityApiProjectGoalStageChangeActivityMetadata):
        project_goal_assignment_change_activity_metadata (DominoActivityApiProjectGoalAssignmentChangeActivityMetadata):
        project_goal_update_title_activity_metadata (DominoActivityApiProjectGoalUpdateTitleActivityMetadata):
        project_goal_update_description_activity_metadata
            (DominoActivityApiProjectGoalUpdateDescriptionActivityMetadata):
        project_goal_file_link_activity_metadata (DominoActivityApiProjectGoalFileLinkActivityMetadata):
        project_goal_job_link_activity_metadata (DominoActivityApiProjectGoalJobLinkActivityMetadata):
        project_goal_workspace_link_activity_metadata (DominoActivityApiProjectGoalWorkspaceLinkActivityMetadata):
        project_goal_app_link_activity_metadata (DominoActivityApiProjectGoalAppLinkActivityMetadata):
        project_goal_model_link_activity_metadata (DominoActivityApiProjectGoalModelLinkActivityMetadata):
        project_link_change_activity_metadata (DominoActivityApiProjectLinkChangeActivityMetadata):
        model_review_activity_with_notes_metadata (DominoActivityApiModelReviewActivityWithNotesMetadata):
        all_model_reviewers_approved_metadata (DominoActivityApiAllModelReviewersApprovedMetadata):
        registered_model_stage_transitioned_metadata (DominoActivityApiRegisteredModelStageTransitionedMetadata):
        project_goal_bulk_update_activity_metadata (DominoActivityApiProjectGoalBulkUpdateActivityMetadata):
        project_goal_bulk_delete_activity_metadata (DominoActivityApiProjectGoalBulkDeleteActivityMetadata):
    """

    job_status_activity_meta_data: DominoActivityApiJobStatusActivityMetaData
    workspace_status_activity_meta_data: DominoActivityApiWorkspaceStatusActivityMetaData
    comment_activity_meta_data: DominoActivityApiCommentActivityMetaData
    commented_on_job_meta_data: DominoActivityApiCommentedOnJobMetaData
    commented_on_workspace_meta_data: DominoActivityApiCommentedOnWorkspaceMetaData
    commented_on_file_meta_data: DominoActivityApiCommentedOnFileMetaData
    commented_on_project_goal_meta_data: DominoActivityApiCommentedOnProjectGoalMetaData
    commented_on_bundle_meta_data: DominoActivityApiCommentedOnBundleMetaData
    project_stage_change_activity_meta_data: DominoActivityApiProjectStageChangeActivityMetaData
    project_status_change_activity_meta_data: DominoActivityApiProjectStatusChangeActivityMetaData
    app_status_activity_meta_data: DominoActivityApiAppStatusActivityMetaData
    model_version_status_activity_meta_data: DominoActivityApiModelVersionStatusActivityMetaData
    schedule_job_activity_meta_data: DominoActivityApiScheduleJobActivityMetaData
    schedule_job_edit_activity_meta_data: DominoActivityApiScheduleJobEditActivityMetaData
    file_change_activity_meta_data: DominoActivityApiFileChangeActivityMetaData
    project_goal_create_activity_metadata: DominoActivityApiProjectGoalCreateActivityMetadata
    project_goal_status_change_activity_metadata: DominoActivityApiProjectGoalStatusChangeActivityMetadata
    project_goal_stage_change_activity_meta_data: DominoActivityApiProjectGoalStageChangeActivityMetadata
    project_goal_assignment_change_activity_metadata: DominoActivityApiProjectGoalAssignmentChangeActivityMetadata
    project_goal_update_title_activity_metadata: DominoActivityApiProjectGoalUpdateTitleActivityMetadata
    project_goal_update_description_activity_metadata: DominoActivityApiProjectGoalUpdateDescriptionActivityMetadata
    project_goal_file_link_activity_metadata: DominoActivityApiProjectGoalFileLinkActivityMetadata
    project_goal_job_link_activity_metadata: DominoActivityApiProjectGoalJobLinkActivityMetadata
    project_goal_workspace_link_activity_metadata: DominoActivityApiProjectGoalWorkspaceLinkActivityMetadata
    project_goal_app_link_activity_metadata: DominoActivityApiProjectGoalAppLinkActivityMetadata
    project_goal_model_link_activity_metadata: DominoActivityApiProjectGoalModelLinkActivityMetadata
    project_link_change_activity_metadata: DominoActivityApiProjectLinkChangeActivityMetadata
    model_review_activity_with_notes_metadata: DominoActivityApiModelReviewActivityWithNotesMetadata
    all_model_reviewers_approved_metadata: DominoActivityApiAllModelReviewersApprovedMetadata
    registered_model_stage_transitioned_metadata: DominoActivityApiRegisteredModelStageTransitionedMetadata
    project_goal_bulk_update_activity_metadata: DominoActivityApiProjectGoalBulkUpdateActivityMetadata
    project_goal_bulk_delete_activity_metadata: DominoActivityApiProjectGoalBulkDeleteActivityMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_status_activity_meta_data = self.job_status_activity_meta_data.to_dict()

        workspace_status_activity_meta_data = self.workspace_status_activity_meta_data.to_dict()

        comment_activity_meta_data = self.comment_activity_meta_data.to_dict()

        commented_on_job_meta_data = self.commented_on_job_meta_data.to_dict()

        commented_on_workspace_meta_data = self.commented_on_workspace_meta_data.to_dict()

        commented_on_file_meta_data = self.commented_on_file_meta_data.to_dict()

        commented_on_project_goal_meta_data = self.commented_on_project_goal_meta_data.to_dict()

        commented_on_bundle_meta_data = self.commented_on_bundle_meta_data.to_dict()

        project_stage_change_activity_meta_data = self.project_stage_change_activity_meta_data.to_dict()

        project_status_change_activity_meta_data = self.project_status_change_activity_meta_data.to_dict()

        app_status_activity_meta_data = self.app_status_activity_meta_data.to_dict()

        model_version_status_activity_meta_data = self.model_version_status_activity_meta_data.to_dict()

        schedule_job_activity_meta_data = self.schedule_job_activity_meta_data.to_dict()

        schedule_job_edit_activity_meta_data = self.schedule_job_edit_activity_meta_data.to_dict()

        file_change_activity_meta_data = self.file_change_activity_meta_data.to_dict()

        project_goal_create_activity_metadata = self.project_goal_create_activity_metadata.to_dict()

        project_goal_status_change_activity_metadata = self.project_goal_status_change_activity_metadata.to_dict()

        project_goal_stage_change_activity_meta_data = self.project_goal_stage_change_activity_meta_data.to_dict()

        project_goal_assignment_change_activity_metadata = (
            self.project_goal_assignment_change_activity_metadata.to_dict()
        )

        project_goal_update_title_activity_metadata = self.project_goal_update_title_activity_metadata.to_dict()

        project_goal_update_description_activity_metadata = (
            self.project_goal_update_description_activity_metadata.to_dict()
        )

        project_goal_file_link_activity_metadata = self.project_goal_file_link_activity_metadata.to_dict()

        project_goal_job_link_activity_metadata = self.project_goal_job_link_activity_metadata.to_dict()

        project_goal_workspace_link_activity_metadata = self.project_goal_workspace_link_activity_metadata.to_dict()

        project_goal_app_link_activity_metadata = self.project_goal_app_link_activity_metadata.to_dict()

        project_goal_model_link_activity_metadata = self.project_goal_model_link_activity_metadata.to_dict()

        project_link_change_activity_metadata = self.project_link_change_activity_metadata.to_dict()

        model_review_activity_with_notes_metadata = self.model_review_activity_with_notes_metadata.to_dict()

        all_model_reviewers_approved_metadata = self.all_model_reviewers_approved_metadata.to_dict()

        registered_model_stage_transitioned_metadata = self.registered_model_stage_transitioned_metadata.to_dict()

        project_goal_bulk_update_activity_metadata = self.project_goal_bulk_update_activity_metadata.to_dict()

        project_goal_bulk_delete_activity_metadata = self.project_goal_bulk_delete_activity_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobStatusActivityMetaData": job_status_activity_meta_data,
                "workspaceStatusActivityMetaData": workspace_status_activity_meta_data,
                "commentActivityMetaData": comment_activity_meta_data,
                "commentedOnJobMetaData": commented_on_job_meta_data,
                "commentedOnWorkspaceMetaData": commented_on_workspace_meta_data,
                "commentedOnFileMetaData": commented_on_file_meta_data,
                "commentedOnProjectGoalMetaData": commented_on_project_goal_meta_data,
                "commentedOnBundleMetaData": commented_on_bundle_meta_data,
                "projectStageChangeActivityMetaData": project_stage_change_activity_meta_data,
                "projectStatusChangeActivityMetaData": project_status_change_activity_meta_data,
                "appStatusActivityMetaData": app_status_activity_meta_data,
                "modelVersionStatusActivityMetaData": model_version_status_activity_meta_data,
                "scheduleJobActivityMetaData": schedule_job_activity_meta_data,
                "scheduleJobEditActivityMetaData": schedule_job_edit_activity_meta_data,
                "fileChangeActivityMetaData": file_change_activity_meta_data,
                "projectGoalCreateActivityMetadata": project_goal_create_activity_metadata,
                "projectGoalStatusChangeActivityMetadata": project_goal_status_change_activity_metadata,
                "projectGoalStageChangeActivityMetaData": project_goal_stage_change_activity_meta_data,
                "projectGoalAssignmentChangeActivityMetadata": project_goal_assignment_change_activity_metadata,
                "projectGoalUpdateTitleActivityMetadata": project_goal_update_title_activity_metadata,
                "projectGoalUpdateDescriptionActivityMetadata": project_goal_update_description_activity_metadata,
                "projectGoalFileLinkActivityMetadata": project_goal_file_link_activity_metadata,
                "projectGoalJobLinkActivityMetadata": project_goal_job_link_activity_metadata,
                "projectGoalWorkspaceLinkActivityMetadata": project_goal_workspace_link_activity_metadata,
                "projectGoalAppLinkActivityMetadata": project_goal_app_link_activity_metadata,
                "projectGoalModelLinkActivityMetadata": project_goal_model_link_activity_metadata,
                "projectLinkChangeActivityMetadata": project_link_change_activity_metadata,
                "modelReviewActivityWithNotesMetadata": model_review_activity_with_notes_metadata,
                "allModelReviewersApprovedMetadata": all_model_reviewers_approved_metadata,
                "registeredModelStageTransitionedMetadata": registered_model_stage_transitioned_metadata,
                "projectGoalBulkUpdateActivityMetadata": project_goal_bulk_update_activity_metadata,
                "projectGoalBulkDeleteActivityMetadata": project_goal_bulk_delete_activity_metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_activity_api_all_model_reviewers_approved_metadata import (
            DominoActivityApiAllModelReviewersApprovedMetadata,
        )
        from ..models.domino_activity_api_app_status_activity_meta_data import (
            DominoActivityApiAppStatusActivityMetaData,
        )
        from ..models.domino_activity_api_comment_activity_meta_data import DominoActivityApiCommentActivityMetaData
        from ..models.domino_activity_api_commented_on_bundle_meta_data import (
            DominoActivityApiCommentedOnBundleMetaData,
        )
        from ..models.domino_activity_api_commented_on_file_meta_data import DominoActivityApiCommentedOnFileMetaData
        from ..models.domino_activity_api_commented_on_job_meta_data import DominoActivityApiCommentedOnJobMetaData
        from ..models.domino_activity_api_commented_on_project_goal_meta_data import (
            DominoActivityApiCommentedOnProjectGoalMetaData,
        )
        from ..models.domino_activity_api_commented_on_workspace_meta_data import (
            DominoActivityApiCommentedOnWorkspaceMetaData,
        )
        from ..models.domino_activity_api_file_change_activity_meta_data import (
            DominoActivityApiFileChangeActivityMetaData,
        )
        from ..models.domino_activity_api_job_status_activity_meta_data import (
            DominoActivityApiJobStatusActivityMetaData,
        )
        from ..models.domino_activity_api_model_review_activity_with_notes_metadata import (
            DominoActivityApiModelReviewActivityWithNotesMetadata,
        )
        from ..models.domino_activity_api_model_version_status_activity_meta_data import (
            DominoActivityApiModelVersionStatusActivityMetaData,
        )
        from ..models.domino_activity_api_project_goal_app_link_activity_metadata import (
            DominoActivityApiProjectGoalAppLinkActivityMetadata,
        )
        from ..models.domino_activity_api_project_goal_assignment_change_activity_metadata import (
            DominoActivityApiProjectGoalAssignmentChangeActivityMetadata,
        )
        from ..models.domino_activity_api_project_goal_bulk_delete_activity_metadata import (
            DominoActivityApiProjectGoalBulkDeleteActivityMetadata,
        )
        from ..models.domino_activity_api_project_goal_bulk_update_activity_metadata import (
            DominoActivityApiProjectGoalBulkUpdateActivityMetadata,
        )
        from ..models.domino_activity_api_project_goal_create_activity_metadata import (
            DominoActivityApiProjectGoalCreateActivityMetadata,
        )
        from ..models.domino_activity_api_project_goal_file_link_activity_metadata import (
            DominoActivityApiProjectGoalFileLinkActivityMetadata,
        )
        from ..models.domino_activity_api_project_goal_job_link_activity_metadata import (
            DominoActivityApiProjectGoalJobLinkActivityMetadata,
        )
        from ..models.domino_activity_api_project_goal_model_link_activity_metadata import (
            DominoActivityApiProjectGoalModelLinkActivityMetadata,
        )
        from ..models.domino_activity_api_project_goal_stage_change_activity_metadata import (
            DominoActivityApiProjectGoalStageChangeActivityMetadata,
        )
        from ..models.domino_activity_api_project_goal_status_change_activity_metadata import (
            DominoActivityApiProjectGoalStatusChangeActivityMetadata,
        )
        from ..models.domino_activity_api_project_goal_update_description_activity_metadata import (
            DominoActivityApiProjectGoalUpdateDescriptionActivityMetadata,
        )
        from ..models.domino_activity_api_project_goal_update_title_activity_metadata import (
            DominoActivityApiProjectGoalUpdateTitleActivityMetadata,
        )
        from ..models.domino_activity_api_project_goal_workspace_link_activity_metadata import (
            DominoActivityApiProjectGoalWorkspaceLinkActivityMetadata,
        )
        from ..models.domino_activity_api_project_link_change_activity_metadata import (
            DominoActivityApiProjectLinkChangeActivityMetadata,
        )
        from ..models.domino_activity_api_project_stage_change_activity_meta_data import (
            DominoActivityApiProjectStageChangeActivityMetaData,
        )
        from ..models.domino_activity_api_project_status_change_activity_meta_data import (
            DominoActivityApiProjectStatusChangeActivityMetaData,
        )
        from ..models.domino_activity_api_registered_model_stage_transitioned_metadata import (
            DominoActivityApiRegisteredModelStageTransitionedMetadata,
        )
        from ..models.domino_activity_api_schedule_job_activity_meta_data import (
            DominoActivityApiScheduleJobActivityMetaData,
        )
        from ..models.domino_activity_api_schedule_job_edit_activity_meta_data import (
            DominoActivityApiScheduleJobEditActivityMetaData,
        )
        from ..models.domino_activity_api_workspace_status_activity_meta_data import (
            DominoActivityApiWorkspaceStatusActivityMetaData,
        )

        d = dict(src_dict)
        job_status_activity_meta_data = DominoActivityApiJobStatusActivityMetaData.from_dict(
            d.pop("jobStatusActivityMetaData")
        )

        workspace_status_activity_meta_data = DominoActivityApiWorkspaceStatusActivityMetaData.from_dict(
            d.pop("workspaceStatusActivityMetaData")
        )

        comment_activity_meta_data = DominoActivityApiCommentActivityMetaData.from_dict(
            d.pop("commentActivityMetaData")
        )

        commented_on_job_meta_data = DominoActivityApiCommentedOnJobMetaData.from_dict(d.pop("commentedOnJobMetaData"))

        commented_on_workspace_meta_data = DominoActivityApiCommentedOnWorkspaceMetaData.from_dict(
            d.pop("commentedOnWorkspaceMetaData")
        )

        commented_on_file_meta_data = DominoActivityApiCommentedOnFileMetaData.from_dict(
            d.pop("commentedOnFileMetaData")
        )

        commented_on_project_goal_meta_data = DominoActivityApiCommentedOnProjectGoalMetaData.from_dict(
            d.pop("commentedOnProjectGoalMetaData")
        )

        commented_on_bundle_meta_data = DominoActivityApiCommentedOnBundleMetaData.from_dict(
            d.pop("commentedOnBundleMetaData")
        )

        project_stage_change_activity_meta_data = DominoActivityApiProjectStageChangeActivityMetaData.from_dict(
            d.pop("projectStageChangeActivityMetaData")
        )

        project_status_change_activity_meta_data = DominoActivityApiProjectStatusChangeActivityMetaData.from_dict(
            d.pop("projectStatusChangeActivityMetaData")
        )

        app_status_activity_meta_data = DominoActivityApiAppStatusActivityMetaData.from_dict(
            d.pop("appStatusActivityMetaData")
        )

        model_version_status_activity_meta_data = DominoActivityApiModelVersionStatusActivityMetaData.from_dict(
            d.pop("modelVersionStatusActivityMetaData")
        )

        schedule_job_activity_meta_data = DominoActivityApiScheduleJobActivityMetaData.from_dict(
            d.pop("scheduleJobActivityMetaData")
        )

        schedule_job_edit_activity_meta_data = DominoActivityApiScheduleJobEditActivityMetaData.from_dict(
            d.pop("scheduleJobEditActivityMetaData")
        )

        file_change_activity_meta_data = DominoActivityApiFileChangeActivityMetaData.from_dict(
            d.pop("fileChangeActivityMetaData")
        )

        project_goal_create_activity_metadata = DominoActivityApiProjectGoalCreateActivityMetadata.from_dict(
            d.pop("projectGoalCreateActivityMetadata")
        )

        project_goal_status_change_activity_metadata = (
            DominoActivityApiProjectGoalStatusChangeActivityMetadata.from_dict(
                d.pop("projectGoalStatusChangeActivityMetadata")
            )
        )

        project_goal_stage_change_activity_meta_data = (
            DominoActivityApiProjectGoalStageChangeActivityMetadata.from_dict(
                d.pop("projectGoalStageChangeActivityMetaData")
            )
        )

        project_goal_assignment_change_activity_metadata = (
            DominoActivityApiProjectGoalAssignmentChangeActivityMetadata.from_dict(
                d.pop("projectGoalAssignmentChangeActivityMetadata")
            )
        )

        project_goal_update_title_activity_metadata = DominoActivityApiProjectGoalUpdateTitleActivityMetadata.from_dict(
            d.pop("projectGoalUpdateTitleActivityMetadata")
        )

        project_goal_update_description_activity_metadata = (
            DominoActivityApiProjectGoalUpdateDescriptionActivityMetadata.from_dict(
                d.pop("projectGoalUpdateDescriptionActivityMetadata")
            )
        )

        project_goal_file_link_activity_metadata = DominoActivityApiProjectGoalFileLinkActivityMetadata.from_dict(
            d.pop("projectGoalFileLinkActivityMetadata")
        )

        project_goal_job_link_activity_metadata = DominoActivityApiProjectGoalJobLinkActivityMetadata.from_dict(
            d.pop("projectGoalJobLinkActivityMetadata")
        )

        project_goal_workspace_link_activity_metadata = (
            DominoActivityApiProjectGoalWorkspaceLinkActivityMetadata.from_dict(
                d.pop("projectGoalWorkspaceLinkActivityMetadata")
            )
        )

        project_goal_app_link_activity_metadata = DominoActivityApiProjectGoalAppLinkActivityMetadata.from_dict(
            d.pop("projectGoalAppLinkActivityMetadata")
        )

        project_goal_model_link_activity_metadata = DominoActivityApiProjectGoalModelLinkActivityMetadata.from_dict(
            d.pop("projectGoalModelLinkActivityMetadata")
        )

        project_link_change_activity_metadata = DominoActivityApiProjectLinkChangeActivityMetadata.from_dict(
            d.pop("projectLinkChangeActivityMetadata")
        )

        model_review_activity_with_notes_metadata = DominoActivityApiModelReviewActivityWithNotesMetadata.from_dict(
            d.pop("modelReviewActivityWithNotesMetadata")
        )

        all_model_reviewers_approved_metadata = DominoActivityApiAllModelReviewersApprovedMetadata.from_dict(
            d.pop("allModelReviewersApprovedMetadata")
        )

        registered_model_stage_transitioned_metadata = (
            DominoActivityApiRegisteredModelStageTransitionedMetadata.from_dict(
                d.pop("registeredModelStageTransitionedMetadata")
            )
        )

        project_goal_bulk_update_activity_metadata = DominoActivityApiProjectGoalBulkUpdateActivityMetadata.from_dict(
            d.pop("projectGoalBulkUpdateActivityMetadata")
        )

        project_goal_bulk_delete_activity_metadata = DominoActivityApiProjectGoalBulkDeleteActivityMetadata.from_dict(
            d.pop("projectGoalBulkDeleteActivityMetadata")
        )

        domino_activity_api_all_metadata = cls(
            job_status_activity_meta_data=job_status_activity_meta_data,
            workspace_status_activity_meta_data=workspace_status_activity_meta_data,
            comment_activity_meta_data=comment_activity_meta_data,
            commented_on_job_meta_data=commented_on_job_meta_data,
            commented_on_workspace_meta_data=commented_on_workspace_meta_data,
            commented_on_file_meta_data=commented_on_file_meta_data,
            commented_on_project_goal_meta_data=commented_on_project_goal_meta_data,
            commented_on_bundle_meta_data=commented_on_bundle_meta_data,
            project_stage_change_activity_meta_data=project_stage_change_activity_meta_data,
            project_status_change_activity_meta_data=project_status_change_activity_meta_data,
            app_status_activity_meta_data=app_status_activity_meta_data,
            model_version_status_activity_meta_data=model_version_status_activity_meta_data,
            schedule_job_activity_meta_data=schedule_job_activity_meta_data,
            schedule_job_edit_activity_meta_data=schedule_job_edit_activity_meta_data,
            file_change_activity_meta_data=file_change_activity_meta_data,
            project_goal_create_activity_metadata=project_goal_create_activity_metadata,
            project_goal_status_change_activity_metadata=project_goal_status_change_activity_metadata,
            project_goal_stage_change_activity_meta_data=project_goal_stage_change_activity_meta_data,
            project_goal_assignment_change_activity_metadata=project_goal_assignment_change_activity_metadata,
            project_goal_update_title_activity_metadata=project_goal_update_title_activity_metadata,
            project_goal_update_description_activity_metadata=project_goal_update_description_activity_metadata,
            project_goal_file_link_activity_metadata=project_goal_file_link_activity_metadata,
            project_goal_job_link_activity_metadata=project_goal_job_link_activity_metadata,
            project_goal_workspace_link_activity_metadata=project_goal_workspace_link_activity_metadata,
            project_goal_app_link_activity_metadata=project_goal_app_link_activity_metadata,
            project_goal_model_link_activity_metadata=project_goal_model_link_activity_metadata,
            project_link_change_activity_metadata=project_link_change_activity_metadata,
            model_review_activity_with_notes_metadata=model_review_activity_with_notes_metadata,
            all_model_reviewers_approved_metadata=all_model_reviewers_approved_metadata,
            registered_model_stage_transitioned_metadata=registered_model_stage_transitioned_metadata,
            project_goal_bulk_update_activity_metadata=project_goal_bulk_update_activity_metadata,
            project_goal_bulk_delete_activity_metadata=project_goal_bulk_delete_activity_metadata,
        )

        domino_activity_api_all_metadata.additional_properties = d
        return domino_activity_api_all_metadata

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
