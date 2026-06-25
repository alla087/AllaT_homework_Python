from selenium import webdriver
from main_page_calc import MainPageCalc
import allure


@allure.story("Выполнение операции сложения")
@allure.epic("Калькулятор")
@allure.title("Получение результата сложения ")
@allure.description("Сложение 7 и 8")
@allure.severity("critical")
@allure.suite("Калькулятор")
def test_calc():
    browser = webdriver.Chrome()
    main_page = MainPageCalc(browser)
    main_page.delay(5)
    with allure.step("Выбиаем первое слагаемое"):
        main_page.number_seven()
    with allure.step("Выбиаем арифметическую операцию "):
        main_page.plus_operator()
    with allure.step("Выбиаем второе слагаемое"):
        main_page.number_eight()
    with allure.step("Получаем результат вычисления"):
        main_page.button_equals()
    result = main_page.result()
    with allure.step("Повереям результат вычисления"):
        assert result == "15"
    main_page.close_browser()
