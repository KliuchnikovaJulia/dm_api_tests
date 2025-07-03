
import uuid
from helpers.account_helper import AccountHelper
from restclient.configaration import Configuration
import structlog

from services.dm_api_account import DmApiAccount
from services.mailhog import Mailhog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, ensure_ascii = False)
    ]
)


def test_post_v1_account_login():
    configuration = Configuration(host='http://5.63.153.31:5051', disable_log=False)
    mailhog_configuration = Configuration(host='http://5.63.153.31:5025')
    dm_api_account = DmApiAccount(configuration)
    mailhog = Mailhog(mailhog_configuration)
    login = str(uuid.uuid4())
    email = login + '@mail.ru'
    password = '123456789'
    account_helper = AccountHelper(dm_api_account, mailhog)


    response = account_helper.register_new_user(login, email, password)
    assert response.status_code == 200
    response = account_helper.login(login, password)
    assert response.status_code == 200
