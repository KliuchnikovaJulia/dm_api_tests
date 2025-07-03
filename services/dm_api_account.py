from apis.dm_api_account.account_api import AccountApi
from apis.dm_api_account.login_api import LoginApi
from restclient.configaration import Configuration


class DmApiAccount:
    def __init__(self, configuration: Configuration):
        self.account_api = AccountApi(configuration=configuration)
        self.login_api = LoginApi(configuration=configuration)
