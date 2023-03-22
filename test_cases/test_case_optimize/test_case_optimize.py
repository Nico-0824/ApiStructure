import requests

from api.api import mobile_query, ip_belong
from utils.read_data import get_data


def test_mobile():
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    params = get_data['mobile_belong']
    result = mobile_query(headers=headers, params=params)
    assert result.body["resultcode"] == "200"
    assert result.body["reason"] == "Return Successd!"
    assert result.body["result"]["province"] == "山西"
    assert result.body["result"]["city"] == "临汾"
    assert result.body["result"]["areacode"] == "0357"
    assert result.body["result"]["zip"] == "041000"
    assert result.body["result"]["company"] == "联通"
    assert result.body["result"]["card"] == ""
    assert result.body["error_code"] == 0