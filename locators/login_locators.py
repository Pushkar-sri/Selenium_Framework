from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    Error = (By.XPATH, "//h3[contains(text(),'Epic sadface')]")