from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import Credentials
from locators import Locators
from url import *
import time
import pytest


class TestConstructor:

    @pytest.mark.parametrize(
        'locators_start, locators_end, locators_verify, ingridient',#locators_start - переключаем на любой пункт меню, кроме тестируемого
                                                                    #locators_end - переключаем на тестируемый пункт меню
                                                                    # сделано по причине некликабельности пункта меню по умолчанию(Булки) 
        [
            [Locators.MOVE_TO_SOUSY, Locators.MOVE_TO_BULKI, Locators.MOVE_TO_BULKI_VERIFY, 'Булки'],
            [Locators.MOVE_TO_NACHINKI, Locators.MOVE_TO_SOUSY, Locators.MOVE_TO_SOUSY_VERIFY, 'Соусы'],            
            [Locators.MOVE_TO_SOUSY, Locators.MOVE_TO_NACHINKI, Locators.MOVE_TO_NACHINKI_VERIFY, 'Начинки']
        ]
    )
    def test_constructor(self, driver_login, locators_start, locators_end, locators_verify, ingridient):
        driver_login.find_element(*locators_start).click()
        driver_login.find_element(*locators_end).click()
        time.sleep(3)
        reg_text = WebDriverWait(driver_login, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(locators_end)).text
        is_active = WebDriverWait(driver_login, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(locators_verify)).get_attribute("class")
        assert ingridient == reg_text
        assert "tab_tab_type_current__2BEPc" in is_active
        assert driver_login.current_url == main_site
