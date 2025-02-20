from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *
from .challenge import *
from .checkout import *
from .paymentMethod import *

def cardPurchase(driver):
        
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
    paymentCard(driver)

    return driver
