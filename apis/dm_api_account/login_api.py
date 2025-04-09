from requests import session


class LoginApi:
    def __init__(self):
        self.session = session()
        self.base_url = 'http://5.63.153.31:5051'

    def post_v1_account_login(self, json_data):
        response = self.session.post(f'{self.base_url}/v1/account/login', json=json_data)
        return response
    