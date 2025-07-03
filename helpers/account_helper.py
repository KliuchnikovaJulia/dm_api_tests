import json
from json import JSONDecodeError

from apis.dm_api_account.account_api import AccountApi
from apis.dm_api_account.login_api import LoginApi
from apis.mailhog_api.mailhog_api import MailhogApi
from services.dm_api_account import DmApiAccount
from services.mailhog import Mailhog


class AccountHelper:
    def __init__(self, dm_api_account: DmApiAccount, mailhog: Mailhog):
        self.dm_api_account = dm_api_account
        self.mailhog = mailhog

    def register_new_user(self, login: str, email: str, password: str):
        json_data = {
            "login": login,
            "email": email,
            "password": password
        }
        response = self.dm_api_account.account_api.post_v1_account(
            json_data=json_data

        )
        assert response.status_code == 201
        activation_token = self.find_token(login)
        response = self.dm_api_account.account_api.put_v1_account_token(token=activation_token)
        assert response.status_code == 200
        return response

    def login(self, login: str, password: str, remember_me: bool = True):
        json_data = {
            "login": login,
            "password": password,
            "rememberMe": remember_me
        }
        response = self.dm_api_account.login_api.post_v1_account_login(
            json_data=json_data
        )
        return response

    def change_email(self, login: str, password: str, email: str):
        json_data = {
            "login": login,
            "password": password,
            "email": email,
        }
        response = self.dm_api_account.account_api.put_v1_account_email(
            json_data=json_data
        )
        return response

    def find_token(self, login: str):
        response = self.mailhog.mailhog_api.get_v2_messages(limit=10)
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
        return activation_token
