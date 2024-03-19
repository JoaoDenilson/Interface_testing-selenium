import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.smoke
class TestLogin:
    def test_valid_login(self):
        # Instancia os Objetos usados no test
        login_page = LoginPage()
        home_page = HomePage()

        # Login
        login_page.to_login("standard_user", "secret_sauce")

        # Verifica se o Login foi realizado com sucesso
        home_page.check_valid_login()
