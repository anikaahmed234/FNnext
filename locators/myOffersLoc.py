from selenium.webdriver.common.by import By

class MyOfferPageLocator:
        MY_OFFER_MENU = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='My Offers']"
        HEADER_TITLE = By. CLASS_NAME, "user-coupon--header--title"
        HEADER_SUBTITLE = By. CLASS_NAME, "user-coupon--header--sub-title"
        EMPTY_COUPON_TITLE = By.CLASS_NAME, "user-coupon--empty--title"        
        EMPTY_COUPON_SUBTITLE = By.CLASS_NAME, "user-coupon--empty--sub-title"
        CARD = By.CLASS_NAME, "user-coupon--card--tag" 
        OFFER_TAG = By.CLASS_NAME, "OfferBadge"
        OFFER_TITLE = By.CLASS_NAME, "user-coupon--card--title"
        OFFER_SUBTITILE = By.CLASS_NAME, "user-coupon--card--secondary-title"
        PLAN_TITLE = By.CLASS_NAME, "user-coupon--card--tertiary-title"
        DESCRIPTION = By.CLASS_NAME, "user-coupon--card--normal-text"
        APPLY = By.CLASS_NAME, "user-coupon--card--footer--button-style"
        VALID_DATE = By.CLASS_NAME, "user-coupon--card--footer--validity-title"
        SERVER = By.XPATH, "//span[@class='ant-tag css-w0hv9i'and text()='Server: All servers']"
        PERCENTAGE = By.CSS_SELECTOR, "img[src*='percentage-tag.png']"
        DOLLAR = By.CSS_SELECTOR, "img[src*='dollar-tag.png']"
