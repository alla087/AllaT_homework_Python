from selenium.webdriver.common.by import By


class SignPageShop:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()

    def sign(self, user_name, password):
        """Функция для ввода логина и пароля"""
        self._driver.find_element(By.ID, "user-name").send_keys(user_name)
        self._driver.find_element(By.ID, "password").send_keys(password)

    def login_button(self):
        """Функция для нажатия кнопкиавторизации"""
        self._driver.find_element(By.ID, "login-button").click()
