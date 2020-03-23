""" POM Base class for all other Page classes. """
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import lib.LoginCreds as LoginCreds


class Page:
    """ Page class. """
    def __init__(self, driver):
        self.driver = driver
        self.url = LoginCreds.URL

    def init_site(self):
        """ Initialize the URL. """
        self.driver.get(self.url)

    def click_element(self, selector, wait_time=5):
        """
        Click on aan element identified by 'selector'
        :param selector: The selector of the element to click
        :param wait_time: Time to wait before timing out, default 5 seconds
        :return: None
        """
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(selector)
        )
        element.click()

    def send_keys_to_element(self, selector, text, wait_time=5):
        """ Enter a username into the username textbox. """
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(selector)
        )
        element.send_keys(text)
