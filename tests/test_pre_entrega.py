# Pre-entrega: QA Automation
# Alumno: Camila Pianeta
# DNI: 41665327
# E-mail: camilasanjunapianeta@gmail.com

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Los modulos son con minuscula al principio, son "troncos" por asi decir
# Las clase con Mayuscula al princpio, son "ramas"



    

#CONSIGNA 1 y pedacin de la C2:
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



def test_02_inventario_esta (navegador):
    titulo = navegador.title
    # driver.title es una prop de selenium y busca el title en la seccion head
    sub_titulo = navegador.find_element (By.CLASS_NAME, "title").text
    # el .text se toma porque yo quiero guardar en mi variable sub_titulo el texto que voy encontrar ahi
    #si no despeus voy a comprar que los elementos sean igual y yo quiero el valor que contiene

    assert titulo =="Swag Labs", f'ERROR: Se esperaba obtener el titulo de ventana "Swag Labs", se obtuvo:{titulo}'

    assert sub_titulo == "Products", f'ERROR: Se esperaba obtener el titulo de seccion "Products", se obtuvo:{sub_titulo}'


#CONSIGNA 2:
def test_03_productos_ver(navegador):
    objeto_inventario = navegador.find_elements(By.CLASS_NAME, 'inventory_item')

    assert len(objeto_inventario) > 0 , 'ERROR: No se encuentran productos'


def test_04_productos_mostrar_primero(navegador):
    objeto_inventario = navegador.find_elements(By.CLASS_NAME, 'inventory_item')
    primer_producto = objeto_inventario[0]

    nombre_producto = primer_producto.find_elements(By.CLASS_NAME, 'inventory_item_name')
    precio_producto = primer_producto.find_elements(By.CLASS_NAME, 'inventory_item_price')

    print(f'Nombre: {nombre_producto} |  Nombre: {precio_producto}')

    assert nombre_producto != '', 'ERROR: Este producto no tiene un nombre ingresado'
    assert precio_producto != '', 'ERROR: Este producto no tiene un precio ingresado'

def test_05_carrito_agregar_productos(navegador):

    boton_agregar = navegador.find_element(By.XPATH, '(//div[@class="inventory_item"])[1]//button')
    boton_agregar.click()

    # Volvemos a buscar el botón (ahora debería decir "Remove")
    boton_remover = navegador.find_element(By.XPATH, '(//div[@class="inventory_item"])[1]//button')

    assert boton_remover.text.lower() == 'remove', 'ERROR: El boton no se actualizo a "Remove"'


def test_06_interfaz_validar(navegador):
    boton_menu = navegador.find_element(By.CLASS_NAME, 'bm-burger-button')
    boton_filtro = navegador.find_element(By.CLASS_NAME, 'product_sort_container')

    assert boton_menu.is_displayed(), 'ERROR: No se puede ver el menu'
    assert boton_filtro.is_displayed(), 'ERROR: No se encuentra el filtro'
#is_displayesd aca es booleano, si se activa va, si no va el error.



def test_07_carrito_verificar_contador(navegador):
    espera = WebDriverWait(navegador, 10)

    contador_carrito = espera.until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge'))
    ).text

    assert contador_carrito == "1", f'ERROR: Se esperaba 1, obtuvo {contador_carrito}'


def test_08_carrito_navegar(navegador):
    navegador.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    assert "/cart.html" in navegador.current_url , "ERROR: No se encuentra en /cart.html"


def test_09_carrito_comprobar_productos(navegador):
    productos_posibles = ['Sauce Labs Backpack' , 'Sauce Labs Bike Light' , 'Sauce Labs Bolt T-Shirt' , 'Sauce Labs Fleece Jacket' , 'Sauce Labs Onesie' , 'Test.allTheThings() T-Shirt (Red)']
    producto_nombre_carrito = navegador.find_element(By.CLASS_NAME, 'inventory_item_name').text

    assert producto_nombre_carrito in productos_posibles, f'ERROR: {producto_nombre_carrito} no se encuentra en la lista'

    