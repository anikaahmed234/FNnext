import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators import *
from login import perform__valid_login
from challenge import take_challenge
from checkout import checkout
from paymentMethod import paymentMethod

from utilities.config import get_driver, USERNAME, PASSWORD, URL, time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = perform__valid_login()

# Verify Dashboard
dashboard = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located(DashboardPageLocators.DASHBOARD_TITLE)
)
assert dashboard.is_displayed(), "Dashboard is not visible after login"

# start challenge
take_challenge(driver)

# Checkout
checkout(driver)

# Select Payment Method
paymentMethod(driver)

print("Ta da!!! Completed!")
driver.quit()