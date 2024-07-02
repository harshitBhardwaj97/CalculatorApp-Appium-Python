from math import factorial

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.utils import *


class TestPower:
    @allure.title("Checking factorial operation")
    def test_division_operation(self, appium_driver):
        wait = WebDriverWait(appium_driver, 10)

        number_mapping: Dict[int, str] = {
            0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine'
        }

        number: int = randint(5, 15)
        result: int = factorial(number)
        print(f'Calculating factorial of {number}')

        number_str = str(number)

        # Click each digit button based on the number
        for digit in number_str:
            locator = getattr(Locators, f'number_{number_mapping.get(int(digit))}')
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()

        factorial_button = wait.until(EC.element_to_be_clickable(Locators.factorial_operation))
        factorial_button.click()

        equal_button = wait.until(EC.element_to_be_clickable(Locators.equal_button))
        equal_button.click()

        final_result = wait.until(EC.presence_of_element_located(Locators.result_final))
        final_result_text = final_result.text

        assert final_result_text == str(result)

