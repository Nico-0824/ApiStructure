import requests
from utils.read import base_data

host = base_data.read_ini()['host']['juhe_api_host']
params = base_data.read_data()['mobile_belong']

def test_mobile():
    url = host + "/get"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.get(url=url, headers=headers, params=params)
    result = r.json()
    assert result["resultcode"] == "200"
    assert result["reason"] == "Return Successd!"
    assert result["result"]["province"] == "山西"
    assert result["result"]["city"] == "临汾"
    assert result["result"]["areacode"] == "0357"
    assert result["result"]["zip"] == "041000"
    assert result["result"]["company"] == "联通"
    assert result["result"]["card"] == ""
    assert result["error_code"] == 0