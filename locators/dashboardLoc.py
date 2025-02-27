from selenium.webdriver.common.by import By

class DashboardPageLocators:
    DASHBOARD_TITLE = (By.CLASS_NAME, "account-hero-v2__text-block--title")
    # POP_UP = (By.CLASS_NAME, "ant-notification-notice")
    # POP_UP_CLOSE = (By.CLASS_NAME, "anticon-close-circle")
    START_CHALLENGE_BUTTON = (By.LINK_TEXT, "Start Challenge")
    CLOSE_BUTTON = (By.CLASS_NAME, "ant-notification-notice-close")
    FN_LOGO = (By.XPATH, '//*[@alt="fundednext-text-logo"]/following-sibling::*')
    USER = (By.XPATH, '//*[@alt="user"]/following-sibling::*')
    SEARCH = (By.CLASS_NAME, "account-search")
    REFER_AND_EARN = (By.LINK_TEXT, "Refer and Earn")
