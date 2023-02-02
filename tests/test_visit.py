import time
from pages.home_page import HomePage


def test_visit(browser):
    home_page = HomePage(browser)

    home_page.visit()
    home_page.login_btn.find_element()
    time.sleep(2)
    home_page.user_name.send_keys('standard_user')
    home_page.password.send_keys('secret_sauce')
    time.sleep(2)
    home_page.login_btn.click()
    time.sleep(2)
