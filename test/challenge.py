from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def take_challenge(driver):
    
    # Start Challenge
    start_challenge = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(DashboardPageLocators.START_CHALLENGE_BUTTON)
    )
    start_challenge.click()

    return driver
