import requests

from api.api import mobile_query, ip_belong
from utils.read_data import get_data


def test_mobile():
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    params = get_data['mobile_belong']
    result = mobile_query(headers=headers, params=params)
    assert result["resultcode"] == "200"
    assert result["reason"] == "Return Successd!"
    assert result["result"]["province"] == "山西"
    assert result["result"]["city"] == "临汾"
    assert result["result"]["areacode"] == "0357"
    assert result["result"]["zip"] == "041000"
    assert result["result"]["company"] == "联通"
    assert result["result"]["card"] == ""
    assert result["error_code"] == 0