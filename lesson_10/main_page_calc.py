from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPageCalc:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        self._driver.maximize_window()
        self.delay_value = 0

    def delay(self, value) -> None:
        """Устанавливает задержку перед выполнением операции.
        Args:
        value (int): Задержка в секундах.
        """
        self.delay_value = value
        input_delay = self._driver.find_element(By.ID, "delay")
        input_delay.click()
        input_delay.clear()
        input_delay.send_keys(value)

    def number_seven(self):
        """Данная функция осуществляет нажатие на цифру 7"""
        keys = self._driver.find_element(By.CLASS_NAME, "keys")
        keys.find_element(By.XPATH, "//span[text()='7']").click()

    def plus_operator(self):
        """Данная функция осуществляет нажатие на оператор сложения"""
        keys = self._driver.find_element(By.CLASS_NAME, "keys")
        keys.find_element(By.XPATH, "//span[text()='+']").click()

    def number_eight(self):
        """Данная функция осуществляет нажатие на цифру 8"""
        keys = self._driver.find_element(By.CLASS_NAME, "keys")
        keys.find_element(By.XPATH, "//span[text()='8']").click()

    def button_equals(self):
        """Данная функция осуществляет нажатие на оператор равенства"""
        keys = self._driver.find_element(By.CLASS_NAME, "keys")
        keys.find_element(By.XPATH, "//span[text()='=']").click()
        wait_time = int(self.delay_value) + 1
        waiter = WebDriverWait(self._driver, wait_time)
        waiter.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

    def result(self) -> str:
        """Возвращает текст результата на экране калькулятора.
        Returns:
        str: Текст, отображаемый на экране (например, "15").
        """
        res = self._driver.find_element(By.CLASS_NAME, "screen").text
        return res

    def close_browser(self) -> None:
        """Закрывает браузер."""
        self._driver.quit()
