from apis.mailhog_api.mailhog_api import MailhogApi
from restclient.configaration import Configuration


class Mailhog:
    def __init__(self, configuration: Configuration):
        self.mailhog_api = MailhogApi(configuration=configuration)
