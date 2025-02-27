import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *
from .sidebar import *
from .pop_ups_close import *
from .intercom import *

def payout_menu(driver):
    
#     driver = perform__valid_login()
#     close_popUp(driver)

    #Payout
    Payout = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBarLocator.PAYOUT) 
    )
    Payout.click(), "sidebar is not visible after login"
    
    driver.set_page_load_timeout(30)
    time.sleep(3)

    expected_url = f'{URL}/payout'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"
        
    expected_col_names = ["Login", "Date", "Withdrawal ID", "Requested Amount", "Status", "Disbursed Amount", "Timer", "Payout Proof","Tx Id","Note"]

    cols = WebDriverWait(driver, 20).until(
         EC.presence_of_all_elements_located((PayoutLocator.COL_HEAD))
    )

    actual_tab_names = [col.text.strip() for col in cols]

    assert actual_tab_names == expected_col_names, f"Expected tabs {expected_col_names}, but found {actual_tab_names}"

    for expected in expected_col_names:
         assert expected in actual_tab_names, f"Expected tab '{expected}' not found in actual tabs: {actual_tab_names}"

    expected_method_names = ["Rise", "USDT", "USDC", "Wind"]

    methodnames = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((PayoutLocator.METHOD))
    )

    actual_method_names = [method.text.strip() for method in methodnames]

    assert actual_method_names == expected_method_names, f"Expected tabs {expected_method_names}, but found {actual_method_names}"

    for expected in expected_method_names:
           assert expected in actual_method_names, f"Expected tab '{expected}' not found in actual tabs: {actual_method_names}"
    
    return driver