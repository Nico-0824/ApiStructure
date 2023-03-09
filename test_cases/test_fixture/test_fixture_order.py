import pytest
from jinja2.nodes import Test


@pytest.fixture(scope="session")
def t_session():
    print("我是session 级别的夹具")


@pytest.fixture(scope="module")
def t_module():
    print("我是module 级别的夹具")


@pytest.fixture(scope="class")
def t_class():
    print("我是class 级别的夹具")


@pytest.fixture(scope="function")
def t_function():
    print("我是function 级别的夹具")



class TestOderFixture:
    def test_t_session(self, t_function, t_module, t_class, t_session):
        assert 1 == 1