from selenium.webdriver.common.by import By

class popUps:
    tradingUpdates = (By.XPATH, "//button[@type='button' and contains(@class, 'tw-absolute')]")
    referPopUp = (By.CLASS_NAME, "close-button")