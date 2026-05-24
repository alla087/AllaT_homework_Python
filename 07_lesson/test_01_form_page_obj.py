from selenium import webdriver


def test_purchase():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Добавление товаров в корзину
    main_page = MainPage(driver)
    main_page.add_to_cart("sauce-labs-backpack")
    main_page.add_to_cart("sauce-labs-bolt-t-shirt")
    main_page.add_to_cart("sauce-labs-onesie")
    main_page.go_to_cart()

    # Переход к оформлению заказа
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Заполнение формы и проверка итоговой стоимости
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Имя", "Фамилия", "12345")
    total = checkout_page.get_total()
    assert total == "$58.29", f"Expected total to be $58.29 but got {total}"

    driver.quit()