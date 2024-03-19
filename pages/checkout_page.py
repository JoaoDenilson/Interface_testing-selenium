from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.firstname_field = (By.ID, "first-name")
        self.lastname_field = (By.ID, "last-name")
        self.postalcode_field = (By.ID, "postal-code")
        self.btn_continue_checkout = (By.ID, "continue")

    def form_checkout(self, firstname, lastname, postalcode):
        self.write_element(self.firstname_field, firstname)
        self.write_element(self.lastname_field, lastname)
        self.write_element(self.postalcode_field, postalcode)
        self.click_element(self.btn_continue_checkout)
