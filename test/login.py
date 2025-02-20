from locators import *
from utilities.config import get_driver, USERNAME, PASSWORD, URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform__valid_login():

    driver = get_driver()
    driver.get(URL)

    # Login
    username = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
    )
    password = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)

    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)

    login = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
    login.click()

    return driver

def perform__invalid_login():

    driver = get_driver()
    driver.get(URL)
    print("logging..")
    # Login
    username = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
    )
    password = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)

    username.send_keys(USERNAME)
    password.send_keys("1234")

    login = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
    login.click()

    return driver