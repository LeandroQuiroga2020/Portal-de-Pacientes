from pages.Test_BasePage import Test_BasePage
from pages.Test_LastPage import Test_LastPage
from pages.Test_HomePage import Test_HomePage
from time import sleep

def test_last(init_driver):
    

    homepage = Test_HomePage(init_driver)
    homepage.load_page("https://portal-app.praxisemr.com/login")
    homepage.login("alice.newman@grr.la", "Gilada12")

    lastccda = Test_LastPage(init_driver)
    lastccda.view_last()

    sleep(3)

