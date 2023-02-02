from pages.base_page import BasePage
from components.components import WebElements


class HomePage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/'
        super().__init__(driver, self.base_url)

        self.login_btn = WebElements(driver, '#login-button')