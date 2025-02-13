import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators import *
from config import get_driver, USERNAME, PASSWORD, URL, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def paymentMethod(driver):
    
    payment_method_text = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(PaymentPageLocators.PAYMENT_METHOD_TEXT)
    )

    international_card = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(PaymentPageLocators.INTERNATIONAL_CARD)
    )
    international_card.click()

    return driver