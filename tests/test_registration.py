from selenium.webdriver.support import expected_conditions as EC

import locators
from data import BASE_URL
from helpers import generate_email, generate_password


class TestRegistration:

    def test_successful_registration(self, driver, wait):
        # Имя не пустое, email в формате логин@домен, пароль минимум 6 символов
        driver.get(f'{BASE_URL}register')

        driver.find_element(*locators.NAME_INPUT).send_keys('Анна Крылова')
        driver.find_element(*locators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(generate_password())
        driver.find_element(*locators.REGISTER_BUTTON).click()

        # Успех: открылась форма входа
        wait.until(EC.visibility_of_element_located(locators.LOGIN_TITLE))
        assert driver.current_url == f'{BASE_URL}login'

    def test_registration_with_invalid_password(self, driver, wait):
        # Пароль короче шести символов — должна появиться ошибка
        driver.get(f'{BASE_URL}register')

        driver.find_element(*locators.NAME_INPUT).send_keys('Анна Крылова')
        driver.find_element(*locators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(generate_password(length=3))
        driver.find_element(*locators.REGISTER_BUTTON).click()

        error = wait.until(EC.visibility_of_element_located(locators.INVALID_PASSWORD_ERROR))
        assert error.is_displayed()
