
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *

def intercom(driver):

     #intercom
    intercomicon = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.intercom)
    )
    assert intercomicon.is_displayed(), "intercom icon is not visible"