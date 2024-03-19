from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.message_order = (By.XPATH, "//*[@class='complete-header' and text()='Thank you for your order!']")

    def finish_order(self):
        self.check_element(self.message_order)
