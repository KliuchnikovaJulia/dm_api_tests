import json
import uuid
from json import JSONDecodeError

from apis.dm_api_account.account_api import AccountApi
from apis.dm_api_account.login_api import LoginApi
from apis.mailhog_api.mailhog_api import MailhogApi


def test_put_v1_account_email():
    account_api = AccountApi()
    mailhog_api = MailhogApi()
    login_api = LoginApi()
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
        print(1, item['Content']['Body'])
        try:
            body = json.loads(item['Content']['Body'])
            email_login = body['Login']
            if login == email_login:
                token = body['ConfirmationLinkUrl']
                activation_token = token.split('/')[4]
        except JSONDecodeError:
            ...
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
    new_email = f'{uuid.uuid4()}@mail.com'
    json_data = {
            "login": login,
            "password": "123456789",
            "email": new_email,
    }
    response = account_api.put_v1_account_email(
        json_data=json_data
    )

    json_data = {
        "login": login,
        "password": "123456789",
        "rememberMe": True
    }
    response = login_api.post_v1_account_login(
        json_data=json_data
    )
    print(response.json())
    assert response.status_code == 403

    response = mailhog_api.get_v2_messages(limit=10)
    for item in response.json()['items']:
        print(1, item['Content']['Body'])
        try:
            body = json.loads(item['Content']['Body'])
            email_login = body['Login']
            if login == email_login:
                token = body['ConfirmationLinkUrl']
                activation_token = token.split('/')[4]
        except JSONDecodeError:
            ...
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
    assert response.status_code == 200
