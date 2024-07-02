import os

import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions


@pytest.fixture()
def apk_path():
    # Get the current working directory (where conftest.py is located)
    current_dir = os.path.dirname(__file__)
    # Move one directory up (assuming tests and app are siblings)
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    # Combine the path with the app folder and APK name
    apk_path = os.path.join(parent_dir, "app", "Calculator.apk")
    return apk_path


@pytest.fixture()
def appium_driver(apk_path):
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:automationName": "uiautomator2",
        # "appium:appPackage": "com.google.android.calculator",
        # "appium:appActivity": "com.android.calculator2.Calculator",
        "appium:app": apk_path,
        "appium:deviceName": "Android",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    # Setup code before yield

    yield driver

    # Teardown code after yield
    driver.quit()
