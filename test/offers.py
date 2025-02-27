import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.config import DASHBOARD

from locators import *
from .login import *
from .pop_ups_close import *
from .intercom import *
from .announcement import *

def my_offers_menu(driver):
        
    # driver = perform__valid_login()
    # close_popUp(driver)

    #My_Offers
    MyOffer = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(MyOfferPageLocator.MY_OFFER_MENU)
    )
    MyOffer.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/user-offer'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    expected_header_title = "Your Exclusive Offer"
    expected_header_subtitle = (
    "Discover Customised offer crafted just for you. Boost your trading journey with "
    "tailored discounts, special deals and unique rewards."
)

    headertitle = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(MyOfferPageLocator.HEADER_TITLE)
    )
    assert headertitle.is_displayed(), "title not displayed"
    actual_header_titile = headertitle.text.strip()
    assert actual_header_titile == expected_header_title, f"Expected '{expected_header_title}', but found '{actual_header_titile}'"

    headersubtitle = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(MyOfferPageLocator.HEADER_SUBTITLE)
    )
    assert headersubtitle.is_displayed(), "subtitle not displayed"
    actual_header_subtitle =  " ".join(headersubtitle.text.split()).strip()
    assert actual_header_subtitle == expected_header_subtitle, f"Expected '{expected_header_subtitle}', but found '{actual_header_subtitle}'"

    expected_empty_title = "No Coupons Available"
    expected_empty_subtitle = (
     "Trade with your current FundedNext Challenge Accounts to earn exclusive " 
     "discounts tailored just for you. Or, purchase any FundedNext Account today to get started "
     "on your rewarding trading journey."
    )
    emptytitle = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(MyOfferPageLocator.EMPTY_COUPON_TITLE)
    )

    assert emptytitle.is_displayed(), "not displayed"
    actual_empty_titile = emptytitle.text.strip()
    assert actual_empty_titile == expected_empty_title, f"Expected '{expected_empty_title}', but found '{actual_empty_titile}'"

    emptysubtitle = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(MyOfferPageLocator.EMPTY_COUPON_SUBTITLE)
    )
    assert emptysubtitle.is_displayed(), "not displayed"
    actual_empty_subtitle = " ".join(emptysubtitle.text.split()).strip()
    assert actual_empty_subtitle == expected_empty_subtitle, f"Expected '{expected_empty_subtitle}', but found '{actual_empty_subtitle}'"

    intercomicon(driver)

    driver.get(DASHBOARD)
    announcement_close(driver)

    return driver