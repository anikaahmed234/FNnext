import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *
from .sidebar import *
from .pop_ups_close import *
from .intercom import *

def tools_menu(driver):
        
    # driver = perform__valid_login()
    # close_popUp(driver)

    #Tools
    Tools = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBarLocator.TOOLS)
    )
    Tools.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/utilities'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    #Tabs
    expected_tab_names = ["All", "Tools", "Partnership", "E-Books","Videos"]

    tabs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((ToolsLocator.COL_HEAD))
    )

    actual_tab_names = [tab.text.strip() for tab in tabs]

    assert actual_tab_names == expected_tab_names, f"Expected tabs {expected_tab_names}, but found {actual_tab_names}"

    for expected in expected_tab_names:
        assert expected in actual_tab_names, f"Expected tab '{expected}' not found in actual tabs: {actual_tab_names}"

    intercomicon(driver)

    return driver