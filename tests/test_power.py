import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.utils import *


class TestPower:
    @allure.title("Checking power operation")
    def test_division_operation(self, appium_driver):
        wait = WebDriverWait(appium_driver, 10)

        first_number, second_number, operation_result, locator_list = get_power_result()
        print(f'Checking the power of {first_number} to {second_number}')

        for element in locator_list:
            current_element = wait.until(EC.element_to_be_clickable(element))
            current_element.click()

        equal_button = wait.until(EC.element_to_be_clickable(Locators.equal_button))
        equal_button.click()

        final_result = wait.until(EC.presence_of_element_located(Locators.result_final))
        final_result_text = final_result.text

        assert final_result_text == str(operation_result)

