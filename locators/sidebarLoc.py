from selenium.webdriver.common.by import By

class SideBarLocator:
        ACCOUNTS = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Accounts']"
        TRANSACTION = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Transactions']"
        PAYOUT = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Payout']"
        COMPETITION = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Competition']"
        MY_OFFER = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='My Offers']"
        TOOLS = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Tools']"       
        SYMBOLS = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Symbols']"
        CALCULATOR = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Calculator']"
        INFINITY_POITNS = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='InfinityPoints']"
        TICKETS = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Tickets']"
        FAQ = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='FAQ']"
        