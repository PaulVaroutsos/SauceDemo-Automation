""" POM of the Product Detail page. """
from selenium.webdriver.common.by import By
from pages.Page import Page


class ProductDetailPage(Page):
    """ Product Detail Page class """

    def __init__(self, driver):
        super().__init__(driver)
        self.price_selector = (By.CLASS_NAME, "inventory_details_price")
        self.add_to_cart_button_selector = (By.CLASS_NAME, "btn_inventory")
        self.back_button_selector = (By.CLASS_NAME, "inventory_details_back_button")
        self.product_name_selector = (By.CLASS_NAME, "inventory_details_name")
        self.cart_item_count_selector = (By.CLASS_NAME, "shopping_cart_badge")

    def get_price(self):
        """ Get the subheader text. Used to assert that the driver is on the cart page. """
        element = self.driver.find_element(*self.price_selector)
        return element.text

    def get_product_name(self):
        """Get a product's name."""
        element = self.driver.find_element(*self.product_name_selector)
        return element.text

    def get_product_price(self):
        """Get a product's price."""
        element = self.driver.find_element(*self.price_selector)
        return element.text

    def get_number_cart_items(self):
        """ Get the number of items in the cart. """
        has_items_in_cart = len(self.driver.find_elements(*self.cart_item_count_selector)) > 0
        if has_items_in_cart:
            num_items_in_cart = self.driver.find_element(*self.cart_item_count_selector).text
            return int(num_items_in_cart)
        else:
            return 0

    def click_add_to_cart(self):
        """Click the add to cart button."""
        self.click_element(self.add_to_cart_button_selector)

    def click_back(self):
        """Click the back button."""
        self.click_element(self.back_button_selector)
