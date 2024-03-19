from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage

class CheckOrderPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.btn_finish = (By.ID, "finish")

    def click_order_finish(self):
        self.click_element(self.btn_finish)
