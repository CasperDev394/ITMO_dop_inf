from pages.home_page import HomePage


def test_visit(browser):
    home_page = HomePage(browser)

    home_page.visit()
    home_page.login_btn.find_element()
