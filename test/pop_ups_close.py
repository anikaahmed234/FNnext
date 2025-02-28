import time 
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from locators import *
from .login import *


def close_popUp(driver):
    print("🚀 Closing popUps...")

    wait = WebDriverWait(driver, 20)
    
    close = wait.until(EC.visibility_of_element_located(PopUpsLocator.TRADING_UPDATES_POP_UP))
    if(close.is_displayed):
        close.click()
    
    
    closer = wait.until(EC.visibility_of_element_located(PopUpsLocator.REFER_POP_UP))
    if(closer.is_displayed):
        closer.click()
    print("PopUps are closed!!!")

    return driver