from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)
    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()



class MainPage:
    def __init__(self, driver):
        self.driver = driver
    def add_to_cart(self, product_id):
        self.driver.find_element(By.ID, f"add-to-cart-{product_id}").click()
    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
    def click_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
    def fill_form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
    def get_total(self):
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text









