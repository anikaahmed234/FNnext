import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *
from .popupsclose import *
from .intercom import *

def payoutHistory():
        
    driver = perform__valid_login()

    close_popUp(driver)

    #Transactions
    Transactions = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(TransactionPageLocators.Transactions)
    )
    Transactions.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/billing/billing-history'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    title_name = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(TransactionPageLocators.title)
    )
    assert title_name.is_displayed(), "title name is not visible"
    intercom(driver)

   #columns
    expected_bilcol_names = ["SN", "Account No","Payment Method", "Status", "Date", "Transaction ID","Transition Type", "Paid Amount", "Funding Package", "Payment Proof" ]

    tabs = WebDriverWait(driver, 10).until(
         EC.presence_of_all_elements_located((TransactionPageLocators.colHead))
    )

    actual_bilcol_names = [tab.text.strip() for tab in tabs]

    assert actual_bilcol_names == expected_bilcol_names, f"Expected tabs {expected_bilcol_names}, but found {actual_bilcol_names}"

    for expected in expected_bilcol_names:
        assert expected in actual_bilcol_names, f"Expected tab '{expected}' not found in actual tabs: {actual_bilcol_names}"

    payoutHistoryopt = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(TransactionPageLocators.payouthistory)
    )
    payoutHistoryopt.click()

    subtitle_name = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(TransactionPageLocators.subtitlepayout)
    )
    assert subtitle_name.is_displayed(), "subtitle name is not visible"


    totaldollar = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(TransactionPageLocators.totalAmount)
    )
    assert totaldollar.is_displayed(), "total amount is not visible"

   #columns
    expected_col_names = ["SN", "Account No", "Wallet Address", "Methods", "Status", "Disbursed Date","Amount" ]

    tabs = WebDriverWait(driver, 10).until(
         EC.presence_of_all_elements_located((TransactionPageLocators.bilcolHead))
    )

    actual_col_names = [tab.text.strip() for tab in tabs]

    assert actual_col_names == expected_col_names, f"Expected tabs {expected_col_names}, but found {actual_col_names}"

    for expected in expected_col_names:
        assert expected in actual_col_names, f"Expected tab '{expected}' not found in actual tabs: {actual_col_names}"

    return driver
    