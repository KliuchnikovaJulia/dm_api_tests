from requests import session

from restclient.client import RestClient


class AccountApi(RestClient):

    def post_v1_account(self, json_data):
        response = self.post(f'/v1/account', json=json_data)
        return response

    def put_v1_account_token(self, token):
        response = self.put(f'/v1/account/{token}')
        return response

    def put_v1_account_email(self, json_data):
        response = self.put(f'/v1/account/email', json=json_data)
        return response
