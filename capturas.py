import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

driver_path = "C:/Users/Facundo/OneDrive/Documentos/selenium_test/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

def take_screenshot(name):
    # Carpeta para screenshots
    folder = "screenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, name)
    driver.save_screenshot(path)
    print(f"Captura guardada: {path}")

try:
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(3)

    products_title = driver.find_element(By.CLASS_NAME, "title")
    if products_title.text == "Products":
        print("Login exitoso! Aquí están los productos disponibles:")
        take_screenshot("login_exitoso.png")  # captura post-login
        
        products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

        with open('productos.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Producto'])
            for product in products:
                print("-", product.text)
                writer.writerow([product.text])

        print("Lista de productos guardada en productos.csv")
    else:
        print("No se encontró la sección de productos, login posiblemente fallido.")
        take_screenshot("error_login.png")
except Exception as e:
    print("Error validando login:", e)
    take_screenshot("excepcion_error.png")

driver.quit()
