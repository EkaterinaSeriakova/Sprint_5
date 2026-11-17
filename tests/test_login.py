from selenium.webdriver.support import expected_conditions as EC

import locators
from data import BASE_URL
from helpers import login_user


class TestLogin:

    def test_login_via_main_page_button(self, driver, wait, registered_user):
        # Вход по кнопке «Войти в аккаунт» на главной
        email, password = registered_user
        driver.find_element(*locators.LOGIN_BUTTON_ON_MAIN).click()
        login_user(driver, email, password)
        assert wait.until(EC.visibility_of_element_located(locators.PLACE_ORDER_BUTTON)).is_displayed()

    def test_login_via_personal_account_button(self, driver, wait, registered_user):
        # Вход через кнопку «Личный Кабинет» в шапке
        email, password = registered_user
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        login_user(driver, email, password)
        assert wait.until(EC.visibility_of_element_located(locators.PLACE_ORDER_BUTTON)).is_displayed()

    def test_login_via_registration_form_link(self, driver, wait, registered_user):
        # Вход по кнопке «Войти» в форме регистрации
        email, password = registered_user
        driver.get(f'{BASE_URL}register')
        driver.find_element(*locators.LOGIN_LINK_ON_FORMS).click()
        login_user(driver, email, password)
        assert wait.until(EC.visibility_of_element_located(locators.PLACE_ORDER_BUTTON)).is_displayed()

    def test_login_via_forgot_password_form_link(self, driver, wait, registered_user):
        # Вход по кнопке «Войти» в форме восстановления пароля
        email, password = registered_user
        driver.get(f'{BASE_URL}forgot-password')
        driver.find_element(*locators.LOGIN_LINK_ON_FORMS).click()
        login_user(driver, email, password)
        assert wait.until(EC.visibility_of_element_located(locators.PLACE_ORDER_BUTTON)).is_displayed()
