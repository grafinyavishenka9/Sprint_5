from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import Credentials
from locators import Locators
from url import *
import time
class TestSuccessEnterInLK:

    def test_success_enter_in_lk(self, driver_with_login):
        driver_with_login.find_element(*Locators.ENTER_TO_LK_BUTTON).click()
        reg_text = WebDriverWait(driver_with_login, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.LK_VERIFY)).text
        assert 'Профиль' == reg_text
        assert driver_with_login.current_url == main_site + 'account/profile'

class TestMoveFromLK_To_Constructor:

    def test_move_from_lk_to_constructor(self, driver_with_login):
        driver_with_login.find_element(*Locators.ENTER_TO_LK_BUTTON).click()
        driver_with_login.find_element(*Locators.LK_TO_CONSTRUCTOR).click()
        reg_text = WebDriverWait(driver_with_login, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_VERIFY)).text
        assert 'Соберите бургер' == reg_text
        assert driver_with_login.current_url == main_site

class TestMoveFromLK_To_Logo:

    def test_move_from_lk_to_logo(self, driver_with_login):
        driver_with_login.find_element(*Locators.ENTER_TO_LK_BUTTON).click()
        driver_with_login.find_element(*Locators.LK_TO_LOGO).click()
        assert driver_with_login.current_url == main_site

class TestExitFromLK:

    def test_exit_from_lk(self, driver_with_login):
        driver_with_login.find_element(*Locators.ENTER_TO_LK_BUTTON).click()
        time.sleep(1)
        driver_with_login.find_element(*Locators.EXIT_FROM_LK).click()
        time.sleep(1)
        reg_text = WebDriverWait(driver_with_login, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.EXIT_FROM_LK_VERIFY)).text
        assert 'Вход' == reg_text
        assert driver_with_login.current_url == main_site + 'login'
        