import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from url import *
from credentials import Credentials
from locators import Locators


@pytest.fixture()
def driver_registration():
    options = ChromeOptions()
    options.add_argument("--window-size=1600,900")
    options.add_experimental_option("prefs", {
            "profile.password_manager_leak_detection": False
        })
    options.add_argument('--headless')
    browser  = webdriver.Chrome(options=options)
    browser.get(reg_form)
    yield browser
    browser.quit()

@pytest.fixture()
def driver_login():
    options = ChromeOptions()
    options.add_argument("--window-size=1600,900")
    options.add_experimental_option("prefs", {
            "profile.password_manager_leak_detection": False
        })
    options.add_argument('--headless')
    browser  = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()

@pytest.fixture
def driver_with_login():
    options = ChromeOptions()
    options.add_argument("--window-size=1600,900")
    options.add_experimental_option("prefs", {
            "profile.password_manager_leak_detection": False
        })
    options.add_argument('--headless')
    browser  = webdriver.Chrome(options=options)
    browser.get(main_site)
    browser.find_element(*Locators.ENTER_TO_ACCOUNT_MAIN_PAGE).click()
    browser.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.EMAIL)
    browser.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.PASSWORD)
    browser.find_element(*Locators.LOGIN_BUTTON).click()
    yield browser
    browser.quit()
    