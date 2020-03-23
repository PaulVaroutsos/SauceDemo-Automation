""" POM of the checkout page. """
from selenium.webdriver.common.by import By
from pages.Page import Page


class CheckoutPage(Page):
    """ Checkout page class. """

    def __init__(self, driver):
        super().__init__(driver)
        self.firstname_textbox_selector = (By.ID, "first-name")
        self.lastname_textbox_selector = (By.ID, "last-name")
        self.postalcode_textbox_selector = (By.ID, "postal-code")
        self.cancel_button_selector = (By.CLASS_NAME, "cart_cancel_link")
        self.continue_button_selector = (By.CLASS_NAME, "btn_primary")
        self.error_message_selector = (By.CLASS_NAME, "error-button")
        self.subheader_selector = (By.CLASS_NAME, 'subheader')

    def input_first_name(self, name):
        """ Input the first name. """
        self.send_keys_to_element(self.firstname_textbox_selector, name)

    def input_last_name(self, name):
        """ Input the last name. """
        self.send_keys_to_element(self.lastname_textbox_selector, name)

    def input_postal_code(self, postal_code):
        """ Input the postal code. """
        self.send_keys_to_element(self.postalcode_textbox_selector, postal_code)

    def input_payment_details(self):
        """
        This is left out of the SauceDemo site. But this is where different payment methods could
        be tested.
        :return: None
        """
        pass

    def get_first_name(self):
        """ Get the text entered into the first name input textbox. """
        element = self.driver.find_element(*self.firstname_textbox_selector)
        return element.get_attribute("value")

    def get_last_name(self):
        """ Get the text entered into the last name input textbox. """
        element = self.driver.find_element(*self.lastname_textbox_selector)
        return element.get_attribute("value")

    def get_postal_code(self):
        """ Get the text entered into the postal code input textbox. """
        element = self.driver.find_element(*self.postalcode_textbox_selector)
        return element.get_attribute("value")

    def is_error_message_present(self):
        """ Checks if there is an error message displayed on the page. """
        error_message = self.driver.find_elements(*self.error_message_selector)
        return len(error_message) > 0

    def click_cancel(self):
        """ Click the cancel button. (Returns to cart page.) """
        self.click_element(self.cancel_button_selector)

    def click_continue(self):
        """ Click the continue button. (Goes to Checkout Overview page.) """
        self.click_element(self.continue_button_selector)

    def get_subheader(self):
        """ Get the subheader text. """
        element = self.driver.find_element(*self.subheader_selector)
        return element.text
