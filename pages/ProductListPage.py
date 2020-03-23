""" POM class for the Product page. """
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Page import Page


class ProductListPage(Page):
    """ Product page class. """
    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_buttons_selector = (By.CLASS_NAME, "btn_primary")
        self.hamburger_menu_selector = (
            By.CSS_SELECTOR, "#menu_button_container > div > div:nth-child(3) > div > button"
        )
        self.cart_item_count_selector = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_selector = (By.CLASS_NAME, "shopping_cart_link")
        self.inventory_item_name_selector = (By.CLASS_NAME, "inventory_item_name")
        self.inventory_item_price_selector = (By.CLASS_NAME, "inventory_item_price")
        self.inventory_item_selector = (By.CLASS_NAME, "inventory_item")
        self.inventory_list_selector = (By.CLASS_NAME, "inventory_list")
        self.sort_a_to_z_selector = (
            By.CSS_SELECTOR, "#inventory_filter_container > select > option:nth-child(1)"
        )
        self.sort_z_to_a_selector = (
            By.CSS_SELECTOR, '#inventory_filter_container > select > option:nth-child(2)'
        )
        self.sort_low_to_high_selector = (
            By.CSS_SELECTOR, "#inventory_filter_container > select > option:nth-child(3)"
        )
        self.sort_high_to_low_selector = (
            By.CSS_SELECTOR, "#inventory_filter_container > select > option:nth-child(4)"
        )
        self.sort_menu_selector = (
            By.CSS_SELECTOR, "#inventory_filter_container > select"
        )
        self.ADD_TO_CART_BUTTON_XPATH = ".//div[3]/button"
        self.URL_XPATH = ".//div[2]/a"
        self.subheader_selector = (By.CLASS_NAME, 'product_label')

    def click_cart(self):
        """ Click the cart button. """
        self.click_element(self.cart_selector)

    def click_hamburger_menu(self):
        """ Open the hamburger menu. """
        self.click_element(self.hamburger_menu_selector)

    def click_product_sort_menu(self):
        """ Click the product sort menu. """
        self.click_element(self.sort_menu_selector)

    def get_add_to_cart_buttons(self):
        """ Get the element of all add to cart buttons on the PLP. """
        buttons = self.driver.find_elements(*self.add_to_cart_buttons_selector)
        return buttons

    def get_all_product_elements(self):
        """ Get the element of all products on the PLP. """
        products = self.driver.find_elements(*self.inventory_item_selector)
        return products

    def get_list_of_product_names(self):
        """ Get the name of all products on the PLP. """
        products = self.driver.find_elements(*self.inventory_item_name_selector)
        return [item.text for item in products]

    def get_subheader(self):
        """ Get the subheader text. Used to assert that the driver is on the cart page. """
        element = self.driver.find_element(*self.subheader_selector)
        return element.text

    def get_number_cart_items(self):
        """ Get the number of items in the cart. """
        has_items_in_cart = len(self.driver.find_elements(*self.cart_item_count_selector)) > 0
        if has_items_in_cart:
            num_items_in_cart = self.driver.find_element(*self.cart_item_count_selector).text
            return int(num_items_in_cart)
        else:
            return 0

    def get_list_of_product_prices(self):
        """ Get the price of all products on the PLP. """
        products = self.driver.find_elements(*self.inventory_item_price_selector)
        return [float(item.text.replace("$", "")) for item in products]

    def sort_products_a_to_z(self):
        """ Sort products A to Z. """
        self.click_product_sort_menu()
        sort_option = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.sort_a_to_z_selector)
        )
        sort_option.click()

    def sort_products_low_to_high(self):
        """ Sort products low to high. """
        self.click_product_sort_menu()
        sort_option = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.sort_low_to_high_selector)
        )
        sort_option.click()

    def sort_products_high_to_low(self):
        """ Sort products high to low. """
        self.click_product_sort_menu()
        sort_option = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.sort_high_to_low_selector)
        )
        sort_option.click()

    def sort_products_z_to_a(self):
        """ Sort products Z to A. """
        self.click_product_sort_menu()
        sort_option = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.sort_z_to_a_selector)
        )
        sort_option.click()

    def add_all_to_cart(self):
        """ Add all products on the PLP to the cart. """
        product_elements = self.get_all_product_elements()
        for product in product_elements:
            add_cart_button = product.find_element_by_xpath(self.ADD_TO_CART_BUTTON_XPATH)
            add_cart_button.click()
