from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'user-name')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        add_button = self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']/following-sibling::button")
        add_button.click()

    def go_to_cart(self):
        cart_button = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        cart_button.click()

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, 'checkout')

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_information(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, 'first-name').send_keys(first_name)
        self.driver.find_element(By.ID, 'last-name').send_keys(last_name)
        self.driver.find_element(By.ID, 'postal-code').send_keys(postal_code)
        self.driver.find_element(By.ID, 'continue').click()

    def assert_total(self, expected_total):
        total = self.driver.find_element(By.CLASS_NAME, 'summary_total_label').text
        assert total == f"Total: ${expected_total}", f"Expected total {expected_total} but got {total}"













