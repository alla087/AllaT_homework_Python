from selenium import webdriver
from sign_page_shop import SignPageShop
from main_page_shop import MainPageShop
from cart_page_shop import CartPageShop
from order_page_shop import OrderPageShop
import allure


@allure.story('Процедура покупки товара "От авторизации, до покупки товара"')
@allure.epic("Онлайн магазин")
@allure.title("Получение полной стоимости корзины товаров")
@allure.severity("critical")
@allure.suit('Онлайн магазин')

def test_shop():
    browser = webdriver.Firefox()
    sign_page = SignPageShop(browser)
    with allure.step("Ввести логин и пароль"):
        sign_page.sign('standard_user','secret_sauce')
    with allure.step("Нажатие кнопки авторизации"):
        sign_page.login_button()
    main_page = MainPageShop(browser)
    with allure.step("Добавиление вещей в корзину"):
        main_page.add_clothes()
    with allure.step("Переход в корзину"):
        main_page.cart()
        cart_page.checkout()
    order_page = OrderPageShop(browser)
    with allure.step("Заполнение формы оформления заказа"):
        order_page.filling_form("Timur","Khasanov", "636780")

    order_page.continue_button()
    with allure.step("Получение стоимости заказа"):
        total = order_page.price()
    with allure.step("Проверка стоимости заказа"):
        assert total == ' $58.29'
    browser.quit()
