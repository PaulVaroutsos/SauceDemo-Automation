"""Testing the cart page of saucedemo.com"""
import pytest
import lib.LoginCreds as LoginCreds
from lib.Constants import CHROME_MOBILE, CHROME_HEADLESS
from pages.CartPage import CartPage
from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.cart
def test_continue_shopping_button(driver, browser, mode, device, username, password):
    """Test the cart page's continue shopping button."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_page = ProductListPage(driver)
    product_page.click_cart()
    cart_page = CartPage(driver)
    cart_page.click_continue_shopping()
    assert len(product_page.get_list_of_product_names()) > 0


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.cart
def test_checkout_button(driver, browser, mode, device, username, password):
    """Test the cart page's checkout button."""
    # Note: SauceDemo intentionally allows you to checkout with no items. This case is explicitly
    # tested in test_cart_page.py in test_checkout_no_items()
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_page = ProductListPage(driver)
    product_page.click_cart()
    cart_page = CartPage(driver)
    cart_page.click_checkout()


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.cart
def test_remove_from_cart(driver, browser, mode, device, username, password):
    """Test the cart page's remove from cart button."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_page = ProductListPage(driver)
    product_page.add_all_to_cart()
    product_page.click_cart()
    cart_page = CartPage(driver)
    cart_page.remove_all_from_cart()
