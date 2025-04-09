from requests import session


class AccountApi:
    def __init__(self):
        self.session = session()
        self.base_url = 'http://5.63.153.31:5051'

    def post_v1_account(self, json_data):
        response = self.session.post(f'{self.base_url}/v1/account', json=json_data)
        return response

    def put_v1_account_token(self, token):
        response = self.session.put(f'{self.base_url}/v1/account/{token}')
        return response

    def put_v1_account_email(self, json_data):
        response = self.session.put(f'{self.base_url}/v1/account/email', json=json_data)
        return response
