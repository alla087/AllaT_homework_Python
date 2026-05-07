from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем экземпляр веб-драйвера
browser = webdriver.Chrome()

try:
    # Переходим на нужный сайт
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ждем, пока все картинки загрузятся, используя явное ожидание
    images = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )

    # Получаем 3-ю картинку (индексы начинаются с 0)
    third_image = images[2]

    # Получаем значение атрибута src
    src_value = third_image.get_attribute("src")

    # Выводим значение в консоль
    print("SRC атрибут третьей картинки:", src_value)

finally:
    # Закрываем браузер
    browser.quit()