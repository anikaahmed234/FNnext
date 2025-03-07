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
    print("🚀 My offer menu...")

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

    try:
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

    except:
        print("cards found!")

    intercomicon(driver)
        
    #refer & earn
    refer = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(DashboardPageLocators.REFER_AND_EARN)
    )
    assert refer.is_displayed(), "refer & earn button is not visible on dashboard header"

    # issue: loop & description issue 

    try:
        cards = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located(MyOfferPageLocator.CARD)
        )

        card_count = len(cards)
        print(f"Card Count: {card_count}")
        for index, card in enumerate(cards):
            try:
              
                offer_tag = WebDriverWait(driver, 20).until(
                  EC.visibility_of_element_located(MyOfferPageLocator.OFFER_TAG)
                )  

                title_element = WebDriverWait(driver, 20).until(
                  EC.visibility_of_element_located(MyOfferPageLocator.OFFER_TITLE)
                )                
                title = title_element.text 

                subtitle_element = WebDriverWait(driver, 20).until(
                  EC.visibility_of_element_located(MyOfferPageLocator.OFFER_SUBTITILE)
                )     
                subtitle = subtitle_element.text  

                plan_title_element = WebDriverWait(driver, 20).until(
                  EC.visibility_of_element_located(MyOfferPageLocator.PLAN_TITLE)
                ) 

                plan_title = plan_title_element.text  
                
                description_element = WebDriverWait(driver, 20).until(
                  EC.visibility_of_element_located(MyOfferPageLocator.DESCRIPTION)
                )  
                  
                description = description_element.text  
                
                valid_date_element = WebDriverWait(driver, 20).until(
                  EC.visibility_of_element_located(MyOfferPageLocator.VALID_DATE)
                )  
                valid_date = valid_date_element.text  

                server_element = WebDriverWait(driver, 20).until(
                  EC.visibility_of_element_located(MyOfferPageLocator.SERVER)
                )  
                server = server_element.text  

                apply_button = WebDriverWait(driver, 20).until(
                  EC.visibility_of_element_located(MyOfferPageLocator.APPLY)
                )       

                print(f"Card {index + 1}:")
                print(f"Offer tag: {offer_tag.is_displayed()}")  
                print(f"Title: {title}")
                print(f"Subtitle: {subtitle}")
                print(f"Plan Title: {plan_title}")
                print(f"Description: {description}")
                print(f"Valid Date: {valid_date}")
                print(f"Server: {server}")
                print(f"Apply Button: {apply_button.is_displayed()}")  

            except Exception as e:
                print(f"Error extracting details from card {index + 1}: {e}")

    except Exception as e:
        print(e)
        print("no cards found!")

    # driver.get(DASHBOARD)
    # announcement_close(driver)
    print("Exiting my offer!!!")

    return driver