from api.api import ip_belong
from utils.read_data import get_data


def test_post(log_info):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    json_data = get_data['json_data']
    result = ip_belong(headers=headers, data=json_data)
    assert result.success is True
    assert result.body["resultcode"] == "200"
    assert result.body["reason"] == "查询成功"
    assert result.body["result"]["City"] == "内网IP"
    assert result.body["result"]["Isp"] == "内网IP"
    assert result.body["error_code"] == 0
