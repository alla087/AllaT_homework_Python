from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера для Edge
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

# Открыть страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# Заполнение формы
driver.find_element(By.ID, "first-name").send_keys("Иван")
driver.find_element(By.ID, "last-name").send_keys("Петров")
driver.find_element(By.ID, "address").send_keys("Ленина, 55-3")
driver.find_element(By.ID, "email").send_keys("test@skypro.com")
driver.find_element(By.ID, "phone").send_keys("+7985899998787")
driver.find_element(By.ID, "city").send_keys("Москва")
driver.find_element(By.ID, "country").send_keys("Россия")
driver.find_element(By.ID, "job-position").send_keys("QA")
driver.find_element(By.ID, "company").send_keys("SkyPro")

# Нажать на кнопку Submit
driver.find_element(By.ID, "submit").click()

# Ожидание, чтобы убедиться, что форма обработана
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "zip-code"))
    )

# Проверка, что поле Zip code подсвечено красным
zip_code_element = driver.find_element(By.ID, "zip-code")
assert "red" in zip_code_element.get_attribute("style"), "Zip code is not highlighted red!"

# Проверка, что остальные поля подсвечены зеленым
fields = ["first-name", "last-name", "address", "email", "phone", "city", "country", "job-position", "company"]
for field in fields:
        element = driver.find_element(By.ID, field)
        assert "green" in element.get_attribute("style"), f"Field {field} is not highlighted green!"

driver.quit()