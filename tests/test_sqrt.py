import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.utils import *


class TestSqrt:
    @allure.title("Checking sqrt operation")
    def test_sqrt_operation(self, appium_driver):
        wait = WebDriverWait(appium_driver, 10)

        sqrt_operation = wait.until(EC.element_to_be_clickable(Locators.sqrt_operation))
        sqrt_operation.click()

        number, operation_result, locator_list = get_square_root_result()
        print(f'Checking the sqrt of {number}')

        for element in locator_list:
            current_element = wait.until(EC.element_to_be_clickable(element))
            current_element.click()

        equal_button = wait.until(EC.element_to_be_clickable(Locators.equal_button))
        equal_button.click()

        final_result = wait.until(EC.presence_of_element_located(Locators.result_final))
        final_result_text = final_result.text

        # Assert with a delta to handle precision differences
        final_result_float = float(final_result_text)

        delta = 0.0001  # Adjust delta as per your tolerance level
        print(f'op_result = {operation_result}, final_result_float = {final_result_float}, delta = {delta}')
        assert abs(final_result_float - operation_result) < delta
        

    @allure.title("Checking negative sqrt operation")
    def test_negative_sqrt_operation(self, appium_driver):
        wait = WebDriverWait(appium_driver, 10)

        minus_symbol = wait.until(EC.element_to_be_clickable(Locators.subtract_operation))
        sqrt_operation = wait.until(EC.element_to_be_clickable(Locators.sqrt_operation))
        sqrt_operation.click()
        minus_symbol.click()

        number, _, locator_list = get_square_root_result()
        print(f'Checking the sqrt of {number}')

        for element in locator_list:
            current_element = wait.until(EC.element_to_be_clickable(element))
            current_element.click()

        equal_button = wait.until(EC.element_to_be_clickable(Locators.equal_button))
        equal_button.click()

        final_result = wait.until(EC.presence_of_element_located(Locators.result_preview))
        final_result_text = final_result.text

        assert final_result_text == "Keep it real"
