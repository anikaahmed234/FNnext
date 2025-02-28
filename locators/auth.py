from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.ID, "basic_email")
    PASSWORD_INPUT = (By.ID, "basic_password")
    LOGIN_BUTTON = (By.ID, "login-btn-gtag")
    ERROR_USER_MSG = (By.CLASS_NAME, "ant-form-item-explain-error")
    ERROR_PASS_MSG = (By.CLASS_NAME, "ant-notification-notice-message")
