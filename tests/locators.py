from appium.webdriver.common.appiumby import AppiumBy
from typing import Tuple


class Locators:
    # numbers / digits
    number_zero: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/digit_0")
    number_one: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/digit_1")
    number_two: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/digit_2")
    number_three: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/digit_3")
    number_four: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/digit_4")
    number_five: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/digit_5")
    number_six: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/digit_6")
    number_seven: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/digit_7")
    number_eight: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/digit_8")
    number_nine: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/digit_9")

    # operations
    add_operation: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/op_add")
    subtract_operation: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/op_sub")
    multiply_operation: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/op_mul")
    divide_operation: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/op_div")
    factorial_operation: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/op_fact")
    power_operation: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/op_pow")
    sqrt_operation: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/op_sqrt")

    # other buttons
    equal_button: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/eq")
    clear_button: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/clr")
    decimal_button: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/dec_point")

    # result
    result_preview: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/result_preview")
    result_final: Tuple[str, str] = (AppiumBy.ID, "com.google.android.calculator:id/result_final")
