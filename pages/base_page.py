import conftest


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def discover_element(self, locator):
        return self.driver.find_element(*locator)

    def discover_elements(self, locator):
        return self.driver.find_elements(*locator)

    def write_element(self, locator, text):
       self.discover_element(locator).send_keys(text)

    def click_element(self, locator):
       self.discover_element(locator).click()

    def check_element(self, locator):
        assert self.discover_element(locator).is_displayed(), f"The element '{locator}' not found"

    def get_text_element(self, locator):
        return self.discover_element(locator).text
