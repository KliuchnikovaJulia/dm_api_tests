import json
import uuid

from apis.dm_api_account.account_api import AccountApi
from apis.dm_api_account.login_api import LoginApi
from apis.mailhog_api.mailhog_api import MailhogApi
from helpers.account_helper import AccountHelper
from restclient.configaration import Configuration
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, ensure_ascii = False)
    ]
)


def test_post_v1_account_login():
    configuration = Configuration(host='http://5.63.153.31:5051', disable_log=False)
    mailhog_configuration = Configuration(host='http://5.63.153.31:5025')
    account_api = AccountApi(configuration)
    mailhog_api = MailhogApi(mailhog_configuration)
    login_api = LoginApi(configuration)
    login = str(uuid.uuid4())
    email = login + '@mail.ru'
    password = '123456789'
    account_helper = AccountHelper(account_api=account_api, mailhog_api=mailhog_api, login_api=login_api)


    response = account_helper.register_new_user(login, email, password)
    assert response.status_code == 200
    response = account_helper.login(login, password)
    assert response.status_code == 200
