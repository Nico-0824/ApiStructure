import pytest

from utils.read_data import get_data


# # 单个数值
# @pytest.mark.parametrize("name", get_data["hero_list"])
# def test_parameterize_01(name):
#     print(name)

# 多个数值
@pytest.mark.parametrize("name, word", get_data["hero_words"])
def test_parameterize_01(name, word):
    print(f'{name}的工作是{word}')
