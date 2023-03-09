import requests

from utils.read import base_data

host = base_data.read_ini()['host']['juhe_api_host']


class RestClient:

    def __init__(self):
        self.host = host

    def get(self, url, **kwargs):
        return requests.get(self.host + url, **kwargs)

    def post(self, url, **kwargs):
        return requests.post(self.host + url, **kwargs)
