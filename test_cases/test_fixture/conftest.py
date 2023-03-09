import pytest


@pytest.fixture()
def return_params():
    params = {"phone": "1311111111", "key": "49d85ac0c73670c9318bde49f3df493c"}
    yield params
