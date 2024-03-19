import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains,Keys

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
        self.wait_show_element(locator)
        self.discover_element(locator).click()

    def check_element(self, locator):
        self.wait_show_element(locator)
        assert self.discover_element(locator).is_displayed(), f"The element '{locator}' not found"

    def get_text_element(self, locator):
        self.wait_show_element(locator)
        return self.discover_element(locator).text

    def wait_show_element(self,locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))

    def check_element_existing(self, locator):
        assert self.discover_element(locator), "Element '{locator}' not found, but is expected."

    def check_element__not_existing(self, locator):
        assert len(self.discover_elements(locator)) == 0, "Found Element, but expected not existing."

    def two_click(self, locator):
        element = self.wait_show_element(locator)
        ActionChains(self.driver).double_click(element).perform()

    def rigth_click(self, locator):
        element = self.wait_show_element(locator)
        ActionChains(self.driver).context_click(element).perform()

    def press_keyboard(self, locator, key):
        element = self.discover_element(locator)
        if key == "ENTER":
            element.send_keys(Keys.ENTER)

        elif key == "ESPACO":
            element.send_keys(Keys.SPACE)

        elif key == "F1":
            element.send_keys(Keys.F1)