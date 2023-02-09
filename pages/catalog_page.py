from pages.base_page import BasePage
from components.components import WebElements


class CatalogPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/inventory.html'
        super().__init__(driver, self.base_url)

        self.btn_first_product = WebElements(driver, '#add-to-cart-sauce-labs-backpack')
        self.btn_cart = WebElements(driver, '#shopping_cart_container > a')
