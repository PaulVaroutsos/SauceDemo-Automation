""" POM of the OrderConfirmationPage page. """
from selenium.webdriver.common.by import By
from pages.Page import Page


class OrderConfirmationPage(Page):
    """ OrderConfirmationPage class """

    def __init__(self, driver):
        super().__init__(driver)
        self.subheader_selector = (By.CLASS_NAME, 'subheader')

    def get_subheader(self):
        """ Get the subheader text. Used to assert that the driver is on the cart page. """
        element = self.driver.find_element(*self.subheader_selector)
        return element.text
