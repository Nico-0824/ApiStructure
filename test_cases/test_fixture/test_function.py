import sys

import requests
import pytest

# 默認scope是function, autouse 是true 所有方法都调用
# 谁用谁调用
@pytest.fixture(scope='function', autouse=True)
def app():
    print("我是前置步驟")


def test_mobile():
    url = "http://apis.juhe.cn/mobile/get"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    params = {"phone": "1311111111", "key": "49d85ac0c73670c9318bde49f3df493c"}
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


def test_mobile_error():
    url = "http://apis.juhe.cn/mobile/get"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    params = {"phone": "131111111", "key": "49d85ac0c73670c9318bde49f3df493"}
    r = requests.get(url=url, headers=headers, params=params)
    result = r.json()
    assert result["resultcode"] == "101"
    assert result["reason"] == "错误的请求KEY"
    assert result["error_code"] == 10001


if __name__ == '__main__':
    pytest.main(['-qv', 'test_function.py'])
    # test_mobile_error()
