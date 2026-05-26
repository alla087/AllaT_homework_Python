from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPageForm:
    def __init__(self,driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.maximize_window()
    def first_name(self,f_name):
        self._driver.find_element(By.CSS_SELECTOR,"[name='first-name']").send_keys(f_name)
    def last_name(self, l_name):
        self._driver.find_element(By.CSS_SELECTOR,"[name='last-name']").send_keys(l_name)
    def address(self,addr):
        self._driver.find_element(By.CSS_SELECTOR,"[name='address']").send_keys(addr)
    def city_name(self,city):
        self._driver.find_element(By.CSS_SELECTOR,"[name='city']").send_keys(city)
    def country(self,country):
        self._driver.find_element(By.CSS_SELECTOR,"[name='country']").send_keys(country)
    def email(self,email):
        self._driver.find_element(By.CSS_SELECTOR,"[name='e-mail']").send_keys(email)
    def phone_number(self,number):
        self._driver.find_element(By.CSS_SELECTOR,"[name='phone']").send_keys(number)
    def job_position(self,job):
        self._driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys(job)
    def company_name(self,name):
        self._driver.find_element(By.CSS_SELECTOR,"[name='company']").send_keys(name)
    def button_submit(self):
        button = self._driver.find_element(By.CLASS_NAME,'btn-outline-primary')
        self._driver.execute_script('arguments[0].click();',button)
    def zip_code(self):
        waiter = WebDriverWait(self._driver, 10)
        waiter.until(
            EC.presence_of_element_located((By.ID, 'zip-code')))
        color=self._driver.find_element(By.ID,'zip-code').get_attribute('class')
        return color
    def fields(self):
        fields = ['first-name', 'last-name', 'address', 'city', 'country', 'e-mail', 'phone', 'job-position', 'company']
        field_class = None
        for field_id in fields:
            field_class = self._driver.find_element(By.ID, field_id).get_attribute('class')
            print(field_class)
        return field_class
    def close_browser(self):
        self._driver.quit()