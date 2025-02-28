from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *

def checkout(driver):
    print("Checkout Page...")

    checkout = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(CheckoutPageLocators.CHECKOUT_TITLE)
    )
    assert checkout.is_displayed(), "Checkout is not visible after redirect"

    get_plan = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(CheckoutPageLocators.PLAN_BUTTON)
    )
    get_plan.click()

    checkbox_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(CheckoutPageLocators.CHECKBOX)
    )
    if not checkbox_element.is_selected():
        checkbox_element.click()

    button_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(CheckoutPageLocators.GET_STARTED_BUTTON)
    )
    button_element.click()
    
    print("Exiting checkout page!!!")
    return driver