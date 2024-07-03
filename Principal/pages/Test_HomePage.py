
from selenium.webdriver.common.by import By
from pages.Test_BasePage import Test_BasePage


class Test_HomePage(Test_BasePage):  #le pasamos por parametro la clase padre para que pueda heredar

    username = (By.ID,("email-login"))
    
    password = (By.ID,("pass1-login"))
    button = (By.XPATH, "/html/body/app-root/app-login/div/main/section/form/button")
    verifica_texto = (By.XPATH, "/html/body/app-root/app-home/div/div[2]/div/header/div[3]/div[1]/app-patient-name/span")        

  
    
    def __init__(self, driver):
        super(Test_HomePage, self).__init__(driver)

    def load_page(self, url):
        self.driver.get(url)

    def login(self, username_text, password_text):
        self.do_send_keys(self.username, username_text)
        self.do_send_keys(self.password, password_text)
        self.do_click(self.button)

    def verificacion(self):
        return self.get_text(self.verifica_texto)