from selenium.webdriver.support import expected_conditions as EC

import locators
from data import BASE_URL


class TestPersonalAccount:

    def test_transition_to_personal_account(self, driver, wait, logged_in_user):
        # Переход в личный кабинет по клику на «Личный Кабинет»
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.url_to_be(f'{BASE_URL}account/profile'))
        assert wait.until(EC.visibility_of_element_located(locators.PROFILE_LINK)).is_displayed()

    def test_transition_to_constructor_via_button(self, driver, wait, logged_in_user):
        # Переход из личного кабинета в конструктор по кнопке «Конструктор»
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*locators.CONSTRUCTOR_BUTTON).click()
        wait.until(EC.visibility_of_element_located(locators.ASSEMBLE_BURGER_TITLE))
        assert driver.current_url == BASE_URL

    def test_transition_to_constructor_via_logo(self, driver, wait, logged_in_user):
        # Переход из личного кабинета в конструктор по логотипу Stellar Burgers
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*locators.LOGO).click()
        wait.until(EC.visibility_of_element_located(locators.ASSEMBLE_BURGER_TITLE))
        assert driver.current_url == BASE_URL

    def test_logout(self, driver, wait, logged_in_user):
        # Выход из аккаунта по кнопке «Выход» в личном кабинете
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(locators.PROFILE_LINK))
        driver.find_element(*locators.LOGOUT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(locators.LOGIN_TITLE))
        assert driver.current_url == f'{BASE_URL}login'
