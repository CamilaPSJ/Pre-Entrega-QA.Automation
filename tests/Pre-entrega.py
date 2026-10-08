# Pre-entrega: QA Automation
# Alumno: Camila Pianeta
# DNI: 41665327
# E-mail: camilasanjunapianeta@gmail.com

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Los modulos son con minuscula al principio, son "troncos" por asi decir
# Las clase con Mayuscula al princpio, son "ramas"



    

#CONSIGNA 1:
def test_01_login(navegador):
    navegador.get("https://www.saucedemo.com/")
    espera = WebDriverWait(navegador, 10) 

    espera.until(EC.visibility_of_element_located((By.ID, "user-name"))) 
    #1 parentesis para until,1 para el EC y uno para el By
    navegador.find_element(By.ID, "user-name").send_keys("standard_user",)

    espera.until(EC.visibility_of_element_located((By.ID, "password")))
    navegador.find_element(By.ID, "password").send_keys("secret_sauce",)

    espera.until(EC.element_to_be_clickable((By.ID, "login-button")))
    navegador.find_element(By.ID, "login-button").click()
    #ID aca seria un tipo de localizador (una constante de Selenium), por eso se pone con mayusucla
    #lo mismo pasaria con TAG_NAME,CLASS_NAME,NAME,etc

    espera.until(EC.url_contains("/inventory.html"))
    assert "/inventory" in navegador.current_url, "ERROR: No se encuentra en /inventory.html"

def test_02_en_inventario (navegador):
    titulo = navegador.title
    # driver.title es una prop de selenium y busca el title en la seccion head
    sub_titulo = navegador.find_element (By.CLASS_NAME, "title").text
    # el .text se toma porque yo quiero guardar en mi variable sub_titulo el texto que voy encontrar ahi
    #si no despeus voy a comprar que los elementos sean igual y yo quiero el valor que contiene

    assert titulo =="Swag Labs", f'ERROR: Se esperaba obtener el titulo de ventana "Swag Labs", se obtuvo:{titulo}'

    assert sub_titulo == "Products", f'ERROR: Se esperaba obtener el titulo de seccion "Products", se obtuvo:{sub_titulo}'

    