import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators import *
from config import get_driver, USERNAME, PASSWORD, URL, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def perform_login():

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
