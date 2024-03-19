import time

import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.smoke
class TestInvalidLogin:
    def test_invalid_login(self):
        expected_message_erro = "Epic sadface: Username and password do not match any user in this service"

        # Instancia os Objetos usados no test
        login_page = LoginPage()
        home_page = HomePage()

        # Login
        login_page.to_login("standard_user", "error_password")

        # Verifica se o Login invalido
        login_page.invalid_login()

        # Verifica o texto da mensagem de error
        login_page.check_text_message_error_login(expected_message_erro)
