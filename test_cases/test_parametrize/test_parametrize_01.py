import pytest


@pytest.mark.parametrize("name", ["Google"])
def test_parameterize_01(name):
    assert name == "Google"


"""一个参数多个值,测试用例会把每个值赋给参数,进行测试用例执行,有几个值,测试用例就执行几次"""


@pytest.mark.parametrize("hero_name", ["Google", "Home", "Family"])
def test_parameterize_02(hero_name):
    assert hero_name == "Google"


# 字典参数
@pytest.mark.parametrize("hero",
                         [{"name": "安琪拉", "job": "法师"}, {"name": "黄忠", "job": "射手"}, {"name": "夏侯惇", "job": "战士"}])
def test_parameterize_03(hero):
    print(f'{hero["name"]}的职业是{hero["job"]}')
