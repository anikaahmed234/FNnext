import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators import *
from config import get_driver, USERNAME, PASSWORD, URL, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def checkout(driver):

    checkout = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(CheckoutPageLocators.CHECKOUT_TITLE)
    )
    assert checkout.is_displayed(), "Checkout is not visible after redirect"

    image_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(CheckoutPageLocators.EVALUATION_BUTTON)
    )
    image_element.click()

    get_plan = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(CheckoutPageLocators.PLAN_BUTTON)
    )
    get_plan.click()
    time.sleep(5)

    checkbox_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(CheckoutPageLocators.CHECKBOX)
    )
    if not checkbox_element.is_selected():
        checkbox_element.click()

    button_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(CheckoutPageLocators.GET_STARTED_BUTTON)
    )
    button_element.click()

    return driver