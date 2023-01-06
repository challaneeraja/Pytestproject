import pytest
@pytest.fixture
def setup():
    print("open browser")
    print("login")
    yield
    print("logout")
@pytest.mark.parametrize("num,result",[(2,4),(3,9),(4,16)])
def test_checksquare(num,result,setup):
    assert num*num==result
@pytest.mark.parametrize("username,password",[("admin","123"),("user","456"),("net","789")])
def test_users(username,password,setup):
    print(username)
    print(password)