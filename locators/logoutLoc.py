from selenium.webdriver.common.by import By

class Logoutdrop:
    logout_icon = (By.CLASS_NAME, "protected-header__user-name")
    dropdown = (By.CLASS_NAME, "ant-dropdown-menu-title-content")
