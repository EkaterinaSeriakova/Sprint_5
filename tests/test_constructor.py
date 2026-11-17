import pytest
from selenium.webdriver.support import expected_conditions as EC

import locators
from data import BASE_URL


class TestConstructorSections:

    @pytest.mark.parametrize(
        'tab, active_tab',
        [
            (locators.BUNS_TAB, locators.ACTIVE_BUNS_TAB),
            (locators.SAUCES_TAB, locators.ACTIVE_SAUCES_TAB),
            (locators.FILLINGS_TAB, locators.ACTIVE_FILLINGS_TAB),
        ],
        ids=['булки', 'соусы', 'начинки'],
    )
    def test_switch_to_section(self, driver, wait, tab, active_tab):
        # Переход к разделу конструктора: вкладка становится активной
        driver.find_element(*tab).click()
        assert wait.until(EC.visibility_of_element_located(active_tab)).is_displayed()
