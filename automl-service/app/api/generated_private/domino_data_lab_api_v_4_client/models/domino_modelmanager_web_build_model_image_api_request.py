from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoModelmanagerWebBuildModelImageApiRequest")


@_attrs_define
class DominoModelmanagerWebBuildModelImageApiRequest:
    """
    Attributes:
        model_name (str):
        project_id (str):
        inference_function_to_call (str):
        inference_function_file (str):
        log_http_request_response (bool):
        environment_id (None | str | Unset):
        model_id (None | str | Unset):
        description (None | str | Unset):
    """

    model_name: str
    project_id: str
    inference_function_to_call: str
    inference_function_file: str
    log_http_request_response: bool
    environment_id: None | str | Unset = UNSET
    model_id: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_name = self.model_name

        project_id = self.project_id

        inference_function_to_call = self.inference_function_to_call

        inference_function_file = self.inference_function_file

        log_http_request_response = self.log_http_request_response

        environment_id: None | str | Unset
        if isinstance(self.environment_id, Unset):
            environment_id = UNSET
        else:
            environment_id = self.environment_id

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelName": model_name,
                "projectId": project_id,
                "inferenceFunctionToCall": inference_function_to_call,
                "inferenceFunctionFile": inference_function_file,
                "logHttpRequestResponse": log_http_request_response,
            }
        )
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if model_id is not UNSET:
            field_dict["modelId"] = model_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_name = d.pop("modelName")

        project_id = d.pop("projectId")

        inference_function_to_call = d.pop("inferenceFunctionToCall")

        inference_function_file = d.pop("inferenceFunctionFile")

        log_http_request_response = d.pop("logHttpRequestResponse")

        def _parse_environment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        environment_id = _parse_environment_id(d.pop("environmentId", UNSET))

        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("modelId", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        domino_modelmanager_web_build_model_image_api_request = cls(
            model_name=model_name,
            project_id=project_id,
            inference_function_to_call=inference_function_to_call,
            inference_function_file=inference_function_file,
            log_http_request_response=log_http_request_response,
            environment_id=environment_id,
            model_id=model_id,
            description=description,
        )

        domino_modelmanager_web_build_model_image_api_request.additional_properties = d
        return domino_modelmanager_web_build_model_image_api_request

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
