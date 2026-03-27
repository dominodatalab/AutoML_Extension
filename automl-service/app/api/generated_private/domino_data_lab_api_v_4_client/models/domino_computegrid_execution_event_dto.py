from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_computegrid_execution_event_dto_execution_type import (
    DominoComputegridExecutionEventDtoExecutionType,
)
from ..models.domino_computegrid_execution_event_dto_outcome import DominoComputegridExecutionEventDtoOutcome
from ..models.domino_computegrid_execution_event_dto_resource_kind import DominoComputegridExecutionEventDtoResourceKind
from ..models.domino_computegrid_execution_event_dto_source import DominoComputegridExecutionEventDtoSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_computegrid_execution_event_dto_payload_type_0 import (
        DominoComputegridExecutionEventDtoPayloadType0,
    )


T = TypeVar("T", bound="DominoComputegridExecutionEventDto")


@_attrs_define
class DominoComputegridExecutionEventDto:
    """
    Attributes:
        id (str):
        kind (str):
        source (DominoComputegridExecutionEventDtoSource):
        attempt (int):
        attempt_correlation_id (str):
        timestamp (datetime.datetime):
        elapsed_millis (int):
        creation_time (datetime.datetime):
        update_time (datetime.datetime):
        payload (DominoComputegridExecutionEventDtoPayloadType0 | None | Unset):
        resource_kind (DominoComputegridExecutionEventDtoResourceKind | Unset):
        reason (None | str | Unset):
        description (None | str | Unset):
        saga_id (None | str | Unset):
        saga_name (None | str | Unset):
        execution_id (None | str | Unset):
        execution_type (DominoComputegridExecutionEventDtoExecutionType | Unset):
        state (None | str | Unset):
        next_state (None | str | Unset):
        max_attempts (int | None | Unset):
        outcome (DominoComputegridExecutionEventDtoOutcome | Unset):
        outcome_message (None | str | Unset):
        outcome_details (None | str | Unset):
        metric_name (None | str | Unset):
        duration_millis (int | None | Unset):
    """

    id: str
    kind: str
    source: DominoComputegridExecutionEventDtoSource
    attempt: int
    attempt_correlation_id: str
    timestamp: datetime.datetime
    elapsed_millis: int
    creation_time: datetime.datetime
    update_time: datetime.datetime
    payload: DominoComputegridExecutionEventDtoPayloadType0 | None | Unset = UNSET
    resource_kind: DominoComputegridExecutionEventDtoResourceKind | Unset = UNSET
    reason: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    saga_id: None | str | Unset = UNSET
    saga_name: None | str | Unset = UNSET
    execution_id: None | str | Unset = UNSET
    execution_type: DominoComputegridExecutionEventDtoExecutionType | Unset = UNSET
    state: None | str | Unset = UNSET
    next_state: None | str | Unset = UNSET
    max_attempts: int | None | Unset = UNSET
    outcome: DominoComputegridExecutionEventDtoOutcome | Unset = UNSET
    outcome_message: None | str | Unset = UNSET
    outcome_details: None | str | Unset = UNSET
    metric_name: None | str | Unset = UNSET
    duration_millis: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_computegrid_execution_event_dto_payload_type_0 import (
            DominoComputegridExecutionEventDtoPayloadType0,
        )

        id = self.id

        kind = self.kind

        source = self.source.value

        attempt = self.attempt

        attempt_correlation_id = self.attempt_correlation_id

        timestamp = self.timestamp.isoformat()

        elapsed_millis = self.elapsed_millis

        creation_time = self.creation_time.isoformat()

        update_time = self.update_time.isoformat()

        payload: dict[str, Any] | None | Unset
        if isinstance(self.payload, Unset):
            payload = UNSET
        elif isinstance(self.payload, DominoComputegridExecutionEventDtoPayloadType0):
            payload = self.payload.to_dict()
        else:
            payload = self.payload

        resource_kind: str | Unset = UNSET
        if not isinstance(self.resource_kind, Unset):
            resource_kind = self.resource_kind.value

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        saga_id: None | str | Unset
        if isinstance(self.saga_id, Unset):
            saga_id = UNSET
        else:
            saga_id = self.saga_id

        saga_name: None | str | Unset
        if isinstance(self.saga_name, Unset):
            saga_name = UNSET
        else:
            saga_name = self.saga_name

        execution_id: None | str | Unset
        if isinstance(self.execution_id, Unset):
            execution_id = UNSET
        else:
            execution_id = self.execution_id

        execution_type: str | Unset = UNSET
        if not isinstance(self.execution_type, Unset):
            execution_type = self.execution_type.value

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        next_state: None | str | Unset
        if isinstance(self.next_state, Unset):
            next_state = UNSET
        else:
            next_state = self.next_state

        max_attempts: int | None | Unset
        if isinstance(self.max_attempts, Unset):
            max_attempts = UNSET
        else:
            max_attempts = self.max_attempts

        outcome: str | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.value

        outcome_message: None | str | Unset
        if isinstance(self.outcome_message, Unset):
            outcome_message = UNSET
        else:
            outcome_message = self.outcome_message

        outcome_details: None | str | Unset
        if isinstance(self.outcome_details, Unset):
            outcome_details = UNSET
        else:
            outcome_details = self.outcome_details

        metric_name: None | str | Unset
        if isinstance(self.metric_name, Unset):
            metric_name = UNSET
        else:
            metric_name = self.metric_name

        duration_millis: int | None | Unset
        if isinstance(self.duration_millis, Unset):
            duration_millis = UNSET
        else:
            duration_millis = self.duration_millis

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "source": source,
                "attempt": attempt,
                "attemptCorrelationId": attempt_correlation_id,
                "timestamp": timestamp,
                "elapsedMillis": elapsed_millis,
                "creationTime": creation_time,
                "updateTime": update_time,
            }
        )
        if payload is not UNSET:
            field_dict["payload"] = payload
        if resource_kind is not UNSET:
            field_dict["resourceKind"] = resource_kind
        if reason is not UNSET:
            field_dict["reason"] = reason
        if description is not UNSET:
            field_dict["description"] = description
        if saga_id is not UNSET:
            field_dict["sagaId"] = saga_id
        if saga_name is not UNSET:
            field_dict["sagaName"] = saga_name
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if execution_type is not UNSET:
            field_dict["executionType"] = execution_type
        if state is not UNSET:
            field_dict["state"] = state
        if next_state is not UNSET:
            field_dict["nextState"] = next_state
        if max_attempts is not UNSET:
            field_dict["maxAttempts"] = max_attempts
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if outcome_message is not UNSET:
            field_dict["outcomeMessage"] = outcome_message
        if outcome_details is not UNSET:
            field_dict["outcomeDetails"] = outcome_details
        if metric_name is not UNSET:
            field_dict["metricName"] = metric_name
        if duration_millis is not UNSET:
            field_dict["durationMillis"] = duration_millis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_computegrid_execution_event_dto_payload_type_0 import (
            DominoComputegridExecutionEventDtoPayloadType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        kind = d.pop("kind")

        source = DominoComputegridExecutionEventDtoSource(d.pop("source"))

        attempt = d.pop("attempt")

        attempt_correlation_id = d.pop("attemptCorrelationId")

        timestamp = isoparse(d.pop("timestamp"))

        elapsed_millis = d.pop("elapsedMillis")

        creation_time = isoparse(d.pop("creationTime"))

        update_time = isoparse(d.pop("updateTime"))

        def _parse_payload(data: object) -> DominoComputegridExecutionEventDtoPayloadType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_0 = DominoComputegridExecutionEventDtoPayloadType0.from_dict(data)

                return payload_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DominoComputegridExecutionEventDtoPayloadType0 | None | Unset, data)

        payload = _parse_payload(d.pop("payload", UNSET))

        _resource_kind = d.pop("resourceKind", UNSET)
        resource_kind: DominoComputegridExecutionEventDtoResourceKind | Unset
        if isinstance(_resource_kind, Unset):
            resource_kind = UNSET
        else:
            resource_kind = DominoComputegridExecutionEventDtoResourceKind(_resource_kind)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_saga_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saga_id = _parse_saga_id(d.pop("sagaId", UNSET))

        def _parse_saga_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saga_name = _parse_saga_name(d.pop("sagaName", UNSET))

        def _parse_execution_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        execution_id = _parse_execution_id(d.pop("executionId", UNSET))

        _execution_type = d.pop("executionType", UNSET)
        execution_type: DominoComputegridExecutionEventDtoExecutionType | Unset
        if isinstance(_execution_type, Unset):
            execution_type = UNSET
        else:
            execution_type = DominoComputegridExecutionEventDtoExecutionType(_execution_type)

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_next_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_state = _parse_next_state(d.pop("nextState", UNSET))

        def _parse_max_attempts(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_attempts = _parse_max_attempts(d.pop("maxAttempts", UNSET))

        _outcome = d.pop("outcome", UNSET)
        outcome: DominoComputegridExecutionEventDtoOutcome | Unset
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = DominoComputegridExecutionEventDtoOutcome(_outcome)

        def _parse_outcome_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outcome_message = _parse_outcome_message(d.pop("outcomeMessage", UNSET))

        def _parse_outcome_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outcome_details = _parse_outcome_details(d.pop("outcomeDetails", UNSET))

        def _parse_metric_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metric_name = _parse_metric_name(d.pop("metricName", UNSET))

        def _parse_duration_millis(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_millis = _parse_duration_millis(d.pop("durationMillis", UNSET))

        domino_computegrid_execution_event_dto = cls(
            id=id,
            kind=kind,
            source=source,
            attempt=attempt,
            attempt_correlation_id=attempt_correlation_id,
            timestamp=timestamp,
            elapsed_millis=elapsed_millis,
            creation_time=creation_time,
            update_time=update_time,
            payload=payload,
            resource_kind=resource_kind,
            reason=reason,
            description=description,
            saga_id=saga_id,
            saga_name=saga_name,
            execution_id=execution_id,
            execution_type=execution_type,
            state=state,
            next_state=next_state,
            max_attempts=max_attempts,
            outcome=outcome,
            outcome_message=outcome_message,
            outcome_details=outcome_details,
            metric_name=metric_name,
            duration_millis=duration_millis,
        )

        domino_computegrid_execution_event_dto.additional_properties = d
        return domino_computegrid_execution_event_dto

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
