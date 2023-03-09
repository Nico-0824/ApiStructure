import pytest


# 数组
@pytest.mark.parametrize("hero_name, hero_job", [("安琪拉", "法师"), ("黄忠", "射手")])
def test_parameterize_02(hero_name, hero_job):
    print(f'{hero_name}的职业是{hero_job}')


# 列表
@pytest.mark.parametrize("hero_name, hero_job", [["安琪拉", "法师"], ["黄忠", "射手"]])
def test_parameterize_03(hero_name, hero_job):
    print(f'{hero_name}的职业是{hero_job}')
