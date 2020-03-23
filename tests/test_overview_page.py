"""Test the overview page of saucedemo.com. (The page just before completing the order.)"""
import pytest
import lib.LoginCreds as LoginCreds
from lib.Constants import CHROME_MOBILE, CHROME_HEADLESS
from pages.CartPage import CartPage
from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage
from pages.CheckoutPage import CheckoutPage
from pages.OrderConfirmationPage import OrderConfirmationPage
from pages.OverviewPage import OverviewPage


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.checkout
def test_cancel_button(driver, browser, mode, device, username, password):
    """Test the overview page's cancel button."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_list_page = ProductListPage(driver)
    product_list_page.click_cart()
    cart_page = CartPage(driver)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.input_first_name("test")
    checkout_page.input_last_name("test")
    checkout_page.input_postal_code("123456")
    checkout_page.click_continue()
    overview_page = OverviewPage(driver)
    overview_page.click_cancel()
    assert product_list_page.get_subheader() == "Products"


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.checkout
def test_finish_button(driver, browser, mode, device, username, password):
    """Test the overview page's finish order button."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_page = ProductListPage(driver)
    product_page.click_cart()
    cart_page = CartPage(driver)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.input_first_name("test")
    checkout_page.input_last_name("test")
    checkout_page.input_postal_code("123456")
    checkout_page.click_continue()
    overview_page = OverviewPage(driver)
    overview_page.click_finish()
    order_confirmation_page = OrderConfirmationPage(driver)
    assert order_confirmation_page.get_subheader() == "Finish"
