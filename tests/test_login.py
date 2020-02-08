import pytest
from pages.login_page import LoginPage
from data import login_data


@pytest.mark.usefixtures('open_base_url')
class TestLogin(object):
    # try to login with an incorrect password and check error
    def test_cannot_incorrect_password(self):
        LoginPage().login_as(login_data['username'], login_data['password'])
        LoginPage().check_error_text_is('Incorrect password')
