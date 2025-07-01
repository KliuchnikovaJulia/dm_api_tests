import json
import uuid
from json import JSONDecodeError

from apis.dm_api_account.account_api import AccountApi
from apis.dm_api_account.login_api import LoginApi
from apis.mailhog_api.mailhog_api import MailhogApi
import structlog

from helpers.account_helper import AccountHelper
from restclient.configaration import Configuration

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, ensure_ascii = False)
    ]
)

def test_put_v1_account_email():
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
    new_email = f'{uuid.uuid4()}@mail.com'
    response = account_helper.change_email(login, password, new_email)
    assert response.status_code == 200
    response = account_helper.login(login, password)
    assert response.status_code == 403

    activation_token = account_helper.find_token(login)
    response = account_api.put_v1_account_token(token=activation_token)
    assert response.status_code == 200

    response = account_helper.login(login, password)
    assert response.status_code == 200
