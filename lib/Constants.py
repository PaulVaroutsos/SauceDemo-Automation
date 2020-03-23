"""Constant variables used throughout the framework."""
from enum import Enum
from selenium import webdriver


class Mode(Enum):
    """Browsers modes used for test fixtures."""
    HEADLESS = "headless"
    MOBILE = "mobile"
    DESKTOP = "desktop"


# Devices
IPHONE_X = "iPhone X"

# Webdrivers
CHROME_MOBILE = (webdriver.Chrome, Mode.MOBILE, IPHONE_X)
CHROME_DESKTOP = (webdriver.Chrome, Mode.DESKTOP, None)
CHROME_HEADLESS = (webdriver.Chrome, Mode.HEADLESS, None)
FIREFOX_DESKTOP = (webdriver.Firefox, Mode.DESKTOP, None)
FIREFOX_MOBILE = (webdriver.Firefox, Mode.MOBILE, None)
DEFAULT = CHROME_HEADLESS

# Strings
REMOVE = "REMOVE"
ADD_TO_CART = "ADD TO CART"
