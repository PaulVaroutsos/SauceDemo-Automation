"""Testing the login page of saucedemo.com"""
import pytest
import lib.LoginCreds as LoginCreds
from lib.Constants import CHROME_MOBILE, CHROME_HEADLESS
from pages.LoginPage import LoginPage


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.STANDARD_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.STANDARD_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.login
@pytest.mark.login_success
def test_login_valid_user(driver, browser, mode, device, username, password):
    """Test logging in with a valid username/password."""
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    assert not login_page.error_message_exists()
    print("Test finished.")


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.LOCKED_OUT_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.LOCKED_OUT_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.login
@pytest.mark.login_lockedout
def test_login_locked_out_user(driver, browser, mode, device, username, password):
    """Test logging in with a user who is locked out."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    assert login_page.error_message_exists()
    print(login_page.get_error_message_text())
    print("test_login_locked_out_user finished successfully.")


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.STANDARD_USER, "abc123"),
        (*CHROME_HEADLESS, "notauser", LoginCreds.DROP_TABLES),
    ],
)
@pytest.mark.login
@pytest.mark.login_incorrect
def test_login_incorrect_credentials(driver, browser, mode, device, username, password):
    """Test attempting to log in with invalid credentials."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    assert login_page.error_message_exists()
    print(login_page.get_error_message_text())
    print("test_login_incorrect_credentials finished successfully.")

@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.EMPTY_STRING, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.EMPTY_STRING, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.login
@pytest.mark.login_incorrect
def test_login_missing_username(driver, browser, mode, device, username, password):
    """Test attempting to log in with a blank username."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    assert login_page.error_message_exists()
    print(login_page.get_error_message_text())
    print("test_login_missing_username finished successfully.")

@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*CHROME_MOBILE, LoginCreds.STANDARD_USER, LoginCreds.EMPTY_STRING),
        (*CHROME_HEADLESS, LoginCreds.STANDARD_USER, LoginCreds.EMPTY_STRING),
    ],
)
@pytest.mark.login
@pytest.mark.login_nopassword
def test_login_missing_password(driver, browser, mode, device, username, password):
    """Test attempting to log in with a blank password."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    assert login_page.error_message_exists()
    print(login_page.get_error_message_text())
    print("test_login_missing_password finished successfully.")
