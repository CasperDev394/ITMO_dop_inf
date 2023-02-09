from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WebElements:
    def __init__(self, driver, locator='', type='css'):
        self.driver = driver
        self.locator = locator
        self.type = type

    def find_element(self):
        if self.type == 'css':
            return self.driver.find_element(By.CSS_SELECTOR, self.locator)
        else:
            return self.driver.find_element(By.XPATH, self.locator)

    def click(self):
        self.find_element().click()

    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        """ Get text of the element. """
        return str(self.find_element().text)

    def get_xpath_text(self, property_path: str):
        return self.driver.execute_script("return arguments[0]." + property_path + ";", self.find_element())


