import pytest
@pytest.mark.parametrize("username,password",[("admin","123Hcl"),("user","123Hcl")])
def test_login(username,password):
    if(username=="admin" and password=="123Hcl"):
        assert  True
    elif(username=="user" and password=="123Hcl"):
        assert True
    else:
        assert False
@pytest.mark.parametrize("items",[200,380,99,300,400])
def test_purchase(items):
    if(items>100):
        assert True
    else:
        assert False
@pytest.mark.smoke
def test_checkout():
    print("logout")