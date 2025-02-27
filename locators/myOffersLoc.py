from selenium.webdriver.common.by import By

class MyOfferPageLocator:
        MY_OFFER_MENU = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='My Offers']"
        HEADER_TITLE = By. CLASS_NAME, "user-coupon--header--title"
        HEADER_SUBTITLE = By. CLASS_NAME, "user-coupon--header--sub-title"
        EMPTY_COUPON_TITLE = By.CLASS_NAME, "user-coupon--empty--title"        
        EMPTY_COUPON_SUBTITLE = By.CLASS_NAME, "user-coupon--empty--sub-title"