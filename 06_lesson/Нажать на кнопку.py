from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация веб-драйвера
browser = webdriver.Chrome()

try:
    # Переход на страницу
    browser.get("http://uitestingplayground.com/ajax")

    # Нахождение синей кнопки и нажатие на нее
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    # Явное ожидание появления текста в зеленой плашке
    text_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#content"))
    )

    # Получение текста и вывод в консоль
    text = text_element.text
    print(text)

finally:
    # Закрытие браузера
    browser.quit()