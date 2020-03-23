"""Test the product list page (PLP) of saucedemo.com"""
import time
import pytest
import lib.Constants as Constants
import lib.LoginCreds as LoginCreds
from lib.Constants import CHROME_MOBILE, CHROME_HEADLESS
from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage
from pages.ProductDetailPage import ProductDetailPage


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.product_page
def test_get_products(driver, browser, mode, device, username, password):
    """Test getting all product names from the PLP."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_page = ProductListPage(driver)
    product_names = product_page.get_list_of_product_names()
    for name in product_names:
        print("PLP has product with name: %s" % name)
    assert len(product_names) > 0, "No products found on the PLP."
    print("test_get_products finished successfully.")


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.product_page
@pytest.mark.product_sort
def test_sort_a_to_z(driver, browser, mode, device, username, password):
    """Test sorting the PLP's products in alphabetical order."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_page = ProductListPage(driver)
    product_page.sort_products_a_to_z()
    product_names = product_page.get_list_of_product_names()
    for i in range(len(product_names)-1):
        assert product_names[i] <= product_names[i+1], "Products {0} and {1} are not ordered correctly.".format(product_names[i], product_names[i+1])
    print("test_sort_a_to_z finished successfully.")

@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.product_page
@pytest.mark.product_sort
def test_sort_z_to_a(driver, browser, mode, device, username, password):
    """Test sorting the PLP's products in reverse alphabetical order."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_page = ProductListPage(driver)
    product_page.sort_products_z_to_a()
    product_names = product_page.get_list_of_product_names()
    for i in range(len(product_names)-1):
        assert product_names[i] >= product_names[i+1], \
            "Products {0} and {1} are not ordered correctly.".format(product_names[i], product_names[i+1])
    print("test_sort_z_to_a finished successfully.")

@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.product_page
@pytest.mark.product_sort
def test_sort_low_to_high(driver, browser, mode, device, username, password):
    """Test sorting the PLP's products by price in ascending order."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_page = ProductListPage(driver)
    product_page.sort_products_low_to_high()
    product_prices = product_page.get_list_of_product_prices()
    for i in range(len(product_prices)-1):
        assert product_prices[i] <= product_prices[i+1], \
            "Products {0} and {1} are not ordered correctly.".format(product_prices[i], product_prices[i+1])
    print("test_sort_low_to_high finished successfully.")

@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.product_page
@pytest.mark.product_sort
def test_sort_high_to_low(driver, browser, mode, device, username, password):
    """Test sorting the PLP's products by price in descending order."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_page = ProductListPage(driver)
    product_page.sort_products_high_to_low()
    product_prices = product_page.get_list_of_product_prices()
    for i in range(len(product_prices)-1):
        assert product_prices[i] >= product_prices[i+1], \
            "Products {0} and {1} are not ordered correctly.".format(product_prices[i], product_prices[i+1])
    print("test_sort_high_to_low finished successfully.")


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.product_page
@pytest.mark.add_cart
def test_add_to_cart(driver, browser, mode, device, username, password):
    """Test adding items to the cart."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_page = ProductListPage(driver)
    product_elements = product_page.get_all_product_elements()
    num_items_in_cart = 0
    assert product_page.get_number_cart_items() == num_items_in_cart, "An unexpected item has been found in the cart."

    # Add products, check mini cart total.
    for product in product_elements:
        add_cart_button = product.find_element_by_xpath(product_page.ADD_TO_CART_BUTTON_XPATH)
        add_cart_button.click()
        num_items_in_cart += 1
        assert num_items_in_cart == product_page.get_number_cart_items(), "An unexpected item has been found in the cart."
        time.sleep(1)
        assert add_cart_button.text == Constants.REMOVE

    # Remove products, check mini cart total.
    for product in product_elements:
        remove_cart_button = product.find_element_by_xpath(product_page.ADD_TO_CART_BUTTON_XPATH)
        remove_cart_button.click()
        num_items_in_cart -= 1
        assert num_items_in_cart == product_page.get_number_cart_items(), "An unexpected item has been found in the cart."
        time.sleep(1)
        assert remove_cart_button.text == Constants.ADD_TO_CART


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.product_page
@pytest.mark.plp_images
def test_plp_images(driver, browser, mode, device, username, password):
    """Test that each product's image link is not broken."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_page = ProductListPage(driver)
    product_elements = product_page.get_all_product_elements()
    image_urls = []
    for product in product_elements:
        image = product.find_element_by_xpath(".//div[1]/a/img")
        image_urls.append(image.get_attribute("src"))

    broken_image_links = []
    for url in image_urls:
        driver.get(url)
        errors = driver.find_elements_by_css_selector(
            "#webkit-xml-viewer-source-xml > Error > Message"
        )
        if len(errors) > 0:
            print("Image source not found:" + url)
            broken_image_links.append(url)

    print(broken_image_links)
    assert len(broken_image_links) == 0, str(len(broken_image_links)) + " image sources not found."

@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.product_page
@pytest.mark.plp_links
def test_plp_links(driver, browser, mode, device, username, password):
    """ Test to ensure that the PLP product link properly redirects to the associated PDP."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_page = ProductListPage(driver)
    product_elements = product_page.get_all_product_elements()

    product_link_map = {}
    for product in product_elements:
        product_name = product.find_element_by_class_name("inventory_item_name").text
        product_url = product.find_element_by_xpath(".//div[2]/a").get_attribute("href")
        product_link_map[product_name] = product_url

    bad_links = []
    for product, link in product_link_map.items():
        driver.get(link)
        pdp_page = ProductDetailPage(driver)
        pdp_product_name = pdp_page.get_product_name()
        if pdp_product_name != product:
            print("The PLP link for {0} was not correct: {1}".format(product, link))
            bad_links.append(product)

    assert len(bad_links) == 0, str(len(bad_links)) + " incorrect links were found on the PLP."

@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.TEST_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.product_page
@pytest.mark.plp_prices
def test_plp_prices(driver, browser, mode, device, username, password):
    """ Check that the PLP prices match the PDP prices. """
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    product_page = ProductListPage(driver)
    product_elements = product_page.get_all_product_elements()

    product_link_map = {}
    product_price_map = {}
    for product in product_elements:
        product_name = product.find_element_by_class_name("inventory_item_name").text
        product_url = product.find_element_by_xpath(".//div[2]/a").get_attribute("href")
        product_price = product.find_element_by_class_name("inventory_item_price").text
        product_link_map[product_name] = product_url
        product_price_map[product_name] = product_price

    bad_prices = []
    for product, link in product_link_map.items():
        driver.get(link)
        pdp_page = ProductDetailPage(driver)
        pdp_price = pdp_page.get_price()
        if pdp_price != product_price_map[product]:
            print("The price for {0} was not correct: {1}".format(product, pdp_price))
            bad_prices.append(product)
        time.sleep(3)

    assert len(bad_prices) == 0, str(len(bad_prices)) + " incorrect prices were found on the PLP."
