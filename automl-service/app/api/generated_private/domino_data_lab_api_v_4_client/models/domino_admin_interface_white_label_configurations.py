from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_admin_interface_admin_settings import DominoAdminInterfaceAdminSettings
    from ..models.domino_admin_interface_global_banner import DominoAdminInterfaceGlobalBanner
    from ..models.domino_admin_interface_governance_sce_settings import DominoAdminInterfaceGovernanceSCESettings


T = TypeVar("T", bound="DominoAdminInterfaceWhiteLabelConfigurations")


@_attrs_define
class DominoAdminInterfaceWhiteLabelConfigurations:
    """
    Attributes:
        app_url (str):
        error_page_contact_email (str):
        default_project_name (str):
        favicon (str):
        git_credentials_description (str):
        help_content_url (str):
        support_url (str):
        pdf_app_name (str):
        hide_add_project_action (bool):
        hide_popular_projects (bool):
        hide_download_domino_cli (bool):
        hide_marketing_disclaimer (bool):
        hide_public_projects (bool):
        hide_searchable_projects (bool):
        hide_suggested_projects (bool):
        hide_learn_more_on_file (bool):
        hide_git_ssh_key (bool):
        app_name (str):
        page_footer (str):
        show_support_button (bool):
        support_email (str):
        app_logo (None | str | Unset):
        app_logo_bg_color (None | str | Unset):
        color_theme (None | str | Unset):
        dataset_container_home_display (None | str | Unset):
        dataset_local_path_display (None | str | Unset):
        pdf_template_url (None | str | Unset):
        global_banner (DominoAdminInterfaceGlobalBanner | Unset):
        admin (DominoAdminInterfaceAdminSettings | Unset):
        govern (DominoAdminInterfaceGovernanceSCESettings | Unset):
    """

    app_url: str
    error_page_contact_email: str
    default_project_name: str
    favicon: str
    git_credentials_description: str
    help_content_url: str
    support_url: str
    pdf_app_name: str
    hide_add_project_action: bool
    hide_popular_projects: bool
    hide_download_domino_cli: bool
    hide_marketing_disclaimer: bool
    hide_public_projects: bool
    hide_searchable_projects: bool
    hide_suggested_projects: bool
    hide_learn_more_on_file: bool
    hide_git_ssh_key: bool
    app_name: str
    page_footer: str
    show_support_button: bool
    support_email: str
    app_logo: None | str | Unset = UNSET
    app_logo_bg_color: None | str | Unset = UNSET
    color_theme: None | str | Unset = UNSET
    dataset_container_home_display: None | str | Unset = UNSET
    dataset_local_path_display: None | str | Unset = UNSET
    pdf_template_url: None | str | Unset = UNSET
    global_banner: DominoAdminInterfaceGlobalBanner | Unset = UNSET
    admin: DominoAdminInterfaceAdminSettings | Unset = UNSET
    govern: DominoAdminInterfaceGovernanceSCESettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_url = self.app_url

        error_page_contact_email = self.error_page_contact_email

        default_project_name = self.default_project_name

        favicon = self.favicon

        git_credentials_description = self.git_credentials_description

        help_content_url = self.help_content_url

        support_url = self.support_url

        pdf_app_name = self.pdf_app_name

        hide_add_project_action = self.hide_add_project_action

        hide_popular_projects = self.hide_popular_projects

        hide_download_domino_cli = self.hide_download_domino_cli

        hide_marketing_disclaimer = self.hide_marketing_disclaimer

        hide_public_projects = self.hide_public_projects

        hide_searchable_projects = self.hide_searchable_projects

        hide_suggested_projects = self.hide_suggested_projects

        hide_learn_more_on_file = self.hide_learn_more_on_file

        hide_git_ssh_key = self.hide_git_ssh_key

        app_name = self.app_name

        page_footer = self.page_footer

        show_support_button = self.show_support_button

        support_email = self.support_email

        app_logo: None | str | Unset
        if isinstance(self.app_logo, Unset):
            app_logo = UNSET
        else:
            app_logo = self.app_logo

        app_logo_bg_color: None | str | Unset
        if isinstance(self.app_logo_bg_color, Unset):
            app_logo_bg_color = UNSET
        else:
            app_logo_bg_color = self.app_logo_bg_color

        color_theme: None | str | Unset
        if isinstance(self.color_theme, Unset):
            color_theme = UNSET
        else:
            color_theme = self.color_theme

        dataset_container_home_display: None | str | Unset
        if isinstance(self.dataset_container_home_display, Unset):
            dataset_container_home_display = UNSET
        else:
            dataset_container_home_display = self.dataset_container_home_display

        dataset_local_path_display: None | str | Unset
        if isinstance(self.dataset_local_path_display, Unset):
            dataset_local_path_display = UNSET
        else:
            dataset_local_path_display = self.dataset_local_path_display

        pdf_template_url: None | str | Unset
        if isinstance(self.pdf_template_url, Unset):
            pdf_template_url = UNSET
        else:
            pdf_template_url = self.pdf_template_url

        global_banner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.global_banner, Unset):
            global_banner = self.global_banner.to_dict()

        admin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.admin, Unset):
            admin = self.admin.to_dict()

        govern: dict[str, Any] | Unset = UNSET
        if not isinstance(self.govern, Unset):
            govern = self.govern.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appURL": app_url,
                "errorPageContactEmail": error_page_contact_email,
                "defaultProjectName": default_project_name,
                "favicon": favicon,
                "gitCredentialsDescription": git_credentials_description,
                "helpContentUrl": help_content_url,
                "supportUrl": support_url,
                "pdfAppName": pdf_app_name,
                "hideAddProjectAction": hide_add_project_action,
                "hidePopularProjects": hide_popular_projects,
                "hideDownloadDominoCli": hide_download_domino_cli,
                "hideMarketingDisclaimer": hide_marketing_disclaimer,
                "hidePublicProjects": hide_public_projects,
                "hideSearchableProjects": hide_searchable_projects,
                "hideSuggestedProjects": hide_suggested_projects,
                "hideLearnMoreOnFile": hide_learn_more_on_file,
                "hideGitSshKey": hide_git_ssh_key,
                "appName": app_name,
                "pageFooter": page_footer,
                "showSupportButton": show_support_button,
                "supportEmail": support_email,
            }
        )
        if app_logo is not UNSET:
            field_dict["appLogo"] = app_logo
        if app_logo_bg_color is not UNSET:
            field_dict["appLogoBgColor"] = app_logo_bg_color
        if color_theme is not UNSET:
            field_dict["colorTheme"] = color_theme
        if dataset_container_home_display is not UNSET:
            field_dict["datasetContainerHomeDisplay"] = dataset_container_home_display
        if dataset_local_path_display is not UNSET:
            field_dict["datasetLocalPathDisplay"] = dataset_local_path_display
        if pdf_template_url is not UNSET:
            field_dict["pdfTemplateUrl"] = pdf_template_url
        if global_banner is not UNSET:
            field_dict["globalBanner"] = global_banner
        if admin is not UNSET:
            field_dict["admin"] = admin
        if govern is not UNSET:
            field_dict["govern"] = govern

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_admin_interface_admin_settings import DominoAdminInterfaceAdminSettings
        from ..models.domino_admin_interface_global_banner import DominoAdminInterfaceGlobalBanner
        from ..models.domino_admin_interface_governance_sce_settings import DominoAdminInterfaceGovernanceSCESettings

        d = dict(src_dict)
        app_url = d.pop("appURL")

        error_page_contact_email = d.pop("errorPageContactEmail")

        default_project_name = d.pop("defaultProjectName")

        favicon = d.pop("favicon")

        git_credentials_description = d.pop("gitCredentialsDescription")

        help_content_url = d.pop("helpContentUrl")

        support_url = d.pop("supportUrl")

        pdf_app_name = d.pop("pdfAppName")

        hide_add_project_action = d.pop("hideAddProjectAction")

        hide_popular_projects = d.pop("hidePopularProjects")

        hide_download_domino_cli = d.pop("hideDownloadDominoCli")

        hide_marketing_disclaimer = d.pop("hideMarketingDisclaimer")

        hide_public_projects = d.pop("hidePublicProjects")

        hide_searchable_projects = d.pop("hideSearchableProjects")

        hide_suggested_projects = d.pop("hideSuggestedProjects")

        hide_learn_more_on_file = d.pop("hideLearnMoreOnFile")

        hide_git_ssh_key = d.pop("hideGitSshKey")

        app_name = d.pop("appName")

        page_footer = d.pop("pageFooter")

        show_support_button = d.pop("showSupportButton")

        support_email = d.pop("supportEmail")

        def _parse_app_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_logo = _parse_app_logo(d.pop("appLogo", UNSET))

        def _parse_app_logo_bg_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_logo_bg_color = _parse_app_logo_bg_color(d.pop("appLogoBgColor", UNSET))

        def _parse_color_theme(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color_theme = _parse_color_theme(d.pop("colorTheme", UNSET))

        def _parse_dataset_container_home_display(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_container_home_display = _parse_dataset_container_home_display(
            d.pop("datasetContainerHomeDisplay", UNSET)
        )

        def _parse_dataset_local_path_display(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_local_path_display = _parse_dataset_local_path_display(d.pop("datasetLocalPathDisplay", UNSET))

        def _parse_pdf_template_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pdf_template_url = _parse_pdf_template_url(d.pop("pdfTemplateUrl", UNSET))

        _global_banner = d.pop("globalBanner", UNSET)
        global_banner: DominoAdminInterfaceGlobalBanner | Unset
        if isinstance(_global_banner, Unset):
            global_banner = UNSET
        else:
            global_banner = DominoAdminInterfaceGlobalBanner.from_dict(_global_banner)

        _admin = d.pop("admin", UNSET)
        admin: DominoAdminInterfaceAdminSettings | Unset
        if isinstance(_admin, Unset):
            admin = UNSET
        else:
            admin = DominoAdminInterfaceAdminSettings.from_dict(_admin)

        _govern = d.pop("govern", UNSET)
        govern: DominoAdminInterfaceGovernanceSCESettings | Unset
        if isinstance(_govern, Unset):
            govern = UNSET
        else:
            govern = DominoAdminInterfaceGovernanceSCESettings.from_dict(_govern)

        domino_admin_interface_white_label_configurations = cls(
            app_url=app_url,
            error_page_contact_email=error_page_contact_email,
            default_project_name=default_project_name,
            favicon=favicon,
            git_credentials_description=git_credentials_description,
            help_content_url=help_content_url,
            support_url=support_url,
            pdf_app_name=pdf_app_name,
            hide_add_project_action=hide_add_project_action,
            hide_popular_projects=hide_popular_projects,
            hide_download_domino_cli=hide_download_domino_cli,
            hide_marketing_disclaimer=hide_marketing_disclaimer,
            hide_public_projects=hide_public_projects,
            hide_searchable_projects=hide_searchable_projects,
            hide_suggested_projects=hide_suggested_projects,
            hide_learn_more_on_file=hide_learn_more_on_file,
            hide_git_ssh_key=hide_git_ssh_key,
            app_name=app_name,
            page_footer=page_footer,
            show_support_button=show_support_button,
            support_email=support_email,
            app_logo=app_logo,
            app_logo_bg_color=app_logo_bg_color,
            color_theme=color_theme,
            dataset_container_home_display=dataset_container_home_display,
            dataset_local_path_display=dataset_local_path_display,
            pdf_template_url=pdf_template_url,
            global_banner=global_banner,
            admin=admin,
            govern=govern,
        )

        domino_admin_interface_white_label_configurations.additional_properties = d
        return domino_admin_interface_white_label_configurations

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
