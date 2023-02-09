import time
from pages.home_page import HomePage
from pages.catalog_page import CatalogPage


def test_xpath(browser):

    home_page = HomePage(browser)
    catalog_page = CatalogPage(browser)

    home_page.visit()
    login = home_page.text_login.get_xpath_text(property_path='childNodes[1].data')
    password = home_page.text_pass.get_xpath_text(property_path='childNodes[1].data')

    home_page.user_name.send_keys(login)
    home_page.password.send_keys(password)
    home_page.login_btn.click()
    time.sleep(2)
    assert catalog_page.equal_url()
