
from api.api import ip_belong
from utils.read_data import get_data


def test_post():
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    json_data = get_data['json_data']
    result = ip_belong(headers=headers, data=json_data)
    assert result["resultcode"] == "200"
    assert result["reason"] == "查询成功"
    assert result["result"]["City"] == "内网IP"
    assert result["result"]["Isp"] == "内网IP"
    assert result["error_code"] == 0