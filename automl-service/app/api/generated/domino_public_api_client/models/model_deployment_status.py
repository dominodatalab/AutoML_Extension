from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_deployment_status_state import ModelDeploymentStatusState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_deployment_status_model_operations import ModelDeploymentStatusModelOperations
    from ..models.model_deployment_status_model_states import ModelDeploymentStatusModelStates
    from ..models.model_deployment_status_operation import ModelDeploymentStatusOperation
    from ..models.model_deployment_status_shared_state import ModelDeploymentStatusSharedState


T = TypeVar("T", bound="ModelDeploymentStatus")


@_attrs_define
class ModelDeploymentStatus:
    """The Model Deployment status

    Attributes:
        state (ModelDeploymentStatusState): Standard Domino state value. This field is required in this location for
            Domino model deployment schemas.
        message (str | Unset): Message indicating error or other status information about the most recent operation.
            This field is required in this location for Domino model deployment schemas.
        model_operations (ModelDeploymentStatusModelOperations | Unset): Model-specific operations supported by this
            model deployment. This field is required with this structure in this location for Domino model deployment
            schemas.
        model_states (ModelDeploymentStatusModelStates | Unset): The model-specific states
        shared_operations (list[ModelDeploymentStatusOperation] | Unset): Operations supported by this model deployment.
            This field is required with this structure in this location for Domino model deployment schemas.
        shared_state (ModelDeploymentStatusSharedState | Unset): The state shared by all models in the deployment
    """

    state: ModelDeploymentStatusState
    message: str | Unset = UNSET
    model_operations: ModelDeploymentStatusModelOperations | Unset = UNSET
    model_states: ModelDeploymentStatusModelStates | Unset = UNSET
    shared_operations: list[ModelDeploymentStatusOperation] | Unset = UNSET
    shared_state: ModelDeploymentStatusSharedState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        message = self.message

        model_operations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_operations, Unset):
            model_operations = self.model_operations.to_dict()

        model_states: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_states, Unset):
            model_states = self.model_states.to_dict()

        shared_operations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shared_operations, Unset):
            shared_operations = []
            for shared_operations_item_data in self.shared_operations:
                shared_operations_item = shared_operations_item_data.to_dict()
                shared_operations.append(shared_operations_item)

        shared_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shared_state, Unset):
            shared_state = self.shared_state.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if model_operations is not UNSET:
            field_dict["modelOperations"] = model_operations
        if model_states is not UNSET:
            field_dict["modelStates"] = model_states
        if shared_operations is not UNSET:
            field_dict["sharedOperations"] = shared_operations
        if shared_state is not UNSET:
            field_dict["sharedState"] = shared_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_deployment_status_model_operations import ModelDeploymentStatusModelOperations
        from ..models.model_deployment_status_model_states import ModelDeploymentStatusModelStates
        from ..models.model_deployment_status_operation import ModelDeploymentStatusOperation
        from ..models.model_deployment_status_shared_state import ModelDeploymentStatusSharedState

        d = dict(src_dict)
        state = ModelDeploymentStatusState(d.pop("state"))

        message = d.pop("message", UNSET)

        _model_operations = d.pop("modelOperations", UNSET)
        model_operations: ModelDeploymentStatusModelOperations | Unset
        if isinstance(_model_operations, Unset):
            model_operations = UNSET
        else:
            model_operations = ModelDeploymentStatusModelOperations.from_dict(_model_operations)

        _model_states = d.pop("modelStates", UNSET)
        model_states: ModelDeploymentStatusModelStates | Unset
        if isinstance(_model_states, Unset):
            model_states = UNSET
        else:
            model_states = ModelDeploymentStatusModelStates.from_dict(_model_states)

        _shared_operations = d.pop("sharedOperations", UNSET)
        shared_operations: list[ModelDeploymentStatusOperation] | Unset = UNSET
        if _shared_operations is not UNSET:
            shared_operations = []
            for shared_operations_item_data in _shared_operations:
                shared_operations_item = ModelDeploymentStatusOperation.from_dict(shared_operations_item_data)

                shared_operations.append(shared_operations_item)

        _shared_state = d.pop("sharedState", UNSET)
        shared_state: ModelDeploymentStatusSharedState | Unset
        if isinstance(_shared_state, Unset):
            shared_state = UNSET
        else:
            shared_state = ModelDeploymentStatusSharedState.from_dict(_shared_state)

        model_deployment_status = cls(
            state=state,
            message=message,
            model_operations=model_operations,
            model_states=model_states,
            shared_operations=shared_operations,
            shared_state=shared_state,
        )

        model_deployment_status.additional_properties = d
        return model_deployment_status

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
