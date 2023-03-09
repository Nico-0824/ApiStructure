import json

import requests

from utils.log_util import logger
from utils.read import base_data

host = base_data.read_ini()['host']['juhe_api_host']


class RestClient:

    def __init__(self):
        self.host = host

    def get(self, url, **kwargs):
        return self.request("GET", self.host + url, **kwargs)

    def post(self, url, **kwargs):
        return self.request("POST", self.host + url, **kwargs)

    def put(self, url, **kwargs):
        return self.request("PUT", self.host + url, **kwargs)

    def delete(self, url, **kwargs):
        return self.request("DELETE", self.host + url, **kwargs)

    def request(self, method, url, **kwargs):
        self.request_log(method, url, **kwargs)
        if method == 'GET':
            return requests.get(url, **kwargs)
        if method == 'POST':
            return requests.post(url, **kwargs)
        if method == 'PUT':
            return requests.put(url, **kwargs)
        if method == 'DELETE':
            return requests.delete(url, **kwargs)

    def request_log(self, method, url, **kwargs):
        params = dict(**kwargs).get('params')
        data = dict(**kwargs).get('data')
        json_data = dict(**kwargs).get('json_data')
        headers = dict(**kwargs).get('headers')
        logger.info('接口请求的地址>>>>{}'.format(self.host + url))
        logger.info('接口请求的方法>>>>{}'.format(method))
        if params is not None:
            logger.info('接口请求的params参数>>>>\n{}'.format(json.dumps(params, indent=2)))
        if data is not None:
            logger.info('接口请求的data参数>>>>\n{}'.format(json.dumps(data, indent=2)))
        if json_data is not None:
            logger.info('接口请求的json_data参数>>>>\n{}'.format(json.dumps(json_data, indent=2)))
        if headers is not None:
            logger.info('接口请求的headers参数>>>>\n{}'.format(json.dumps(headers, indent=2)))
