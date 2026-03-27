from enum import Enum


class DominoDatasourceModelAuthType(str, Enum):
    APIKEY = "APIKey"
    AWSIAMBASIC = "AWSIAMBasic"
    AWSIAMBASICNOOVERRIDE = "AWSIAMBasicNoOverride"
    AWSIAMROLE = "AWSIAMRole"
    AWSIAMROLEWITHUSERNAME = "AWSIAMRoleWithUsername"
    AZUREBASIC = "AzureBasic"
    BASIC = "Basic"
    BASICOPTIONAL = "BasicOptional"
    CERTAUTH = "CertAuth"
    CLIENTIDSECRET = "ClientIdSecret"
    GCPBASIC = "GCPBasic"
    KEYPAIR = "KeyPair"
    NOAUTH = "NoAuth"
    OAUTH = "OAuth"
    OAUTHTOKEN = "OAuthToken"
    PERSONALTOKEN = "PersonalToken"
    USERONLY = "UserOnly"

    def __str__(self) -> str:
        return str(self.value)
