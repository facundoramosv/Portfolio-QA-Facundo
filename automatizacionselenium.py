from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = "C:/Users/Facundo/OneDrive/Documentos/selenium_test/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(3)

# Validar login buscando título de productos
try:
    products_title = driver.find_element(By.CLASS_NAME, "title")
    if products_title.text == "Products":
        print("Login exitoso! Aquí están los productos disponibles:")
        
        # Obtener todos los nombres de productos
        products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        for product in products:
            print("-", product.text)
    else:
        print("No se encontró la sección de productos, login posiblemente fallido.")
except Exception as e:
    print("Error validando login:", e)

# driver.quit()
