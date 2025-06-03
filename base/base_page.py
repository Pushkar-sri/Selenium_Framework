
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        self.driver.find_element(*by_locator).click()
        print("Click method executed.")

    def send_keys(self, by_locator, value):
        self.driver.find_element(*by_locator).send_keys(value)
        print("Send Keys method executed.")

    def get_title(self):
        print("Get Title method executed.")
        return self.driver.title
    
    