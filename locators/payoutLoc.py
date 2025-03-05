from selenium.webdriver.common.by import By

class PayoutLocator:
    COL_HEAD = (By.XPATH,("//thead//th"))
    METHOD = (By.CLASS_NAME, "method")
    REQUEST = (By.CSS_SELECTOR, ".withdraw-request h3")
    MINIMUM_PAYOUT = (By.CSS_SELECTOR, ".withdraw-request p")
    PAYOUT_METHOD = (By.CSS_SELECTOR, ".payment-method-wrapper h3")
    PAYOUT_METHOD_BODY = (By.CSS_SELECTOR, ".payment-method-wrapper p")
    PAYOUT_AMOUNT = (By.CSS_SELECTOR, ".withdraw-request .warning span")
    CARDS = (By.CSS_SELECTOR, ".withdraw-card-wrapper .withdraw-card .card-single")
    REFRESHING_IN = (By.CSS_SELECTOR, ".top-up-reset-history__head--title h3:nth-child(2)")
    AMOUNT = (By.CSS_SELECTOR, ".card-single h3")
    TITLE = (By.CSS_SELECTOR, ".card-single p")
