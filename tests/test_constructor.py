from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import Credentials
from locators import Locators
from url import *
import time

class TestConstructor:

    def test_constructor_move_to_sousy(self, driver_login):
        driver_login.find_element(*Locators.MOVE_TO_SOUSY).click()
        time.sleep(3)
        reg_text = WebDriverWait(driver_login, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.MOVE_TO_SOUSY)).text
        is_active = WebDriverWait(driver_login, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.MOVE_TO_SOUSY_VERIFY)).get_attribute("class")
        assert 'Соусы' == reg_text
        assert "tab_tab_type_current__2BEPc" in is_active
        assert driver_login.current_url == main_site

    def test_constructor_move_to_bulki(self, driver_login):
        driver_login.find_element(*Locators.MOVE_TO_NACHINKI).click()
        driver_login.find_element(*Locators.MOVE_TO_BULKI).click()
        time.sleep(3)
        reg_text = WebDriverWait(driver_login, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.MOVE_TO_BULKI)).text
        is_active = WebDriverWait(driver_login, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.MOVE_TO_BULKI_VERIFY)).get_attribute("class")
        assert 'Булки' == reg_text
        assert "tab_tab_type_current__2BEPc" in is_active
        assert driver_login.current_url == main_site

    def test_constructor_move_to_nachinki(self, driver_login):
        driver_login.find_element(*Locators.MOVE_TO_NACHINKI).click()
        time.sleep(3)
        reg_text = WebDriverWait(driver_login, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.MOVE_TO_NACHINKI)).text
        is_active = WebDriverWait(driver_login, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.MOVE_TO_NACHINKI_VERIFY)).get_attribute("class")
        assert 'Начинки' == reg_text
        assert "tab_tab_type_current__2BEPc" in is_active
        assert driver_login.current_url == main_site
