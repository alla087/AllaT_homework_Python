from selenium.webdriver.common.by import By
class OrderPageShop:
    def __init__(self, driver):
        self._driver = driver
    def filling_form(self,f_name,l_name,postal_code):
        self._driver.find_element(By.ID,'first-name').send_keys(f_name)
        self._driver.find_element(By.ID, 'last-name').send_keys(l_name)
        self._driver.find_element(By.ID, 'postal-code').send_keys(postal_code)
    def continue_button(self):
        self._driver.find_element(By.ID,'continue').click()
    def price(self):
        total = self._driver.find_element(By.CLASS_NAME, 'summary_total_label').text
        price = total.replace('Total:', '')
        return price