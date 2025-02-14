import sys
import os

from utilities.config import get_driver, USERNAME, PASSWORD, URL, time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators import *
from challenge import take_challenge
from checkout import checkout
from paymentMethod import paymentMethod

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def dashboard(driver):

    # Verify Dashboard
    dashboard = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.DASHBOARD_TITLE)
    )
    assert dashboard.is_displayed(), "Dashboard is not visible after login"

    # start challenge
    driver = take_challenge(driver)

    # Checkout
    driver = checkout(driver)

    # Select Payment Method
    driver = paymentMethod(driver)

    print("Ta daaa!!! Completed!")
    driver.quit()
