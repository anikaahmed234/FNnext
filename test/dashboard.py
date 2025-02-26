import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *

def landingPage():
        
    driver = perform__valid_login()
    
    #logo
    logo = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.FNlogo)
    )
    assert logo.is_displayed(), "logo is not visible on dashboard"

    #profile pic
    # profile_pic = WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located(DashboardPageLocators.user)
    # )
    # assert profile_pic.is_displayed(), "profile pic is not visible on dashboard"

    #sidebar
    sidebarLoc(driver)

    #accountsTab
    expected_tab_names = ["Active", "Inactive", "Breached"]

    tabs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "ant-tabs-tab-btn"))
    )

    actual_tab_names = [tab.text.strip() for tab in tabs]

    assert actual_tab_names == expected_tab_names, f"Expected tabs {expected_tab_names}, but found {actual_tab_names}"

    for expected in expected_tab_names:
        assert expected in actual_tab_names, f"Expected tab '{expected}' not found in actual tabs: {actual_tab_names}"

    #search box
    searchbox = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.search)
    )
    assert searchbox.is_displayed(), "search box is not visible"

    #filter

    #banners

    return driver