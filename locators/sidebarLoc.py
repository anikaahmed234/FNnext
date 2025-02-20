from selenium.webdriver.common.by import By

class SideBar:
        accounts = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Accounts']"
        Transactions = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Transactions']"
        Payout = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Payout']"
        Competition = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Competition']"
        My_Offers = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='My Offers']"
        Tools = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Tools']"       
        Symbols = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Symbols']"
        Calculator = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Calculator']"
        InfinityPoints = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='InfinityPoints']"
        Tickets = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='Tickets']"
        FAQ = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='FAQ']"
        