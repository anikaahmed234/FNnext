from selenium.webdriver.common.by import By

class TransactionPageLocators:
    title = (By.XPATH, "//p[contains(text(), 'Billing-Payment Method')]")
    payouthistory = (By.LINK_TEXT, "Payout History")
    Transactions = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Transactions']"
    subtitlepayout = (By.XPATH, "//p[contains(text(), 'Payout History')]")

    tradingUpdates = (By.XPATH, "//button[@type='button' and contains(@class, 'tw-absolute')]")
    referPopUp = (By.CLASS_NAME, "close-button")
    colHead = (By.XPATH, "//thead//th")
    bilcolHead = (By.XPATH, "//thead//th")