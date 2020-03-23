"""Test the entire checkout process of saucedemo.com"""
import random
import time
import pytest
import lib.LoginCreds as LoginCreds
from lib.Constants import CHROME_MOBILE, CHROME_HEADLESS, REMOVE
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.LoginPage import LoginPage
from pages.OrderConfirmationPage import OrderConfirmationPage
from pages.OverviewPage import OverviewPage
from pages.ProductListPage import ProductListPage


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.checkout
@pytest.mark.full_checkout
def test_checkout_all_items(driver, browser, mode, device, username, password):
    """Test the checkout process with all items on the PLP."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_list_page = ProductListPage(driver)
    add_to_cart_buttons = product_list_page.get_add_to_cart_buttons()
    num_items_in_cart = 0
    assert product_list_page.get_number_cart_items() == num_items_in_cart, \
        "An unexpected item has been found in the cart."

    # Add products, check mini cart total.
    for button in add_to_cart_buttons:
        button.click()
        num_items_in_cart += 1
        assert num_items_in_cart == product_list_page.get_number_cart_items(), \
            "An unexpected item has been found in the cart."
        time.sleep(1)
        assert button.text == REMOVE

    assert product_list_page.get_number_cart_items() == len(add_to_cart_buttons), \
        "Unexpected number of cart items"
    product_list_page.click_cart()

    # Continue to the checkout page from the cart page.
    cart_page = CartPage(driver)
    cart_total = cart_page.get_sum_prices()
    cart_page.click_checkout()

    # Attempt to checkout without entering a name and postal code.
    checkout_page = CheckoutPage(driver)
    checkout_page.click_continue()
    assert checkout_page.is_error_message_present()

    # Checkout with valid information
    first_name = "Testy"
    last_name = "McTest"
    postal_code = "08221"
    checkout_page.input_first_name(first_name)
    checkout_page.input_last_name(last_name)
    checkout_page.input_postal_code(postal_code)
    checkout_page.input_payment_details()
    assert checkout_page.get_first_name() == first_name
    assert checkout_page.get_last_name() == last_name
    assert checkout_page.get_postal_code() == postal_code
    checkout_page.click_continue()

    # Check the overview page before completing the order.
    overview_page = OverviewPage(driver)
    assert overview_page.get_subheader() == "Checkout: Overview"
    assert cart_total == overview_page.get_subtotal()
    overview_page.click_finish()

    # Check the order confirmation page.
    order_confirmation_page = OrderConfirmationPage(driver)
    assert order_confirmation_page.get_subheader() == "Finish"
    assert product_list_page.get_number_cart_items() == 0, "Unexpected item found in cart."


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.checkout
@pytest.mark.full_checkout
def test_checkout_one_item(driver, browser, mode, device, username, password):
    """Test the checkout process with one item."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_list_page = ProductListPage(driver)
    add_to_cart_buttons = product_list_page.get_add_to_cart_buttons()
    num_items_in_cart = 0
    assert product_list_page.get_number_cart_items() == num_items_in_cart, \
        "An unexpected item has been found in the cart."
    item_button = random.choice(add_to_cart_buttons)
    item_button.click()
    assert item_button.text == REMOVE
    assert product_list_page.get_number_cart_items() == 1, \
        "An unexpected item has been found in the cart."

    # Continue to the cart page
    product_list_page.click_cart()
    cart_page = CartPage(driver)
    cart_total = cart_page.get_sum_prices()
    cart_page.click_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.click_continue()
    assert checkout_page.is_error_message_present()

    # Input checkout information.
    first_name = "Testy"
    last_name = "McTest"
    postal_code = "08221"
    checkout_page.input_first_name(first_name)
    checkout_page.input_last_name(last_name)
    checkout_page.input_postal_code(postal_code)
    checkout_page.input_payment_details()  # A real e-commerce site would allow you to add payment info.
    assert checkout_page.get_first_name() == first_name
    assert checkout_page.get_last_name() == last_name
    assert checkout_page.get_postal_code() == postal_code
    checkout_page.click_continue()

    # Check the overview page before completing the order.
    overview_page = OverviewPage(driver)
    assert overview_page.get_subheader() == "Checkout: Overview"
    assert cart_total == overview_page.get_subtotal()
    overview_page.click_finish()

    # Check the order confirmation page.
    order_confirmation_page = OrderConfirmationPage(driver)
    assert order_confirmation_page.get_subheader() == "Finish"
    assert product_list_page.get_number_cart_items() == 0, "Unexpected item found in cart."


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.checkout
@pytest.mark.full_checkout
@pytest.mark.xpass(reason="SwagLabs allows this even when logging in with standard_user.")
def test_checkout_no_items(driver, browser, mode, device, username, password):
    """Checkout with no items.  SwagLabs allows this even when logging in with standard_user."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_list_page = ProductListPage(driver)
    product_list_page.click_cart()

    # Continue to cart page with no items.
    cart_page = CartPage(driver)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.click_continue()
    assert checkout_page.is_error_message_present()

    # Enter name and postal code
    first_name = "Testy"
    last_name = "McTest"
    postal_code = "08221"
    checkout_page.input_first_name(first_name)
    checkout_page.input_last_name(last_name)
    checkout_page.input_postal_code(postal_code)
    checkout_page.input_payment_details()
    assert checkout_page.get_first_name() == first_name
    assert checkout_page.get_last_name() == last_name
    assert checkout_page.get_postal_code() == postal_code
    checkout_page.click_continue()

    # Check the overview page before completing the order.
    overview_page = OverviewPage(driver)
    assert overview_page.get_subheader() == "Checkout: Overview"
    overview_page.click_finish()

    # Check the order confirmation page.
    order_confirmation_page = OrderConfirmationPage(driver)
    assert order_confirmation_page.get_subheader() == "Finish"
    assert product_list_page.get_number_cart_items() == 0, "Unexpected item found in cart."
