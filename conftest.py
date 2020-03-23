#!/usr/bin/env python
"""Test configuration for pytest"""
import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from lib.Constants import Mode

@pytest.fixture
def driver(request, browser, mode, device):
    """Creates test fixtures for pytest."""
    if browser == webdriver.Chrome:
        if mode == Mode.MOBILE:
            options = webdriver.ChromeOptions()
            mobile_emulation = {"deviceName": device}
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            web_driver = browser("./drivers/chromedriver", options=options)
        elif mode == Mode.HEADLESS:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            web_driver = browser("./drivers/chromedriver", options=options)
        else:
            web_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == webdriver.Firefox:
        web_driver = webdriver.Firefox(executable_path='./drivers/geckodriver')
    else:
        raise NameError("Unsupported browser: %s" % browser)

    web_driver.delete_all_cookies()

    # Close/quit browser after the test is completed.
    request.addfinalizer(lambda *args: mac_finalizer(web_driver))
    return web_driver


def mac_finalizer(web_driver):
    """Close/quit browser after the test is completed."""
    web_driver.close()
    web_driver.quit()
    time.sleep(2)
