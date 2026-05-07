from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
element = driver.find_element(By.TAG_NAME, "input")
element.send_keys("12345")
sleep (5)
element.clear()
sleep (5)
element.send_keys("54321")
sleep (5)
driver.quit()
