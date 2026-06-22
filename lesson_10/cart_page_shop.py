from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPageShop:
    def __init__(self, driver):
        self._driver = driver

    def checkout(self):
        checkout_button = WebDriverWait(self._driver,10).until(
            EC.presence_of_element_located((By.ID,'checkout'))

        )
        checkout_button.click()