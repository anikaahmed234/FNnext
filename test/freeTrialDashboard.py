import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from locators import *
from .login import *
from .intercom import *

def free_trial_dashboard(driver):

    dashboard_buttons = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located(FreeTrialButton.DASHBOARD_FT)
    )
    if dashboard_buttons:
        dashboard_buttons[0].click()
        print("Clicked on Free Trial Dashboard button")
    else:
        print("Free Trial Dashboard button not found")

    time.sleep(5)
    expected_url = f'{URL}/accounts/account-overview'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"
    
    intercomicon(driver)

    #refer & earn
    refer = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.REFER_AND_EARN)
    )
    assert refer.is_displayed(), "not visible on the screen"

    imp_notice = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(FreeTrialButton.IMPORTANT_NOTICE)
    )
    assert imp_notice.is_displayed(), "not visible on the screen"

    login_header = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(FreeTrialButton.LOGIN_ID_HEADER)
    )
    assert login_header.is_displayed(), "not visible on the screen"

    hello_username = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(FreeTrialButton.HELLO_USERNAME)
    )
    assert hello_username.is_displayed(), "not visible on the screen"

    trading_cycle = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(FreeTrialButton.TRADING_CYCLE)
    )
    assert trading_cycle.is_displayed(), "not visible on the screen"

    start_date = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(FreeTrialButton.START_DATE)
    )
    assert start_date.is_displayed(), "not visible on the screen"

    end_date = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(FreeTrialButton.END_DATE)
    )
    assert end_date.is_displayed(), "not visible on the screen"

    stats_title = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(FreeTrialButton.STATS_TITLE)
    )
    assert stats_title.is_displayed(), "not visible on the screen"

    stats_cards = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(FreeTrialButton.STATS_CARDS)
    )
    assert stats_cards.is_displayed(), "not visible on the screen"

    email_support = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(FreeTrialButton.EMAIL_SUPPORT)
    )
    assert email_support.is_displayed(), "not visible on the screen"

    contact = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(FreeTrialButton.CONTACT)
    )
    assert contact.is_displayed(), "not visible on the screen"

    trading_obj_title = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(FreeTrialButton.TRADING_OBJ_TITLE)
    )
    assert trading_obj_title.is_displayed(), "not visible on the screen"

    print("Exiting Free Trial Dashboard Account!!!")

    return driver
