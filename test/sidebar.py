import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.config import DASHBOARD


from locators import *
from .login import *

def sidebarLoc():

    driver = perform__valid_login()

    #logo

    #sidebars

    #account
    accounts = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBar.accounts)
    )
    accounts.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/accounts'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    #Transactions
    Transactions = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBar.Transactions)
    )
    Transactions.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/billing/billing-history'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    #Payout
    Payout = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBar.Payout)
    )
    Payout.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/payout'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    #Competition
    Competition = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBar.Competition)
    )
    Competition.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/competition'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    #My_Offers
    My_Offers = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBar.My_Offers)
    )
    My_Offers.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/user-offer'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    driver.get(DASHBOARD)

    #Tools
    Tools = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBar.Tools)
    )
    Tools.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/utilities'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    #Symbols
    
    Symbols = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBar.Symbols)
    )
    Symbols.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/symbols'
    current_url = driver.current_url
    # assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    #Calculator
    Calculator = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBar.Calculator)
    )
    Calculator.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/widgets'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    #Tickets
    Tickets = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBar.Tickets)
    )
    Tickets.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/support-tickets'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    #FAQ
    FAQ = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBar.FAQ)
    )
    FAQ.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = 'https://help.fundednext.com/en'
    current_url = driver.current_url
    # assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    driver.get(DASHBOARD)

    #profile pic

    #tabs

    #search box

    #filter

    #banners


    return driver
