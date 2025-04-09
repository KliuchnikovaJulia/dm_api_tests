from requests import session


class MailhogApi:
    def __init__(self):
        self.session = session()
        self.base_url = ' http://5.63.153.31:5025'

    def get_v2_messages(self, limit):
        params = {
            'limit': limit,
        }

        response = self.session.get(f'{self.base_url}/api/v2/messages', params=params)
        return response
