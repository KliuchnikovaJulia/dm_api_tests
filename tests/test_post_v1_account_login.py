import json
import uuid

from apis.dm_api_account.account_api import AccountApi
from apis.dm_api_account.login_api import LoginApi
from apis.mailhog_api.mailhog_api import MailhogApi
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
    json_data = {
        "login": login,
        "email": f'{login}@mail.ru',
        "password": "123456789"
    }
    response = account_api.post_v1_account(
        json_data=json_data

    )
    assert response.status_code == 201

    response = mailhog_api.get_v2_messages(limit=10)
    for item in response.json()['items']:
        body = json.loads(item['Content']['Body'])
        email_login = body['Login']
        if login == email_login:
            token = body['ConfirmationLinkUrl']
            activation_token = token.split('/')[4]
    response = account_api.put_v1_account_token(token=activation_token)
    assert response.status_code == 200
    json_data = {
        "login": login,
        "password": "123456789",
        "rememberMe": True
    }
    response = login_api.post_v1_account_login(
        json_data=json_data
    )
    print(response.json())
    assert response.status_code == 200
