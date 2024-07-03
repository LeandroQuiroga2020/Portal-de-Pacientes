from selenium.webdriver.common.by import By
from pages.Test_BasePage import Test_BasePage

class Test_LastPage(Test_BasePage):
    
    boton_lastccda = (By.XPATH, "/html/body/app-root/app-home/div/div[2]/div/main/button") 
     
    def __init__(self, driver):
        super(Test_LastPage, self).__init__(driver)

    def view_last(self):
        self.do_click(self.boton_lastccda) 


    