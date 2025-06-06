import pytest
from driver.driver_factory import DriverFactory
from pages.login_page import LoginPage
from utils.config import Config
from locators.login_locators import LoginLocators

import time

class TestLogin:
     def setup_method(self):
         self.driver = DriverFactory.get_driver(Config.BROWSER)
         self.driver.get(Config.URL)
         self.login_page = LoginPage(self.driver)

     def teardown_method(self):
         self.driver.quit()

     def test_login_success(self):
        self.login_page.enter_username(Config.USERNAME)
        time.sleep(3)

        self.login_page.enter_password(Config.PASSWORD)
        time.sleep(3)
        self.login_page.click_login()
        time.sleep(5)
        assert "Swag Labs" in self.driver.title

     def test_login_success1(self):
        
        self.login_page.enter_username(Config.USERNAME1)
        time.sleep(3)
        self.login_page.enter_password(Config.PASSWORD)
        time.sleep(3)
        self.login_page.click_login()
        time.sleep(5)
        assert "Swag Labs" in self.driver.title

     def test_login_fail(self):
        
        self.login_page.enter_username(Config.USERNAME2)
        time.sleep(5)
        self.login_page.enter_password(Config.PASSWORD)
        time.sleep(5)
        self.login_page.click_login()
        time.sleep(5)
        assert "sadface" in self.login_page.get_Text(LoginLocators.Error)