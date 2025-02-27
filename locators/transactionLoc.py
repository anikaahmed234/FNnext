from selenium.webdriver.common.by import By

class TransactionPageLocators:
    TITLE = (By.XPATH, "//p[contains(text(), 'Billing-Payment Method')]")
    PAYOUT_HISTORY = (By.LINK_TEXT, "Payout History")
    TRANSACTION = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Transactions']"
    SUBTITLE_PAYOUT = (By.XPATH, "//p[contains(text(), 'Payout History')]")
    TOTAL_AMOUNT = (By.XPATH, "//p[contains(text(), 'Total Amount: $')]")
    COL_HEAD = (By.XPATH, "//thead//th")
    BILL_COL_HEAD = (By.XPATH, "//thead//th")