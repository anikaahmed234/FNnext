from selenium.webdriver.common.by import By

class myOfferpage:
        MyOffersmenu = By.XPATH, "//span[@class='sidebar__nav-link-title' and text()='My Offers']"
        header_title = By. CLASS_NAME, "user-coupon--header--title"
        header_subtitle = By. CLASS_NAME, "user-coupon--header--sub-title"
        emptycoupon_title = By.CLASS_NAME, "user-coupon--empty--title"        
        emptycoupon_subtitle = By.CLASS_NAME, "user-coupon--empty--sub-title"