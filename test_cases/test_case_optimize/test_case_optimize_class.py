import requests
import allure
from api.api import mobile_query, ip_belong
from utils.read_data import get_data

@allure.epic('数据进制项目epic')
@allure.feature('手机号查询模块feature')
class TestMobileQuery:

    @allure.story('山西手机号的story')
    @allure.title('测试手机号的title')
    @allure.testcase('http://www.baidu.com/', name='接口地址testcase')
    @allure.issue('http://www.baidu.com/', name='缺陷地址issue')
    @allure.link('http://www.baidu.com/', name='链接地址link')
    @allure.step('先进行归属地的操作step')
    @allure.description('当前手机号是:13111111111, 归属地是山西的description')
    @allure.severity('critical')
    def test_mobile(self):
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

    @allure.title('测试手机号的mobile2')
    @allure.testcase('http://www.baidu.com/', name='接口地址testcase')
    @allure.issue('http://www.baidu.com/', name='缺陷地址issue')
    @allure.link('http://www.baidu.com/', name='链接地址link')
    @allure.step('先进行归属地的操作step')
    @allure.description('当前手机号是:13100000000, 归属地是山东的description')
    @allure.severity('blocker')
    def test_mobile2(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        params = get_data['mobile_belong']
        result = mobile_query(headers=headers, params=params)
        assert result.body["resultcode"] == "200"
        assert result.body["reason"] == "Return Successd!"
        assert result.body["result"]["province"] == "山西1"
        assert result.body["result"]["city"] == "临汾"
        assert result.body["result"]["areacode"] == "0357"
        assert result.body["result"]["zip"] == "041000"
        assert result.body["result"]["company"] == "联通"
        assert result.body["result"]["card"] == ""
        assert result.body["error_code"] == 0\

    @allure.testcase('http://www.baidu.com/', name='接口地址testcase')
    @allure.issue('http://www.baidu.com/', name='缺陷地址issue')
    @allure.link('http://www.baidu.com/', name='链接地址link')
    @allure.step('先进行归属地的操作step')
    @allure.description('当前手机号是:13100000000, 归属地是山东的description')
    @allure.severity('blocker')
    def test_mobile_dynamic(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        params = get_data['mobile_belong_dynamic']['params']
        title = get_data['mobile_belong_dynamic']['title']
        story = get_data['mobile_belong_dynamic']['story']
        allure.dynamic.title(title)
        allure.dynamic.story(story)
        result = mobile_query(headers=headers, params=params)
        assert result.body["resultcode"] == "200"
        assert result.body["reason"] == "Return Successd!"
        assert result.body["result"]["province"] == "山西3"
        assert result.body["result"]["city"] == "临汾"
        assert result.body["result"]["areacode"] == "0357"
        assert result.body["result"]["zip"] == "041000"
        assert result.body["result"]["company"] == "联通"
        assert result.body["result"]["card"] == ""
        assert result.body["error_code"] == 0

