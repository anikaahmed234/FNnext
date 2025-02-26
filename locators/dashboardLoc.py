from selenium.webdriver.common.by import By

class DashboardPageLocators:
    DASHBOARD_TITLE = (By.CLASS_NAME, "account-hero-v2__text-block--title")
    START_CHALLENGE_BUTTON = (By.LINK_TEXT, "Start Challenge")
    close_button = (By.CLASS_NAME, "ant-notification-notice-close")
    FNlogo = (By.XPATH, '//*[@alt="fundednext-text-logo"]/following-sibling::*')
    user = (By.XPATH, '//*[@alt="user"]/following-sibling::*')
    search = (By.CLASS_NAME, "account-search")
    intercom = (By.CLASS_NAME, "intercom-lightweight-app-launcher-icon")
