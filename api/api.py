from core.api_util import api_util
from utils.response_util import process_response


def mobile_query(params, headers):
    res = api_util.get_mobile_belong(headers=headers, params=params)
    result = process_response(res)
    return result


def ip_belong(data, headers):
    res = api_util.post_ip_belong(headers=headers, data=data)
    result = process_response(res)
    return result
