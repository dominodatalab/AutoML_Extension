from enum import Enum


class DominoGuardrailsWebRecordGuardrailsAuditEventRequestEventType(str, Enum):
    ACCEPTGOVERNANCEAPPROVAL = "AcceptGovernanceApproval"
    ADDGOVERNANCEBUNDLEATTACHMENT = "AddGovernanceBundleAttachment"
    ADDGOVERNANCEMONITORMODEL = "AddGovernanceMonitorModel"
    ADDGOVERNANCEPOLICYTOBUNDLE = "AddGovernancePolicyToBundle"
    CANCELGOVERNANCEREVIEW = "CancelGovernanceReview"
    CHANGEGOVERNANCEAPPROVERS = "ChangeGovernanceApprovers"
    CHANGEGOVERNANCEBUNDLEPRIMARYPOLICY = "ChangeGovernanceBundlePrimaryPolicy"
    CHANGEGOVERNANCEBUNDLESTAGE = "ChangeGovernanceBundleStage"
    CHANGEGOVERNANCEBUNDLESTATE = "ChangeGovernanceBundleState"
    CHANGEGOVERNANCEFINDINGSTATUS = "ChangeGovernanceFindingStatus"
    CHANGEGOVERNANCEPOLICYSTATUS = "ChangeGovernancePolicyStatus"
    CONDITIONALLYAPPROVEINGOVERNANCE = "ConditionallyApproveInGovernance"
    COPYGOVERNANCEBUNDLE = "CopyGovernanceBundle"
    CREATEGOVERNANCEAPPROVAL = "CreateGovernanceApproval"
    CREATEGOVERNANCEBUNDLE = "CreateGovernanceBundle"
    CREATEGOVERNANCEFINDING = "CreateGovernanceFinding"
    CREATEGOVERNANCEPOLICY = "CreateGovernancePolicy"
    CREATEGOVERNANCERESULTS = "CreateGovernanceResults"
    DEACTIVATEGOVERNANCEBUNDLEPOLICY = "DeactivateGovernanceBundlePolicy"
    DELETEGOVERNANCEBUNDLE = "DeleteGovernanceBundle"
    DELETEGOVERNANCEPOLICY = "DeleteGovernancePolicy"
    DOWNLOADGOVERNANCEBUNDLEREPORT = "DownloadGovernanceBundleReport"
    REACTIVATEGOVERNANCEBUNDLEPOLICY = "ReactivateGovernanceBundlePolicy"
    REJECTGOVERNANCEAPPROVAL = "RejectGovernanceApproval"
    REMOVEGOVERNANCEBUNDLEATTACHMENT = "RemoveGovernanceBundleAttachment"
    RESETGOVERNANCEBUNDLE = "ResetGovernanceBundle"
    UPDATEGOVERNANCEPOLICYDEFINITION = "UpdateGovernancePolicyDefinition"

    def __str__(self) -> str:
        return str(self.value)
