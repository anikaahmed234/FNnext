from selenium.webdriver.common.by import By

class PopUpsLocator:
    TRADING_UPDATES_POP_UP = (By.XPATH, "//button[@type='button' and contains(@class, 'tw-absolute')]")
    REFER_POP_UP = (By.CLASS_NAME, "close-button")