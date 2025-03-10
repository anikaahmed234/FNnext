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
    try:
        refer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(DashboardPageLocators.REFER_AND_EARN)
        )
        assert refer.is_displayed(), "❌ not visible on the screen"
        print("✅ refer button is visible!!!")

        imp_notice = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(FreeTrialButton.IMPORTANT_NOTICE)
        )
        assert imp_notice.is_displayed(), "❌ not visible on the screen"
        print("✅ imp_notice button is visible!!!")

        login_header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(FreeTrialButton.LOGIN_ID_HEADER)
        )
        assert login_header.is_displayed(), "❌ not visible on the screen"
        print("✅ login header is visible!!!")

        hello_username = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(FreeTrialButton.HELLO_USERNAME)
        )
        assert hello_username.is_displayed(), "❌ not visible on the screen"
        print("✅ username is visible!!!")

        trading_cycle = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(FreeTrialButton.TRADING_CYCLE)
        )
        assert trading_cycle.is_displayed(), "❌ not visible on the screen"
        print("✅ trading cycle is visible!!!")

        start_date = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(FreeTrialButton.START_DATE)
        )
        assert start_date.is_displayed(), "❌ not visible on the screen"
        print("✅ start date is visible!!!")

        end_date = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(FreeTrialButton.END_DATE)
        )
        assert end_date.is_displayed(), "❌ not visible on the screen"
        print("✅ end date is visible!!!")

        stats_title = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(FreeTrialButton.STATS_TITLE)
        )
        assert stats_title.is_displayed(), "❌ not visible on the screen"
        print("✅ stats title is visible!!!")

        stats_cards = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(FreeTrialButton.STATS_CARDS)
        )
        assert stats_cards.is_displayed(), "❌ not visible on the screen"
        print("✅ stats card is visible!!!")

        email_support = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(FreeTrialButton.EMAIL_SUPPORT)
        )
        assert email_support.is_displayed(), "❌ not visible on the screen"
        print("✅ email support is visible!!!")

        contact = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(FreeTrialButton.CONTACT)
        )
        assert contact.is_displayed(), "❌ not visible on the screen"
        print("✅ contact is visible!!!")

        trading_obj_title = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(FreeTrialButton.TRADING_OBJ_TITLE)
        )
        assert trading_obj_title.is_displayed(), "❌ not visible on the screen"
        print("✅ trading obj title is visible!!!")

    except AssertionError as msg:
        print(msg)
        
    print("Exiting Free Trial Dashboard Account!!!")

    return driver
