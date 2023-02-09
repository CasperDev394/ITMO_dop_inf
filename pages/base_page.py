'''this: klass base pages'''


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        self.driver.get(self.base_url)

    def get_url(self):
        """ Returns current browser URL. """
        return self.driver.current_url

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False
