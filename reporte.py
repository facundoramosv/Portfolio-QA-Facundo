from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

driver_path = "C:/Users/Facundo/OneDrive/Documentos/selenium_test/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

def take_screenshot(name):
    folder = "screenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, name)
    driver.save_screenshot(path)
    print(f"Captura guardada: {path}")

def log_message(message):
    with open("test_log.txt", "a", encoding="utf-8") as file:
        file.write(message + "\n")
    print(message)

try:
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(3)

    products_title = driver.find_element(By.CLASS_NAME, "title")
    if products_title.text == "Products":
        log_message("Login exitoso!")
        take_screenshot("login_exitoso.png")

        products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

        # Validar que exista un producto específico
        producto_a_buscar = "Sauce Labs Backpack"
        productos_texto = [p.text for p in products]

        if producto_a_buscar in productos_texto:
            log_message(f"Producto '{producto_a_buscar}' encontrado. Test PASADO.")
        else:
            log_message(f"Producto '{producto_a_buscar}' NO encontrado. Test FALLADO.")
            take_screenshot("producto_no_encontrado.png")
    else:
        log_message("No se encontró la sección de productos, login posiblemente fallido.")
        take_screenshot("error_login.png")

except Exception as e:
    log_message(f"Error ejecutando test: {e}")
    take_screenshot("excepcion_error.png")

driver.quit()
