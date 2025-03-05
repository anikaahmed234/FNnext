from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *

def paymentCard(driver):

    international_card = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(PaymentPageLocators.INTERNATIONAL_CARD)
    )
    international_card.click()

    return driver