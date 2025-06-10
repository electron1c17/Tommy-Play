import pytest
from selenium import webdriver

@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://my.proweb.uz/log-in")

    yield driver
