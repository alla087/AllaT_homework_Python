from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Открываем страницу
driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

# Находим поле ввода по локатору #delay и вводим значение 45
delay_input = driver.find_element(By.ID, 'delay')
delay_input.clear()
delay_input.send_keys('45')

# Нажимаем кнопки 7, +, 8, =
for button in ['7', '+', '8', '=']:
        driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

# Используем явное ожидание, чтобы дождаться результата "15" в окне
result = WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15')
    )

# Проверяем, что результат равен "15"
assert result, "Результат не равен 15"
print("Тест пройден: результат равен 15")

driver.quit()