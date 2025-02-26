import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *
from .popupsclose import *
from .intercom import *

def comp():
        
    driver = perform__valid_login()
    close_popUp(driver)

    return driver