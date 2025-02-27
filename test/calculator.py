import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *
from .pop_ups_close import *
from .intercom import *
from .sidebar import *

def calc(driver):
        
    # driver = perform__valid_login()
    # close_popUp(driver)

    #Calculator
    Calculator = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBarLocator.CALCULATOR)
    )
    Calculator.click(), "SideBar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/widgets'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    #calc_tabs
    tabs = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located(CalculatorLocators.TABS)
    )

    expected_tab_names = ["Margin Calculator", "Profit/Loss Calculator", "Risk Calculator","News Calendar", "Top Stories","Forex Cross Rates","Technical Analysis", "Fundamental Data"]

    actual_tab_names = [tab.text.strip() for tab in tabs]

    assert actual_tab_names == expected_tab_names, f"Expected tabs {expected_tab_names}, but found {actual_tab_names}"

    for expected in expected_tab_names:
        assert expected in actual_tab_names, f"Expected tab '{expected}' not found in actual tabs: {actual_tab_names}"

    intercomicon(driver)

    return driver