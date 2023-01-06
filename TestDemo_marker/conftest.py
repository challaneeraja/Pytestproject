import pytest
@pytest.fixture(scope="function",autouse=True)
def setup():
    print("open browser")
    print("login")
    yield
    print("logout")