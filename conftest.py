
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='module') 
def navegador():
    service = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=service)

    yield navegador 
    navegador.quit()
    #yield lo abre al anvegador durante la prueba y ocn quit se cierra despues
    # considerar el scope, quiero que quede siempre abierto el navegador hasta que terminen las pruebas?
    # le iba a agregar el scope=module para que no se cierre nunca,
    # pero quiza quedaba en un estado por el anterior test que no me dejaba hacer el actual
    # lo deje predeterminado en function