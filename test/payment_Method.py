from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *

def paymentCard(driver):

    international_card = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(PaymentPageLocators.INTERNATIONAL_CARD)
    )
    international_card.click()

    # iframe_locator = PaymentPageLocators.iframe
    # WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))

    # print(iframe_locator)
    # card_locator = PaymentPageLocators.card
    # card_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(card_locator))
    # card_element.click()

    # first_name = WebDriverWait(driver, 20).until(
    # EC.visibility_of_element_located(PaymentPageLocators.first_name)
    # )
    # first_name.send_keys("Anika")
    # print(first_name)

    return driver