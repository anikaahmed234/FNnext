from locators import *
from utilities.config import get_driver, USERNAME, PASSWORD, URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform__valid_login():

    try:
        driver = get_driver()
        driver.get(URL)

        print("logging into FundedNext..")

        username = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        password = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        login = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login.click()

        print("Yahoooo!!! Logged in...")

    except:
        print("UAT Server DOWN!")

    return driver

def perform__invalid_login():

    driver = get_driver()
    driver.get(URL)
    
    print("logging into FundedNext..")

    username = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
    )
    password = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)

    username.send_keys("a")
    password.send_keys("1")

    login = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
    login.click()
   
    try:
        error = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.ERROR_USER_MSG)
        )
        if(error.is_displayed()):
            print("Why I'm not in!!!")
            error_text = error.text.strip()
            if(error_text == "Please enter valid email"):
                print("Invalid email")
                username.clear
                password.clear
        else:
            print("dunno")

    except Exception as e:
        print(f"Error checking email: {e}")

    username.send_keys(USERNAME)
    password.send_keys("1")
    login.click()

    try:  
        error = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.ERROR_PASS_MSG)
        )
        if(error.is_displayed()):
            print("Why I'm not in!!!")
            error_text = error.text.strip()
            if(error_text == "The password must be at least 6 characters."):
              print("Oh! Incorrect Password")
        else:
            print("dunno")
    except Exception as e:
        print(f"Error checking email: {e}")

    perform__valid_login()
    return driver

