import time
import pytest
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.cart
@pytest.mark.smoke
class TestAddProductToCart:
    def test_add_product_cart(self):
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()

        # Variables
        product01 = "Sauce Labs Backpack"
        product02 = "Sauce Labs Bike Light"

        # Taking Login
        login_page.to_login("standard_user", "secret_sauce")

        # Add item to cart
        home_page.add_to_cart(product01)

        # # Checking that the item has been added to the cart
        home_page.click_cart()
        cart_page.check_product_cart(product01)

        # Returning to view products
        cart_page.click_continue_shopping()

        # # Add item 2 to cart
        home_page.add_to_cart(product02)

        # # Checking all items has been added to the cart
        home_page.click_cart()
        cart_page.check_product_cart(product01)
        cart_page.check_product_cart(product02)
