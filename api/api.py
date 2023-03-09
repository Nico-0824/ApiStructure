from core.api_util import api_util


def mobile_query(params, headers):
    res = api_util.get_mobile_belong(headers=headers, params=params)
    return res.json()


def ip_belong(data, headers):
    res = api_util.post_ip_belong(headers=headers, data=data)
    return res.json()