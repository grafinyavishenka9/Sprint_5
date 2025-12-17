from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import Credentials
from locators import Locators
from url import *


class TestLogin:

    def test_success_login_by_button_on_main_page(self, driver_login):
        driver_login.find_element(*Locators.ENTER_TO_ACCOUNT_MAIN_PAGE).click()
        driver_login.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.EMAIL)
        driver_login.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.PASSWORD)
        driver_login.find_element(*Locators.LOGIN_BUTTON).click()
        reg_text = WebDriverWait(driver_login, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.LOGIN_SUCCESS_VERIFY_ELEMENT)).text
        assert 'Оформить заказ' == reg_text
        assert driver_login.current_url == main_site

    def test_success_login_by_button_lk(self, driver_login):
        driver_login.find_element(*Locators.ENTER_TO_ACCOUNT_LK).click()
        driver_login.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.EMAIL)
        driver_login.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.PASSWORD)
        driver_login.find_element(*Locators.LOGIN_BUTTON).click()
        reg_text = WebDriverWait(driver_login, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.LOGIN_SUCCESS_VERIFY_ELEMENT)).text
        assert 'Оформить заказ' == reg_text
        assert driver_login.current_url == main_site

    def test_success_login_by_button_zareg(self, driver_login):
        driver_login.find_element(*Locators.ENTER_TO_ACCOUNT_LK).click()
        driver_login.find_element(*Locators.ENTER_TO_ACCOUNT_ZAREG).click()
        driver_login.find_element(*Locators.ENTER_TO_ACCOUNT_ZAREG_ENTER).click()
        driver_login.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.EMAIL)
        driver_login.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.PASSWORD)
        driver_login.find_element(*Locators.LOGIN_BUTTON).click()
        reg_text = WebDriverWait(driver_login, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.LOGIN_SUCCESS_VERIFY_ELEMENT)).text
        assert 'Оформить заказ' == reg_text
        assert driver_login.current_url == main_site

    def test_success_login_by_restore_password_page(self, driver_login):
        driver_login.find_element(*Locators.ENTER_TO_ACCOUNT_MAIN_PAGE).click()
        driver_login.find_element(*Locators.ENTER_TO_ACCOUNT_RESTORE_PASSWORD_PAGE).click()
        driver_login.find_element(*Locators.ENTER_TO_ACCOUNT_RESTORE_PASSWORD_PAGE_ENTER).click()
        driver_login.find_element(*Locators.ENTER_TO_ACCOUNT_ZAREG).click()
        driver_login.find_element(*Locators.ENTER_TO_ACCOUNT_ZAREG_ENTER).click()
        driver_login.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.EMAIL)
        driver_login.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.PASSWORD)
        driver_login.find_element(*Locators.LOGIN_BUTTON).click()
        reg_text = WebDriverWait(driver_login, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.LOGIN_SUCCESS_VERIFY_ELEMENT)).text
        assert 'Оформить заказ' == reg_text
        assert driver_login.current_url == main_site
