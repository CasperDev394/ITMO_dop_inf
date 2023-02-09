import time
from pages.home_page import HomePage
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage


def test_visit(browser):
    home_page = HomePage(browser)
    catalog_page = CatalogPage(browser)
    cart_page = CartPage(browser)

    home_page.visit()
    home_page.login_btn.find_element()
    time.sleep(2)
    home_page.user_name.send_keys('standard_user')
    home_page.password.send_keys('secret_sauce')
    time.sleep(2)
    home_page.login_btn.click()
    time.sleep(2)
    catalog_page.btn_first_product.click()
    catalog_page.btn_cart.click()
    time.sleep(2)
    assert cart_page.cart_item.exist()
    cart_page.btn_remove_product.click()
    time.sleep(2)
    assert not cart_page.cart_item.exist()

