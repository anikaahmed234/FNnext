
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *
from .challenge import *
from .checkout import *
from .paymentMethod import *

def free_trial():
   
    driver = perform__valid_login()

    # Free Trial
    freeTrial = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(FreeTrialButton.Free_Trial)
    )
    freeTrial.click()

    checkbox_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(freeTrialLoc.CHECKBOX)
    )
    if not checkbox_element.is_selected():
        checkbox_element.click()

    freeTrialLoc.GET_STARTED_BUTTON.click()

    time.sleep(5)

    thank_you = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(FreeTrialButton.Thank_you_msg)
    )
    assert thank_you.is_displayed(), "Free Trial Failed"
    freeTrialLoc.START_CHALLENGE_BUTTON.click()
    
    # Verify Dashboard
    dashboard = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.DASHBOARD_TITLE)
    )
    assert dashboard.is_displayed(), "Dashboard is not visible after login"

    return driver
