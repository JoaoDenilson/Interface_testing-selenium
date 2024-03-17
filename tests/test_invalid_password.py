import pytest
from selenium.webdriver.common.by import By
import conftest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.smoke
class TestInvalidLogin:
    def test_invalid_login(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce-error")
        driver.find_element(By.ID, "login-button").click()

        h3element = driver.find_element(By.XPATH, "//*[@id='login_button_container' ]/div/form/div[3]/h3")
        assert h3element.text == "Epic sadface: Username and password do not match any user in this service"
        # assert driver.find_element(By.XPATH, "//span[@class='title']") == 0
