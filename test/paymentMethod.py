from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

def paymentMethod(driver):
    
    payment_method_text = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(PaymentPageLocators.PAYMENT_METHOD_TEXT)
    )

    international_card = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(PaymentPageLocators.INTERNATIONAL_CARD)
    )
    international_card.click()

    return driver