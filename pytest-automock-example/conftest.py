import pytest

@pytest.fixture(autouse=True)
def _mocks(automock):
    with automock("mymod.get_data_from_network", storage="mocks"):
        yield
