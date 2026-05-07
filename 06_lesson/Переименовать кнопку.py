from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем браузер
browser = webdriver.Chrome()

try:
    # Переходим на сайт
    browser.get('http://uitestingplayground.com/textinput')

    # Находим поле ввода и вводим в него текст "SkyPro"
    input_field = browser.find_element(By.ID, 'newButtonName')
    input_field.send_keys('SkyPro')

    # Находим кнопку и нажимаем на нее
    button = browser.find_element(By.ID, 'updatingButton')
    button.click()

    # Получаем текст кнопки и выводим его в консоль
    button_text = button.text
    print(button_text)

finally:
    # Закрываем браузер
    browser.quit()