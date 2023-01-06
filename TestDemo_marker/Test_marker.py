import pytest
import sys
@pytest.mark.smoke
def test_login():
    print("Login Details")
@pytest.mark.regression
def test_additem():
    print("adding item to the cart")
@pytest.mark.smoke
def test_chechout():
    print("checkout")
@pytest.mark.smoke
def test_logout():
    print("logout")
@pytest.mark.skipif(sys.version_info<(3,12),reason="will execute above 3.11.0 version")
def test_demo():
    print("demo skip")