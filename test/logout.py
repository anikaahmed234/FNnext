from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def doLogout(driver):
    
    # driver.get("https://uat-dashboard.fundednext.com/competition")
    print("🚀 Logging Out...")

    dropdown = WebDriverWait(driver, 20).until(
     EC.visibility_of_element_located(LogoutLocator.HAMBURGER)
    )
    dropdown.click()
        
    logout_option = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(LogoutLocator.LOGOUT)
    )
    logout_option.click()
    
    print("Logged Out!!!")

    return driver
