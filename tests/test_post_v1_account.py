import pprint
import uuid

from apis.dm_api_account.account_api import AccountApi
from apis.mailhog_api.mailhog_api import MailhogApi
import json


def test_post_v1_account():
    account_api = AccountApi()
    mailhog_api = MailhogApi()
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
