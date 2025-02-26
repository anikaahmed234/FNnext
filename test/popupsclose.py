
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *


def close_popUp(driver):

    wait = WebDriverWait(driver, 20)

    close = wait.until(EC.visibility_of_element_located(popUps.tradingUpdates))
    if(close.is_displayed):
        close.click()

    closer = wait.until(EC.visibility_of_element_located(popUps.referPopUp))
    if(closer.is_displayed):
        closer.click()
    
    return driver