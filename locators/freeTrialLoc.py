from selenium.webdriver.common.by import By

class FreeTrialButton:
        Free_Trial = (By.XPATH, "//button[contains(@data-plan, 'Free Trial')]")
        GET_STARTED_BUTTON = (By.XPATH, "//button[contains(., 'Get Started')]")
        CHECKBOX = (By.CSS_SELECTOR, "#Free Trial | 50K-3")
        PAYMENT_METHOD_TEXT = (By.XPATH, "//h1[contains(text(), 'Select Account Size')]")
        Thank_you_msg = (By.XPATH, "//h3[contains(text(), 'Thank you for starting FundedNext Free Trial!')]")
        START_CHALLENGE_BUTTON = (By.LINK_TEXT, "Start Challenge")