#Импорт библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Запуск браузера и открытие сайта
driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")

#Авторизация
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

#Добавление товаров в корзину
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

#Переход в корзину и чек-аут
driver.find_element(By.ID, "shopping_cart_container").click()
driver.find_element(By.ID, "checkout").click()

#Заполнение формы
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Имя")
driver.find_element(By.ID, "last-name").send_keys("Фамилия")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()

#Проверка итоговой стоимости
total = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
assert "$58.29" in total, f"Expected total to be $58.29 but got {total}"

#Закрытие браузера
driver.quit()