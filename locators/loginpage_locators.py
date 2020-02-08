from selene.api import s


class LoginpageLocators(object):
        # page element locators are stored in this class
        username_input = s('#username')
        password_input = s('#password')
        signin_btn = s('#submit')
        error = s('#error')
