from selenium.webdriver.common.by import By
import time
import conftest
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")
        # self.item_inventory_2 = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.item_inventory = (By.XPATH, "//*[text()='{}']")
        self.add_cart = (By.XPATH, "//*[text()='Add to cart']")
        self.icon_cart = (By.XPATH, "//*[@class='shopping_cart_link']")

    def check_valid_login(self):
        self.check_element(self.page_title)

    def add_to_cart(self, item_name):
        # item = (self.item_inventory_2[0], self.item_inventory_2[1].format(item_name))
        # self.click_element(item)
        item = (self.item_inventory[0], self.item_inventory[1].format(item_name))
        self.click_element(item)
        self.click_element(self.add_cart)

    def click_cart(self):
        self.click_element(self.icon_cart)
