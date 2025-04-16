from requests import session

from restclient.client import RestClient


class MailhogApi(RestClient):

    def get_v2_messages(self, limit):
        params = {
            'limit': limit,
        }

        response = self.get(f'/api/v2/messages', params=params)
        return response
