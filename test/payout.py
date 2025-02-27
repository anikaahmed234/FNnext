import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *
from .sidebar import *
from .popupsclose import *
from .intercom import *

def payoutmenu():
        
    driver = perform__valid_login()
    close_popUp(driver)

    #Payout
    Payout = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBar.Payout)
    )
    Payout.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/payout'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"
    
    expected_col_names = ["Login", "Date", "Withdrawal ID", "Requested Amount", "Status", "Disbursed Amount", "Timer", "Payout Proof","Tx Id","Note"]

    cols = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((payoutelement.colHead))
    )

    actual_tab_names = [col.text.strip() for col in cols]

    assert actual_tab_names == expected_col_names, f"Expected tabs {expected_col_names}, but found {actual_tab_names}"

    for expected in expected_col_names:
        assert expected in actual_tab_names, f"Expected tab '{expected}' not found in actual tabs: {actual_tab_names}"

    return driver