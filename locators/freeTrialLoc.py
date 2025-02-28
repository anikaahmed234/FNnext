from selenium.webdriver.common.by import By

class FreeTrialButton:
        FREE_TRIAL = (By.XPATH, "//button[contains(text(), 'Free Trial')]")
        GET_STARTED_BUTTON = (By.XPATH, "//button[contains(., 'Get Started')]") 
        CHECKBOX = (By.ID, "Free Trial | 15K-1")
        PAYMENT_METHOD_TEXT = (By.XPATH, "//h1[contains(text(), 'Select Account Size')]")
        THANK_YOU_MSG = (By.XPATH, "//h3[contains(text(), 'Thank you for starting FundedNext Free Trial!')]")
        START_CHALLENGE_BUTTON = (By.ID, "free-trial-account")
        HAVE_FT = (By.CLASS_NAME, "ant-tooltip-inner")
     