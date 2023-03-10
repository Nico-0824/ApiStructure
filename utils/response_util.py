import json

from core.result_base import ResultResponse
from utils.log_util import logger


def process_response(response):
    if response.status_code == 200 or response.status_code == 201:
        ResultResponse.success = True
        logger.info('接口返回的内容>>>:' + json.dumps(response.json(), ensure_ascii=False))
        ResultResponse.body = response.json()
    else:
        ResultResponse.success = False
        logger.info('接口状态码不是2开头, 请检查')
    return ResultResponse
