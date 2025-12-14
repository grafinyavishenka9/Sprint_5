from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import Credentials
from helper import generate_random_credentials
from locators import Locators
from url import *
import time
class TestRegistrationWithNewCredentials:

    def test_success_registration(self, driver_registration):                
        driver_registration.find_element(*Locators.REGISTRATION_NAME).send_keys(Credentials.NAME)
        driver_registration.find_element(*Locators.REGISTRATION_EMAIL).send_keys(Credentials.EMAIL)
        driver_registration.find_element(*Locators.REGISTRATION_PASSWORD).send_keys(Credentials.PASSWORD)
        driver_registration.find_element(*Locators.REGISTRATION_BUTTON).click()
        time.sleep(1)
        assert driver_registration.current_url == main_site + "login"

class TestRegistrationWithWrongPassword:

    def test_registration_with_wrong_password(self, driver_registration):        
        name, email, password = generate_random_credentials()        
        driver_registration.find_element(*Locators.REGISTRATION_NAME).send_keys(name)
        driver_registration.find_element(*Locators.REGISTRATION_EMAIL).send_keys(email)
        driver_registration.find_element(*Locators.REGISTRATION_PASSWORD).send_keys(Credentials.WRONG_PASSWORD)
        driver_registration.find_element(*Locators.REGISTRATION_BUTTON).click()
        reg_text = WebDriverWait(driver_registration, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.REGISTRATION_WRONG_PASSWORD_ERROR)).text
        assert 'Некорректный пароль' == reg_text
        assert driver_registration.current_url == main_site + "register"
