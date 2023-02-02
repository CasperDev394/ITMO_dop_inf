from selenium.webdriver.common.by import By


class WebElements:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def click(self):
        self.find_element().click()

    def send_keys(self, text: str):
        self.find_element().send_keys(text)
