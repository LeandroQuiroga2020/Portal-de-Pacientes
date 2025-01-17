from selenium.webdriver.support import expected_conditions as ec  
from selenium.webdriver.support.wait import WebDriverWait  
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

class Test_BasePage():
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        
        
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def do_click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def do_send_keys(self, locator, text):
        self.wait.until(ec.visibility_of_element_located(locator)).send_keys(text)

    def do_clear(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator)).clear()

    def get_text(self, locator):
       return self.wait.until(ec.visibility_of_element_located(locator)).text