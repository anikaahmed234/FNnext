from selenium.webdriver.common.by import By

class FreeTrialButton:
        FREE_TRIAL = (By.XPATH, "//button[contains(text(), 'Free Trial')]")
        GET_STARTED_BUTTON = (By.XPATH, "//button[contains(., 'Get Started')]") 
        CHECKBOX = (By.ID, "Free Trial | 15K-1")
        PAYMENT_METHOD_TEXT = (By.XPATH, "//h1[contains(text(), 'Select Account Size')]")
        THANK_YOU_MSG = (By.XPATH, "//h3[contains(text(), 'Thank you for starting FundedNext Free Trial!')]")
        START_CHALLENGE_BUTTON = (By.ID, "free-trial-account")
        HAVE_FT = (By.CLASS_NAME, "ant-tooltip-inner")
        FREE_TITLE = (By.CSS_SELECTOR, ".account-wrapper__create-account h4")
        DASHBOARD_FT = (By.XPATH, "//h3[contains(text(), 'Free Trial')]/ancestor::div[contains(@class, 'dashboard-tour-content')]//button")
        IMPORTANT_NOTICE =(By.CLASS_NAME, "ant-dropdown-trigger")
        LOGIN_ID_HEADER = (By.CSS_SELECTOR, ".view-input-data p")
        HELLO_USERNAME = (By.CLASS_NAME, "accountDetails__profile-heading")
        ACCOUNT_DETAILS_TITLE = (By.CSS_SELECTOR, ".accountDetails__card-heading h3")
        DETAILS_TAGS = (By.CLASS_NAME, ".view-input-data")
        TRADING_CYCLE = (By.CSS_SELECTOR, ".accountDetails__col-third H3")
        START_DATE = (By.CSS_SELECTOR, ".accountDetails__col-third p:nth-child(1)")
        END_DATE = (By.CSS_SELECTOR, ".accountDetails__col-third p:nth-child(2)")
        STATS_TITLE= (By.CSS_SELECTOR, ".account-overview-card__heading h2")
        STATS_CARDS = (By.CLASS_NAME, "account-data-section__col")
        CONTACT = (By.LINK_TEXT, "Contact")
        EMAIL_SUPPORT = (By.CSS_SELECTOR, ".support-card-wrap__account-manager h3")
        REFRESHING_IN = (By.CSS_SELECTOR, ".account-overview-card__heading h2:nth-child(2)")
        TRADING_OBJ_TITLE = (By.CSS_SELECTOR, ".account-overview-card__heading h2")
        TRADING_OBJ_CARDS = (By.CLASS_NAME, "objective-single-card")
        
         

