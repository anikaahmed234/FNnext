from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from locators import *
from .login import *
from .challenge import *
from .checkout import *
from .paymentMethod import *

def test_dashbaord():
        
    driver = perform__valid_login()

    # Verify Dashboard
    dashboard = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.DASHBOARD_TITLE)
    )
    assert dashboard.is_displayed(), "Dashboard is not visible after login"
 
    while True:
        try:
            close_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(DashboardPageLocators.close_button)
            )
            close_button.click()
            time.sleep(2) 
        except TimeoutException:
            print("Close button not found.")
            break
    
    # start challenge
    take_challenge(driver)

    # Checkout
    checkout(driver)

    # Select Payment Method
    paymentMethod(driver)

    print("Ta da!!!! Completed!!")

    return driver
