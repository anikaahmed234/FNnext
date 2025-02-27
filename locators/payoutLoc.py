from selenium.webdriver.common.by import By

class PayoutLocator:
    COL_HEAD = (By.XPATH,("//thead//th"))
    METHOD = (By.CLASS_NAME, "method")