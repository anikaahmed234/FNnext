from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *
from .sidebar import *
from .pop_ups_close import *
from .intercom import *
from .announcement import *

def landingPage(driver):
    print("🚀 Landing page...")

    announcement_close(driver)

    #logo
    logo = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.FN_LOGO)
    )
    assert logo.is_displayed(), "logo is not visible on dashboard"

    #profile pic
    profile_pic = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.USER)
    )
    assert profile_pic.is_displayed(), "profile pic is not visible on dashboard"
    
    #refer & earn
    refer = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.REFER_AND_EARN)
    )
    assert refer.is_displayed(), "refer & earn button is not visible on dashboard header"

    #sidebar
    # sidebar_menu(driver)

    intercomicon(driver)

    #title & subtitle
    expected_account_title = "Accounts"
    account_title = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.ACCOUNT)
    )
    assert account_title.is_displayed(), "account title is not visible on dashboard"
    actual_acc_title = account_title.text.strip()

    assert actual_acc_title == expected_account_title, f"Expected tabs {expected_account_title}, but found {actual_acc_title}"

    for expected in expected_account_title:
        assert expected in actual_acc_title, f"Expected tab '{expected}' not found in actual tabs: {actual_acc_title}"

    expected_account_subtitle = "Unlock your trading potential with FundedNext. Start trading now!"
    account_subtitle = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.ACCOUNT_SUBTITLE)
    )
    assert account_subtitle.is_displayed(), "account subtitle is not visible on dashboard"
    actual_acc_subtitle = account_subtitle.text.strip()

    assert actual_acc_subtitle == expected_account_subtitle, f"Expected tabs {expected_account_subtitle}, but found {actual_acc_subtitle}"

    for expected in expected_account_subtitle:
        assert expected in actual_acc_subtitle, f"Expected tab '{expected}' not found in actual tabs: {actual_acc_subtitle}"

    time.sleep(5)

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

    print("Exiting Landing Page!!!")

    return driver