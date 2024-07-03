from pages.Test_BasePage import Test_BasePage
from pages.Test_HomePage import Test_HomePage
from time import sleep

def test_login(init_driver):
    
    homepage = Test_HomePage(init_driver)  #creo el objeto homepage, para llamar a los metodos de la clase HomePage
    homepage.load_page("https://portal-app.praxisemr.com/login")
    homepage.login("alice.newman@grr.la", "Gilada12")

    sleep(6)

    texto_obtenido=homepage.verificacion()

    print(f"Texto obtenidoooo: '{texto_obtenido}'")
    sleep(2)
    
    assert texto_obtenido == "alice.newman@grr.la", f"Texto esperado alice.newman@grr.la, pero se obtuvo '{texto_obtenido}'"

    