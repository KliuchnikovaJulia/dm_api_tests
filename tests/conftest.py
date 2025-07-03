import pytest
import structlog

from helpers.account_helper import AccountHelper
from restclient.configaration import Configuration
from services.dm_api_account import DmApiAccount
from services.mailhog import Mailhog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, ensure_ascii=False)
    ]
)


@pytest.fixture
def account_helper():
    configuration = Configuration(host='http://5.63.153.31:5051', disable_log=False)
    mailhog_configuration = Configuration(host='http://5.63.153.31:5025')
    dm_api_account = DmApiAccount(configuration)
    mailhog = Mailhog(mailhog_configuration)
    account_helper = AccountHelper(dm_api_account, mailhog)
    return account_helper
