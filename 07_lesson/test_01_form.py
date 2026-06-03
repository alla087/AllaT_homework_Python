from selenium import webdriver
from pages.main_page_form import MainPageForm

def test_form():
    browser = webdriver.Chrome()
    main_page= MainPageForm(browser)
    main_page.first_name("Иван")
    main_page.last_name("Петров")
    main_page.address('Ленина,55-3')
    main_page.city_name('Москва')
    main_page.country('Россия')
    main_page.email('test@skypro.com')
    main_page.phone_number('+7985899998787')
    main_page.job_position('QA')
    main_page.company_name('SkyPro')
    main_page.button_submit()
    red = main_page.zip_code()
    assert 'danger' in red
    green = main_page.fields()
    assert 'success' in green
    main_page.close_browser()