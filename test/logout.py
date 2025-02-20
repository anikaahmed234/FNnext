import time 
from locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def doLogout(driver):
    
    dropdown = WebDriverWait(driver, 20).until(
     EC.visibility_of_element_located(Logoutdrop.logout_icon)
    )
    dropdown.click()
        
    logout_option = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located(Logoutdrop.dropdown[1])
    )
    logout_option.click()

    return driver
