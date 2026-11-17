import pytest
from selenium import webdriver

from data import BASE_URL
from helpers import register_user, login_user


@pytest.fixture
def driver():
    """Открывает Chrome перед тестом и закрывает после теста (driver.quit()).
    Так каждый тест автономен: браузер запускается и умирает вместе с тестом."""
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(BASE_URL)
    yield driver          # всё до yield выполняется ПЕРЕД тестом
    driver.quit()         # всё после yield — ПОСЛЕ теста (требование задания)


@pytest.fixture
def registered_user(driver):
    """Регистрирует уникального пользователя и отдаёт тесту (email, password)."""
    return register_user(driver)


@pytest.fixture
def logged_in_user(driver):
    """Регистрирует пользователя и сразу выполняет вход. Отдаёт (email, password)."""
    email, password = register_user(driver)
    login_user(driver, email, password)
    return email, password

from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def wait(driver):
    """Явные ожидания до 10 секунд для проверок в тестах."""
    return WebDriverWait(driver, 10)
