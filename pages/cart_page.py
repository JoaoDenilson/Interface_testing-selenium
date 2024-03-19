from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.item_inventory = (By.XPATH, "//*[text()='{}']")
        self.btn_continue_shopping = (By.ID, "continue-shopping")
        self.btn_checkout = (By.ID, "checkout")

    def check_product_cart(self, item_name):
        item = (self.item_inventory[0], self.item_inventory[1].format(item_name))
        self.check_element(item)

    def click_continue_shopping(self):
        self.click_element(self.btn_continue_shopping)

    def click_checkout(self):
        self.click_element(self.btn_checkout)
