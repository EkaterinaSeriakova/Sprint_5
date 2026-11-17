import random
import string

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
from data import BASE_URL

# Номер вашей когорты — замените на свой, чтобы email был уникальным
COHORT_NUMBER = '19'

FIRST_NAMES = ['anna', 'maria', 'olga', 'petr', 'ivan', 'fedya']
LAST_NAMES = ['krylova', 'petrova', 'ivanova', 'smirnov', 'orlov']


def generate_email():
    """Генерирует логин (email) в формате: имя_фамилия_номер когорты_3 цифры@домен."""
    digits = ''.join(random.choices(string.digits, k=3))
    return f"{random.choice(FIRST_NAMES)}_{random.choice(LAST_NAMES)}_{COHORT_NUMBER}_{digits}@yandex.ru"


def generate_password(length=8):
    """Генерирует пароль из латиницы и цифр.
    Длина 6 и больше — валидный пароль, меньше 6 — невалидный."""
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choices(alphabet, k=length))


def register_user(driver):
    """Регистрирует нового пользователя через UI.
    Возвращает кортеж (email, password), чтобы тест мог потом войти под ним."""
    wait = WebDriverWait(driver, 10)
    driver.get(f'{BASE_URL}register')
    wait.until(EC.visibility_of_element_located(locators.REGISTRATION_TITLE))

    email = generate_email()
    password = generate_password()

    driver.find_element(*locators.NAME_INPUT).send_keys('Анна Крылова')
    driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*locators.REGISTER_BUTTON).click()

    # После успешной регистрации открывается форма входа
    wait.until(EC.visibility_of_element_located(locators.LOGIN_TITLE))
    return email, password


def login_user(driver, email, password):
    """Заполняет и отправляет форму входа на странице /login."""
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(locators.LOGIN_TITLE))
    driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*locators.LOGIN_FORM_SUBMIT_BUTTON).click()
    # Успешный вход проверяем по кнопке «Оформить заказ» — она видна только вошедшему
    wait.until(EC.visibility_of_element_located(locators.PLACE_ORDER_BUTTON))
