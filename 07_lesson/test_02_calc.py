from selenium import webdriver
from main_page_calc import CalculatorPage  # Импортируем наш Page Object

class CalculatorTestpytest:
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.calc_page = CalculatorPage(self.driver)

    def test_addition(self):
        self.calc_page.set_delay("45")  # Устанавливаем задержку в 45 секунд

        # Нажимаем кнопки 7, +, 8 и =
        self.calc_page.click_button("7")
        self.calc_page.click_button("+")
        self.calc_page.click_button("8")
        self.calc_page.click_button("=")

        # Проверяем результат
        assert "15" in self.calc_page.get_result(), "Результат неверный!"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()