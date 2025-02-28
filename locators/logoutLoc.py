from selenium.webdriver.common.by import By

class LogoutLocator:
    HAMBURGER = (By.CLASS_NAME, "protected-header__user-name")
    LOGOUT = (By.CLASS_NAME, "ant-dropdown-menu-item")
