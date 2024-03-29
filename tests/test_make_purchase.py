import time

import pytest
from pages.cart_page import CartPage
from pages.check_order_page import CheckOrderPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.order_page import OrderPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.smoke
class TestMakePurchase:
    def test_make_purchase(self):
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        checkout_page = CheckoutPage()
        check_order_page = CheckOrderPage()
        order_page = OrderPage()


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

        # Check-out all cart item
        cart_page.click_checkout()

        # # Fill purchase data , postalcode
        checkout_page.form_checkout("João", "Denilson", "63452-222")

        # # Checkout: Overview | Finalizing purchase
        check_order_page.click_order_finish()

        # Checking purchase order
        order_page.finish_order()
