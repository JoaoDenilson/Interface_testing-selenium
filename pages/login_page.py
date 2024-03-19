from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_field = (By.ID, "login-button")
        self.error_message_login = (By.XPATH, "//*[@data-test='error']")

    def to_login(self, user, password):
        self.write_element(self.username_field, user)
        self.write_element(self.password_field, password)
        self.click_element(self.login_field)

    def invalid_login(self):
        self.check_element(self.error_message_login)

    def check_text_message_error_login(self, expected_text):
        found_text = self.get_text_element(self.error_message_login)
        assert found_text == expected_text, f"The text returns is '{found_text}', but expected is '{expected_text}'"
