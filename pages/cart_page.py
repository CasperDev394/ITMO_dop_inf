from pages.base_page import BasePage
from components.components import WebElements


class CartPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/cart.html'
        super().__init__(driver, self.base_url)

        self.btn_remove_product = WebElements(driver, '#remove-sauce-labs-backpack')
        self.cart_item = WebElements(driver, '.cart_item')

