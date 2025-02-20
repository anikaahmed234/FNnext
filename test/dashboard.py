from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *
from .challenge import *
from .checkout import *
from .paymentMethod import *

def landingPage():
        
    driver = perform__valid_login()
    
    #logo

    #profile pic

    #sidebar

    #accountsTab

    #search box

    #filter

    #banners

    return driver