from selenium import webdriver
from pages.sign_page_shop import SignPageShop
from pages.main_page_shop import MainPageShop
from pages.cart_page_shop import CartPageShop
from pages.order_page_shop import OrderPageShop
def test_shop():
    browser = webdriver.Firefox()
    sign_page = SignPageShop(browser)
    sign_page.sign('standard_user','secret_sauce')
    sign_page.login_button()
    main_page = MainPageShop(browser)
    main_page.add_clothes()
    main_page.cart()
    cart_page = CartPageShop(browser)
    cart_page.checkout()
    order_page = OrderPageShop(browser)
    order_page.filling_form("Timur","Khasanov", "636780")
    order_page.continue_button()
    total = order_page.price()
    assert total == ' $58.29'
    browser.quit()