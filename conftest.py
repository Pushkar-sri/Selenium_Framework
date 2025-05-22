import pytest
from driver.driver_factory import DriverFactory
from utils.config import Config

@pytest.fixture
def driver():
    driver = DriverFactory.get_driver(Config.BROWSER)
    driver.get(Config.URL)
    yield driver
    driver.quit()
