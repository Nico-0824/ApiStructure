from core.rest_client import RestClient
from utils.read_data import get_data


class Api(RestClient):
    def __init__(self):
        super().__init__()

    def get_mobile_belong(self, **kwargs):
        return self.get('/mobile/get', **kwargs)

    def post_ip_belong(self, **kwargs):
        return self.post('/ip/ipNewV3', **kwargs) 


api_util = Api()
