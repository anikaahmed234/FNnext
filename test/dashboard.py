from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from locators import *
from .login import *
from .sidebar import *
from .pop_ups_close import *
from .intercom import *

def landingPage(driver):
        
    # driver = perform__valid_login()
    # close_popUp(driver)

    #logo
    logo = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.FN_LOGO)
    )
    assert logo.is_displayed(), "logo is not visible on dashboard"

    intercomicon(driver)

    #popUp
    hover_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-notification-notice"))  
    )
    ActionChains(driver).move_to_element(hover_element).perform()

    pops = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "anticon-close-circle"))
    )

    for pop in pops:
        try:
            ActionChains(driver).move_to_element(pop).click().perform()
            
        except Exception as e:
            print(f"Could not close popup: {e}")

    #profile pic
    # profile_pic = WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located(DashboardPageLocators.USER)
    # )
    # assert profile_pic.is_displayed(), "profile pic is not visible on dashboard"
    
    #refer & earn
    refer = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.REFER_AND_EARN)
    )
    assert refer.is_displayed(), "refer & earn button is not visible on dashboard header"

    #sidebar
    # sidebar_menu(driver)

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
        EC.visibility_of_element_located(DashboardPageLocators.SEARCH)
    )
    assert searchbox.is_displayed(), "search box is not visible"

    #filter

    #banners

    return driver