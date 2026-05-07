from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("tomsmith")
sleep (5)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("SuperSecretPassword!")
sleep (5)
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
sleep (5)
flash_message = driver.find_element(By.ID, "flash")
print(flash_message.text)
sleep (5)
driver.quit()
