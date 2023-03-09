import pytest

from utils.log_util import logger


@pytest.fixture()
def return_params():
    params = {"phone": "1311111111", "key": "49d85ac0c73670c9318bde49f3df493c"}
    yield params


@pytest.fixture(scope='function', autouse=True)
def log_info():
    logger.info("用例开始执行~")
    yield
    logger.info("用例执行完毕~")
