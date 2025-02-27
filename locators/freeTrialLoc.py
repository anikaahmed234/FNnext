from selenium.webdriver.common.by import By

class FreeTrialButton:
        FREE_TRIAL = (By.XPATH, "//button[contains(@data-plan, 'Free Trial')]")
        GET_STARTED_BUTTON = (By.XPATH, "//button[contains(., 'Get Started')]")
        CHECKBOX = (By.CSS_SELECTOR, "#Free Trial | 50K-3")
        PAYMENT_METHOD_TEXT = (By.XPATH, "//h1[contains(text(), 'Select Account Size')]")
        THANK_YOU_MSG = (By.XPATH, "//h3[contains(text(), 'Thank you for starting FundedNext Free Trial!')]")
        START_CHALLENGE_BUTTON = (By.LINK_TEXT, "Start Challenge")
        CLOSE_ICON = (By.CLASS_NAME, "ant-notification-notice-close")
        CLOSE_TEXT = (By.XPATH, "//h3[contains(text(), 'nnouncement Registration for September Competition...'))]")