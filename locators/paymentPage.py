from selenium.webdriver.common.by import By

class PaymentPageLocators:
    PAYMENT_METHOD_TEXT = (By.XPATH, "//p[contains(text(), 'Select a payment method')]")
    INTERNATIONAL_CARD = (By.XPATH, "//span[text()='International Cards']")
