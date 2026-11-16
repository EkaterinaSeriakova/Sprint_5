from selenium.webdriver.common.by import By

# ---------- Главная страница ----------

# Кнопка «Войти в аккаунт» на главной странице
LOGIN_BUTTON_ON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
# Кнопка «Личный Кабинет» в шапке сайта
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
# Логотип Stellar Burgers в шапке
LOGO = (By.XPATH, ".//a[contains(@class, 'AppHeader_header__logo__')]")

# ---------- Конструктор ----------

# Заголовок «Соберите бургер»
ASSEMBLE_BURGER_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")
# Вкладка «Булки»
BUNS_TAB = (By.XPATH, ".//span[text()='Булки']")
# Вкладка «Соусы»
SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']")
# Вкладка «Начинки»
FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']")

# ---------- Формы (вход, регистрация, восстановление пароля) ----------

# Заголовок «Вход» на странице логина
LOGIN_TITLE = (By.XPATH, ".//h2[text()='Вход']")
# Заголовок «Регистрация»
REGISTRATION_TITLE = (By.XPATH, ".//h2[text()='Регистрация']")
# Заголовок «Восстановление пароля»
FORGOT_PASSWORD_TITLE = (By.XPATH, ".//h2[text()='Восстановление пароля']")
# Поле «Имя» в форме регистрации
NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
# Поле «Email»
EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
# Поле «Пароль»
PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")
# Кнопка «Зарегистрироваться» в форме регистрации
REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
# Кнопка «Войти» в форме логина
LOGIN_FORM_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']")
# Ссылка «Войти» под формами регистрации и восстановления пароля
LOGIN_LINK_ON_FORMS = (By.XPATH, ".//a[text()='Войти']")
# Ссылка «Восстановить пароль» в форме логина
FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")
# Ошибка «Некорректный пароль»
INVALID_PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")

# ---------- Личный кабинет ----------

# Ссылка «Профиль» в меню личного кабинета
PROFILE_LINK = (By.XPATH, ".//a[text()='Профиль']")
# Кнопка «Выход»
LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
# Кнопка «Оформить заказ» (видна только вошедшему пользователю — по ней проверяем, что вход удался)
PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

# Кнопка «Конструктор» в шапке
CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")

# Активная вкладка «Булки» (класс tab_tab_type_current есть только у выбранной вкладки)
ACTIVE_BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Булки']]")
# Активная вкладка «Соусы»
ACTIVE_SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Соусы']]")
# Активная вкладка «Начинки»
ACTIVE_FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Начинки']]")
