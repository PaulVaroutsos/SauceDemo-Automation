"""Test the product details page (PDP) of saucedemo.com"""
import random
import pytest
import lib.LoginCreds as LoginCreds
from lib.Constants import CHROME_MOBILE, CHROME_HEADLESS
from pages.ProductDetailPage import ProductDetailPage
from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.pdp
def test_back_button(driver, browser, mode, device, username, password):
    """Test the PDP's back button."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_list_page = ProductListPage(driver)

    # Get a random product
    products = product_list_page.get_all_product_elements()
    index = random.randrange(0, len(products))
    product = products[index]
    product_url = product.find_element_by_xpath(product_list_page.URL_XPATH).get_attribute("href")
    driver.get(product_url)
    pdp = ProductDetailPage(driver)
    pdp.click_back()
    assert product_list_page.get_subheader() == "Products"

@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.pdp
def test_add_to_cart_button(driver, browser, mode, device, username, password):
    """Test the PDP's add to cart button."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_list_page = ProductListPage(driver)

    # Get a random product
    products = product_list_page.get_all_product_elements()
    index = random.randrange(0, len(products))
    product = products[index]
    product_url = product.find_element_by_xpath(product_list_page.URL_XPATH).get_attribute("href")
    driver.get(product_url)
    pdp = ProductDetailPage(driver)
    pdp.click_add_to_cart()
    assert pdp.get_number_cart_items() == 1


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.pdp
def test_remove_from_cart_button(driver, browser, mode, device, username, password):
    """Test the PDP's remove from cart button."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_list_page = ProductListPage(driver)

    # Get a random product
    products = product_list_page.get_all_product_elements()
    index = random.randrange(0, len(products))
    product = products[index]
    add_cart_button = product.find_element_by_xpath(product_list_page.ADD_TO_CART_BUTTON_XPATH)
    add_cart_button.click()
    product_url = product.find_element_by_xpath(product_list_page.URL_XPATH).get_attribute("href")
    driver.get(product_url)
    pdp = ProductDetailPage(driver)
    pdp.click_add_to_cart()
    assert pdp.get_number_cart_items() == 0
