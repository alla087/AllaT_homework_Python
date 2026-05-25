import pytest
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_purchase_flow(driver):
    driver.get('https://www.saucedemo.com/')

    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    main_page = MainPage(driver)
    main_page.add_to_cart('Sauce Labs Backpack')
    main_page.add_to_cart('Sauce Labs Bolt T-Shirt')
    main_page.add_to_cart('Sauce Labs Onesie')
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_information('Имя', 'Фамилия', '12345')
    checkout_page.assert_total('58.29')