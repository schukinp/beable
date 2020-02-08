from locators.loginpage_locators import LoginpageLocators
from selene.api import have


class LoginPage(object):
    # page methods are store in this class
    def login_as(self, username, password):
        LoginpageLocators.username_input.set(username)
        LoginpageLocators.password_input.set(password)
        LoginpageLocators.signin_btn.click()

    def check_error_text_is(self, text):
        LoginpageLocators.error.should(have.text(text))
