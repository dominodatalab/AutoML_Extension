from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_gruz_api_raw_run_command_run_command_type import DominoGruzApiRawRunCommandRunCommandType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_gruz_api_container_networking_config import DominoGruzApiContainerNetworkingConfig
    from ..models.domino_gruz_api_http_proxy_config import DominoGruzApiHttpProxyConfig
    from ..models.domino_gruz_api_launcher_value import DominoGruzApiLauncherValue


T = TypeVar("T", bound="DominoGruzApiRawRunCommand")


@_attrs_define
class DominoGruzApiRawRunCommand:
    """
    Attributes:
        run_command_type (DominoGruzApiRawRunCommandRunCommandType):
        argv (list[str] | None | Unset):
        name (None | str | Unset):
        title (None | str | Unset):
        commands (list[str] | None | Unset):
        init_command (list[str] | None | Unset):
        networking_config (DominoGruzApiContainerNetworkingConfig | Unset):
        http_proxy (DominoGruzApiHttpProxyConfig | Unset):
        is_git_based (bool | None | Unset):
        command_string (None | str | Unset):
        launcher_id (None | str | Unset):
        values (list[DominoGruzApiLauncherValue] | None | Unset):
    """

    run_command_type: DominoGruzApiRawRunCommandRunCommandType
    argv: list[str] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    commands: list[str] | None | Unset = UNSET
    init_command: list[str] | None | Unset = UNSET
    networking_config: DominoGruzApiContainerNetworkingConfig | Unset = UNSET
    http_proxy: DominoGruzApiHttpProxyConfig | Unset = UNSET
    is_git_based: bool | None | Unset = UNSET
    command_string: None | str | Unset = UNSET
    launcher_id: None | str | Unset = UNSET
    values: list[DominoGruzApiLauncherValue] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_command_type = self.run_command_type.value

        argv: list[str] | None | Unset
        if isinstance(self.argv, Unset):
            argv = UNSET
        elif isinstance(self.argv, list):
            argv = self.argv

        else:
            argv = self.argv

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        commands: list[str] | None | Unset
        if isinstance(self.commands, Unset):
            commands = UNSET
        elif isinstance(self.commands, list):
            commands = self.commands

        else:
            commands = self.commands

        init_command: list[str] | None | Unset
        if isinstance(self.init_command, Unset):
            init_command = UNSET
        elif isinstance(self.init_command, list):
            init_command = self.init_command

        else:
            init_command = self.init_command

        networking_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.networking_config, Unset):
            networking_config = self.networking_config.to_dict()

        http_proxy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.http_proxy, Unset):
            http_proxy = self.http_proxy.to_dict()

        is_git_based: bool | None | Unset
        if isinstance(self.is_git_based, Unset):
            is_git_based = UNSET
        else:
            is_git_based = self.is_git_based

        command_string: None | str | Unset
        if isinstance(self.command_string, Unset):
            command_string = UNSET
        else:
            command_string = self.command_string

        launcher_id: None | str | Unset
        if isinstance(self.launcher_id, Unset):
            launcher_id = UNSET
        else:
            launcher_id = self.launcher_id

        values: list[dict[str, Any]] | None | Unset
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, list):
            values = []
            for values_type_0_item_data in self.values:
                values_type_0_item = values_type_0_item_data.to_dict()
                values.append(values_type_0_item)

        else:
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runCommandType": run_command_type,
            }
        )
        if argv is not UNSET:
            field_dict["argv"] = argv
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title
        if commands is not UNSET:
            field_dict["commands"] = commands
        if init_command is not UNSET:
            field_dict["initCommand"] = init_command
        if networking_config is not UNSET:
            field_dict["networkingConfig"] = networking_config
        if http_proxy is not UNSET:
            field_dict["httpProxy"] = http_proxy
        if is_git_based is not UNSET:
            field_dict["isGitBased"] = is_git_based
        if command_string is not UNSET:
            field_dict["commandString"] = command_string
        if launcher_id is not UNSET:
            field_dict["launcherId"] = launcher_id
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_gruz_api_container_networking_config import DominoGruzApiContainerNetworkingConfig
        from ..models.domino_gruz_api_http_proxy_config import DominoGruzApiHttpProxyConfig
        from ..models.domino_gruz_api_launcher_value import DominoGruzApiLauncherValue

        d = dict(src_dict)
        run_command_type = DominoGruzApiRawRunCommandRunCommandType(d.pop("runCommandType"))

        def _parse_argv(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                argv_type_0 = cast(list[str], data)

                return argv_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        argv = _parse_argv(d.pop("argv", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_commands(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                commands_type_0 = cast(list[str], data)

                return commands_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        commands = _parse_commands(d.pop("commands", UNSET))

        def _parse_init_command(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                init_command_type_0 = cast(list[str], data)

                return init_command_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        init_command = _parse_init_command(d.pop("initCommand", UNSET))

        _networking_config = d.pop("networkingConfig", UNSET)
        networking_config: DominoGruzApiContainerNetworkingConfig | Unset
        if isinstance(_networking_config, Unset):
            networking_config = UNSET
        else:
            networking_config = DominoGruzApiContainerNetworkingConfig.from_dict(_networking_config)

        _http_proxy = d.pop("httpProxy", UNSET)
        http_proxy: DominoGruzApiHttpProxyConfig | Unset
        if isinstance(_http_proxy, Unset):
            http_proxy = UNSET
        else:
            http_proxy = DominoGruzApiHttpProxyConfig.from_dict(_http_proxy)

        def _parse_is_git_based(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_git_based = _parse_is_git_based(d.pop("isGitBased", UNSET))

        def _parse_command_string(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        command_string = _parse_command_string(d.pop("commandString", UNSET))

        def _parse_launcher_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        launcher_id = _parse_launcher_id(d.pop("launcherId", UNSET))

        def _parse_values(data: object) -> list[DominoGruzApiLauncherValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = []
                _values_type_0 = data
                for values_type_0_item_data in _values_type_0:
                    values_type_0_item = DominoGruzApiLauncherValue.from_dict(values_type_0_item_data)

                    values_type_0.append(values_type_0_item)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoGruzApiLauncherValue] | None | Unset, data)

        values = _parse_values(d.pop("values", UNSET))

        domino_gruz_api_raw_run_command = cls(
            run_command_type=run_command_type,
            argv=argv,
            name=name,
            title=title,
            commands=commands,
            init_command=init_command,
            networking_config=networking_config,
            http_proxy=http_proxy,
            is_git_based=is_git_based,
            command_string=command_string,
            launcher_id=launcher_id,
            values=values,
        )

        domino_gruz_api_raw_run_command.additional_properties = d
        return domino_gruz_api_raw_run_command

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
