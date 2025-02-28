import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from locators import *
from .login import *
from .challenge import *
from .dashboard import *
from .checkout import *
from .payment_Method import *

def free_trial(driver):
    print("🚀 Free Trial Launching...")

    # Free Trial
    freeTrial = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(FreeTrialButton.FREE_TRIAL)
    )
    freeTrial.click()

    try:
        have_ft = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(FreeTrialButton.HAVE_FT)
        )
        if have_ft.is_displayed():
            print("Have Free Trial' is displayed. Exiting function.")
            return driver
    except:
        print("Have Free Trial' not displayed. Continuing with Free Trial process...")

        checkbox_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(FreeTrialButton.CHECKBOX)
        )
        if not checkbox_element.is_selected():
            checkbox_element.click()
        
        get_start = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(FreeTrialButton.GET_STARTED_BUTTON)
        )
        get_start.click()

        thank_you = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(FreeTrialButton.THANK_YOU_MSG)
        )
        assert thank_you.is_displayed(), "Free Trial Failed"
        
        start_challenge_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(FreeTrialButton.START_CHALLENGE_BUTTON)
        )
        start_challenge_button.click()
        
        # Verify Dashboard
        dashboard = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(DashboardPageLocators.DASHBOARD_TITLE)
        )
        assert dashboard.is_displayed(), "Dashboard is not visible after login"
        
        print("Exiting Free Trial!!!")

    return driver
