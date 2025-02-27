
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from locators import *
from .login import *
from .challenge import *
from .checkout import *
from .payment_Method import *

def free_trial():
   
    driver = perform__valid_login()
    actions = ActionChains(driver)

    close_txt = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(FreeTrialButton.CLOSE_TEXT)
    )

    # actions.move_to_element(close_icon).perform()
    assert close_txt.is_displayed() , "no"

    close_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(FreeTrialButton.CLOSE_ICON)
    )

    # actions.move_to_element(close_icon).perform()
    assert close_icon.is_displayed() , "no"
    close_icon.click()
    
    # Free Trial
    freeTrial = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(FreeTrialButton.FREE_TRIAL)
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
        EC.visibility_of_element_located(FreeTrialButton.THANK_YOU_MSG)
    )
    assert thank_you.is_displayed(), "Free Trial Failed"
    freeTrialLoc.START_CHALLENGE_BUTTON.click()
    
    # Verify Dashboard
    dashboard = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.DASHBOARD_TITLE)
    )
    assert dashboard.is_displayed(), "Dashboard is not visible after login"

    return driver
