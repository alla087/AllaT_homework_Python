from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = driver.find_element(By.ID, "delay")
        self.result_field = driver.find_element(By.CSS_SELECTOR, ".screen")

    def set_delay(self, delay_value):
        self.delay_input.clear()
        self.delay_input.send_keys(delay_value)

    def click_button(self, button_value):
        button = self.driver.find_element(By.XPATH, f"//span[text()='{button_value}']")
        button.click()

    def get_result(self):
        return WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )


