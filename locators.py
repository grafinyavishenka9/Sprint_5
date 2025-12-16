from selenium.webdriver.common.by import By


class Locators:

    #Локаторы для регистрации
    REGISTRATION_NAME = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')#поле "Имя" на странице регистрации
    REGISTRATION_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')#поле "Email" на странице регистрации
    REGISTRATION_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')#поле "Пароль" на странице регистрации
    REGISTRATION_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')#кнопка "Зарегистрироваться" на странице регистрации
    REGISTRATION_WRONG_PASSWORD_ERROR = (By.XPATH, '//p[text()="Некорректный пароль"]')#тект ошибки при вводе некорректного пароля на странице регистрации
    
    #Локаторы для логина
    ENTER_TO_ACCOUNT_MAIN_PAGE = (By.XPATH, '//button[text()="Войти в аккаунт"]')#кнопка "Войти в аккаунт" на главной странице
    LOGIN_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')#поле "Email" на странице авторизации
    LOGIN_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')#поле "Пароль" на странице авторизации
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')#кнопка "Войти" на странице авторизации
    LOGIN_SUCCESS_VERIFY_ELEMENT =(By.XPATH,'//button[text()="Оформить заказ"]')#кнопка "Оформить заказ" используется как признак успешной авторизации
    ENTER_TO_ACCOUNT_LK = (By.XPATH, '//p[text()="Личный Кабинет"]')#кнопка "Личный кабинет"
    ENTER_TO_ACCOUNT_ZAREG = (By.XPATH, '//a[text()="Зарегистрироваться"]')#кнопка "Зарегистрироваться" на странице регистрации
    ENTER_TO_ACCOUNT_ZAREG_ENTER = (By.XPATH, '//a[text()="Войти"]')#кнопка "Войти" на странице регистрации
    ENTER_TO_ACCOUNT_RESTORE_PASSWORD_PAGE =(By.XPATH, '//a[text()="Восстановить пароль"]')#кнопка "Восстановить пароль" на странице регистрации
    ENTER_TO_ACCOUNT_RESTORE_PASSWORD_PAGE_ENTER = (By.XPATH,'//a[text()="Войти"]')#кнопка "Войти" на странице восстановления пароля
    
    #Локаторы для проверки личного кабинета
    ENTER_TO_LK_BUTTON = (By.XPATH,'//p[text()="Личный Кабинет"]')#Кнопка "Личный кабинет" на главной странице
    LK_VERIFY = (By.XPATH, '//a[text()="Профиль"]')#Заголовок "Профиль" используется для верификации личного кабинета
    LK_TO_CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')#Заголовок "Конструктор" в ЛК
    CONSTRUCTOR_VERIFY = (By.XPATH, '//h1[text()="Соберите бургер"]')#Заголовок "Соберите бургер" используется для верификации конструктора
    LK_TO_LOGO = (By.XPATH, '//a[@href="/"]')#Логотип "Конструктор" в ЛК
    EXIT_FROM_LK = (By.XPATH,'//button[text()="Выход"]')#Кнопка "Выход" в ЛК
    EXIT_FROM_LK_VERIFY = (By.XPATH, '//h2[text()="Вход"]')#Заголовок "Вход" используется для верификации выхода из ЛК

    #Локаторы для проверки коструктора
    MOVE_TO_BULKI = (By.XPATH, '//span[text()="Булки"]')#Заголовок "Булки"
    MOVE_TO_SOUSY = (By.XPATH, '//span[text()="Соусы"]') #Заголовок "Соусы"
    MOVE_TO_NACHINKI = (By.XPATH, '//span[text()="Начинки"]')#Заголовок "Начинки"
    MOVE_TO_BULKI_VERIFY = (By.XPATH, '//span[text()="Булки"]/parent::div[contains(@class,"tab_tab_type_current__2BEPc")]')#Заголовок "Булки" используется для верификации переключения между вкладками в конструкторе
    MOVE_TO_SOUSY_VERIFY = (By.XPATH, '//span[text()="Соусы"]/parent::div[contains(@class,"tab_tab_type_current__2BEPc")]')#Заголовок "Соусы" используется для верификации переключения между вкладками в конструкторе
    MOVE_TO_NACHINKI_VERIFY = (By.XPATH, '//span[text()="Начинки"]/parent::div[contains(@class,"tab_tab_type_current__2BEPc")]')#Заголовок "Начинки" используется для верификации переключения между вкладками в конструкторе
   