from base.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.send_keys(LoginLocators.USERNAME, username)
        

    def enter_password(self, password):
        self.send_keys(LoginLocators.PASSWORD, password)

    def click_login(self):
        self.click(LoginLocators.LOGIN_BUTTON)

    def get_Text(self, err):
        return self.driver.find_element(*err).text
