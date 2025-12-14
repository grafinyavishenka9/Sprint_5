from selenium.webdriver.common.by import By


class Locators:

    #Локаторы для регистрации
    REGISTRATION_NAME = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')#поле "Имя" на странице регистрации
    REGISTRATION_EMAIL = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')#поле "Email" на странице регистрации
    REGISTRATION_PASSWORD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')#поле "Пароль" на странице регистрации
    REGISTRATION_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')#кнопка "Зарегистрироваться" на странице регистрации
    REGISTRATION_WRONG_PASSWORD_ERROR = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')#тект ошибки при вводе некорректного пароля на странице регистрации
    
    #Локаторы для логина
    ENTER_TO_ACCOUNT_MAIN_PAGE = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')#кнопка "Войти в аккаунт" на главной странице
    LOGIN_EMAIL = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')#поле "Email" на странице авторизации
    LOGIN_PASSWORD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')#поле "Пароль" на странице авторизации
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')#кнопка "Войти" на странице авторизации
    LOGIN_SUCCESS_VERIFY_ELEMENT =(By.XPATH,'//*[@id="root"]/div/main/section[2]/div/button')#кнопка "Оформить заказ" используется как признак успешной авторизации
    ENTER_TO_ACCOUNT_LK = (By.XPATH, '//*[@id="root"]/div/header/nav/a')#кнопка "Личный кабинет"
    ENTER_TO_ACCOUNT_ZAREG = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a')#кнопка "Зарегистрироваться" на странице регистрации
    ENTER_TO_ACCOUNT_ZAREG_ENTER = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')#кнопка "Войти" на странице регистрации
    ENTER_TO_ACCOUNT_RESTORE_PASSWORD_PAGE =(By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a')#кнопка "Восстановить" на странице регистрации
    ENTER_TO_ACCOUNT_RESTORE_PASSWORD_PAGE_ENTER = (By.XPATH,'//*[@id="root"]/div/main/div/div/p/a')#кнопка "Войти" на странице восстановления пароля
    
    #Локаторы для проверки личного кабинета
    ENTER_TO_LK_BUTTON = (By.XPATH,'//*[@id="root"]/div/header/nav/a/p')#Кнопка "Личный кабинет" на главной странице
    LK_VERIFY = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[1]/a')#Заголовок "Профиль" используется для верификации личного кабинета
    LK_TO_CONSTRUCTOR = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p')#Заголовок "Конструктор" в ЛК
    CONSTRUCTOR_VERIFY = (By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')#Заголовок "Собери бургер" используется для верификации конструктора
    LK_TO_LOGO = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a')#Логотип "Конструктор" в ЛК
    EXIT_FROM_LK = (By.XPATH,'//*[@id="root"]/div/main/div/nav/ul/li[3]/button')#Кнопка "Выйти" в ЛК
    EXIT_FROM_LK_VERIFY = (By.XPATH, '//*[@id="root"]/div/main/div/h2')#Заголовок "Вход" используется для верификации выхода из ЛК

    #Локаторы для проверки коструктора
    MOVE_TO_BULKI = (By.XPATH, '//span[text()="Булки"]')#Заголовок "Булки"
    MOVE_TO_SOUSY = (By.XPATH, '//span[text()="Соусы"]') #Заголовок "Соусы"
    MOVE_TO_NACHINKI = (By.XPATH, '//span[text()="Начинки"]')#Заголовок "Начинки"
    MOVE_TO_BULKI_VERIFY = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1][@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')#Заголовок "Булки" используется для верификации переключения между вкладками в конструкторе
    MOVE_TO_SOUSY_VERIFY = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2][@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')#Заголовок "Соусы" используется для верификации переключения между вкладками в конструкторе
    MOVE_TO_NACHINKI_VERIFY = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3][@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')#Заголовок "Начинки" используется для верификации переключения между вкладками в конструкторе
   