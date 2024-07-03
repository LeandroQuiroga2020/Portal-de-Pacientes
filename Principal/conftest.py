import pytest
from selenium import webdriver

@pytest.fixture
def init_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()