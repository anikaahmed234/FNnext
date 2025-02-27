import time 
from locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def doLogout(driver):
    
    dropdown = WebDriverWait(driver, 20).until(
     EC.visibility_of_element_located(LogoutLocator.LOGOUT_ICON)
    )
    dropdown.click()
        
    logout_option = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located(LogoutLocator.DROPDOWN[1])
    )
    logout_option.click()

    return driver
