import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.config import DASHBOARD

from locators import *
from .login import *

def sidebar_menu(driver):
    print("🚀 Checking Sideabars...")

    #account
    accounts = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBarLocator.ACCOUNTS)
    )
    accounts.click(), "❌ sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/accounts'
    current_url = driver.current_url
    try:
        assert current_url == expected_url, f"❌ Expected URL: {expected_url}, but got: {current_url}"
        print("✅ Redirected Successfully!!!")

    except AssertionError as msg:
            print(msg)
       
    #Transactions
    Transactions = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBarLocator.TRANSACTION)
    )
    Transactions.click(), "❌ sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/billing/billing-history'
    current_url = driver.current_url
    try:
        assert current_url == expected_url, f"❌ Expected URL: {expected_url}, but got: {current_url}"
        print("✅ Redirected Successfully!!!")

    except AssertionError as msg:
            print(msg)
            
    #Payout
    Payout = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBarLocator.PAYOUT)
    )
    Payout.click(), "❌ sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/payout'
    current_url = driver.current_url
    try:
        assert current_url == expected_url, f"❌ Expected URL: {expected_url}, but got: {current_url}"
        print("✅ Redirected Successfully!!!")

    except AssertionError as msg:
            print(msg)

    #Competition
    Competition = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBarLocator.COMPETITION)
    )
    Competition.click(), "❌ sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/competition'
    current_url = driver.current_url
    try:
        assert current_url == expected_url, f"❌ Expected URL: {expected_url}, but got: {current_url}"
        print("✅ Redirected Successfully!!!")

    except AssertionError as msg:
            print(msg)

    #My_Offers
    My_Offers = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBarLocator.MY_OFFER)
    )
    My_Offers.click(), "❌ sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/user-offer'
    current_url = driver.current_url
    try:
        assert current_url == expected_url, f"❌ Expected URL: {expected_url}, but got: {current_url}"
        print("✅ Redirected Successfully!!!")

    except AssertionError as msg:
            print(msg)
    driver.get(DASHBOARD)

    #Tools
    FILES = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBarLocator.FILES)
    )
    FILES.click(), "❌ sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/utilities'
    current_url = driver.current_url
    try:
        assert current_url == expected_url, f"❌ Expected URL: {expected_url}, but got: {current_url}"
        print("✅ Redirected Successfully!!!")

    except AssertionError as msg:
            print(msg)

    #Symbols
    Symbols = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBarLocator.SYMBOLS)
    )
    Symbols.click(), "❌ sidebar is not visible after login"

    time.sleep(3)

    expected_url = "https://uat-lander.fundednext.com/symbols"
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-1])
    current_url = driver.current_url

    try:
        assert current_url == expected_url, f"❌ Expected URL: {expected_url}, but got: {current_url}"
        print("✅ Redirected Successfully!!!")

    except AssertionError as msg:
            print(msg)
    
    driver.get(DASHBOARD)

    #Calculator
    Calculator = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBarLocator.CALCULATOR)
    )
    Calculator.click(), "❌ sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/widgets'
    current_url = driver.current_url
    try:
        assert current_url == expected_url, f"❌ Expected URL: {expected_url}, but got: {current_url}"
        print("✅ Redirected Successfully!!!")

    except AssertionError as msg:
            print(msg)
    
    #Tickets
    Tickets = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBarLocator.TICKETS)
    )
    Tickets.click(), "❌ sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/support-tickets'
    current_url = driver.current_url
    try:
        assert current_url == expected_url, f"❌ Expected URL: {expected_url}, but got: {current_url}"
        print("✅ Redirected Successfully!!!")

    except AssertionError as msg:
            print(msg)
    
    #FAQ
    FAQ = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBarLocator.FAQ)
    )
    FAQ.click(), "❌ sidebar is not visible after login"

    time.sleep(3)

    expected_url = 'https://help.fundednext.com/en'
    current_url = driver.current_url

    driver.get(DASHBOARD)
    print("sidebar checked!!!")

    return driver
