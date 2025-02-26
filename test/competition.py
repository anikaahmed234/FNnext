import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *
from .popupsclose import *
from .intercom import *

def comp():
        
    driver = perform__valid_login()
    close_popUp(driver)

    expected_header_title = "FundedNext Trade Master Cup"
    expected_header_subtitle = "Join the Trade Master Cup, showcase your trading skills, climb the leaderboard, and compete for a $35,000 grand prize with just a $35 entry fee!"

    headertitle = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(myOfferpage.header_title)
    )
    assert headertitle.is_displayed(), "title not displayed"
    actual_header_titile = headertitle.text.strip()
    assert actual_header_titile == expected_header_title, f"Expected '{expected_header_title}', but found '{actual_header_titile}'"

    headersubtitle = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(myOfferpage.header_subtitle)
    )
    assert headersubtitle.is_displayed(), "subtitle not displayed"
    actual_header_subtitle =  " ".join(headersubtitle.text.split()).strip()
    assert actual_header_subtitle == expected_header_subtitle, f"Expected '{expected_header_subtitle}', but found '{actual_header_subtitle}'"


    intercomicon(driver)

    return driver