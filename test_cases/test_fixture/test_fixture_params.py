import pytest


@pytest.fixture(params=["数据1", "数据2"], ids=["case1", "case2"])
def test_data(request):
    return request.param


def test_params(test_data):
    print(test_data)
