import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.utils import *


class TestDivision:
    @allure.title("Checking division operation")
    def test_division_operation(self, appium_driver):
        wait = WebDriverWait(appium_driver, 10)

        first_number, second_number, operation_result, locator_list = get_two_random_ints_and_result('/')
        print(f'Checking the division of {first_number} and {second_number}')

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
        assert abs(final_result_float - operation_result) < delta


    @allure.title("Checking division operation with zero")
    def test_division_by_zero_operation(self, appium_driver):
        wait = WebDriverWait(appium_driver, 10)

        first_number: int = 5
        second_number: int = 0

        print(f'Checking the division of {first_number} and {second_number}')
        
        number_five = wait.until(EC.element_to_be_clickable(Locators.number_five))
        number_zero = wait.until(EC.element_to_be_clickable(Locators.number_zero))
        division_operation = wait.until(EC.element_to_be_clickable(Locators.divide_operation)) 

        number_five.click()
        division_operation.click()
        number_zero.click()

        equal_button = wait.until(EC.element_to_be_clickable(Locators.equal_button))
        equal_button.click()

        result_preview = wait.until(EC.presence_of_element_located(Locators.result_preview))
        result_preview_text = result_preview.text
        is_displayed = result_preview.get_attribute("displayed")
        print(f'Warning is displayed ? {is_displayed}')

        assert result_preview_text == "Can't divide by 0"
        assert is_displayed == "true"
