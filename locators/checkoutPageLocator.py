from selenium.webdriver.common.by import By

class CheckoutPageLocators:
    CHECKOUT_TITLE = (By.CSS_SELECTOR, "h2.tw-text-center.tw-font-Rebond")
    EVALUATION_BUTTON = (By.XPATH, "//button[contains(text(), 'Evaluation')]")
    PLAN_BUTTON = (By.XPATH, "//button[contains(@data-plan, 'Evaluation $25,000')]")
    CHECKBOX = (By.CSS_SELECTOR, "#addon-3")
    GET_STARTED_BUTTON = (By.XPATH, "//button[contains(., 'Get Started')]")

