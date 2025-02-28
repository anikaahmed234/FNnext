from selenium.webdriver.common.by import By

class DashboardPageLocators:
    DASHBOARD_TITLE = (By.CLASS_NAME, "account-hero-v2__text-block--title")
    START_CHALLENGE_BUTTON = (By.LINK_TEXT, "Start Challenge")
    CLOSE_BUTTON = (By.CLASS_NAME, "ant-notification-notice-close")
    FN_LOGO = (By.XPATH, '//*[@alt="fundednext-text-logo"]/following-sibling::*')
    USER = (By.CLASS_NAME, "protected-header__avatar")
    SEARCH = (By.CLASS_NAME, "account-search")
    REFER_AND_EARN = (By.LINK_TEXT, "Refer and Earn")
    ACCOUNT = (By.CLASS_NAME, "account-hero-v2__text-block--title")
    ACCOUNT_SUBTITLE = (By.CLASS_NAME, "account-hero-v2__text-block--subtitle")
