import pytest

@pytest.fixture()
def choise_user():
    user_id = 123
    yield user_id
    print("Delete User_123")

@pytest.fixture()
def configure_mobile_browser():
    """set the mobile aspect ratio of the browser"""
    print("I'm mobile!")

@pytest.fixture()
def configure_desktop_browser():
    """set the desktop_browser"""
    prinf("I'm desktop")

def test_first(configure_mobile_browser):
    print(configure_mobile_browser);

def test_secong(configure_desktop_browser):
    print(configure_desktop_browser)
    assert 1==1

def test_third(choise_user)
    print(choise_user)
    assert choise_user == 123
