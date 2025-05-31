from locators import *
from utilities.config import get_driver, USERNAME, PASSWORD, URL, log_error
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Perform a valid login and handle errors with logging and screenshot

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
    except Exception as e:
        log_error(f"UAT Server DOWN or login failed: {e}", driver, screenshot_name="login_error.png")
    return driver

# Perform an invalid login and handle errors with logging and screenshot

def perform__invalid_login():
    driver = get_driver()
    driver.get(URL)
    print("logging into FundedNext..")
    try:
        username = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        password = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        username.send_keys("1")
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
            log_error(f"Error checking email: {e}", driver, screenshot_name="invalid_login_email_error.png")
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
                  username.clear
                  password.clear
            else:
                print("dunno")
        except Exception as e:
            log_error(f"Error checking password: {e}", driver, screenshot_name="invalid_login_pass_error.png")
        username.send_keys(" ")
        password.send_keys(" ")
        login.click()
        try:  
            error = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(LoginPageLocators.ERROR_USER_MSG)
            )
            if(error.is_displayed()):
                print("Why I'm not in!!!")
                error_text = error.text.strip()
                if(error_text == "Please enter valid email"):
                  print("Oh! Space")
            else:
                print("dunno")
        except Exception as e:
            log_error(f"Error checking email (space): {e}", driver, screenshot_name="invalid_login_space_error.png")
        perform__valid_login()
    except Exception as e:
        log_error(f"Invalid login flow failed: {e}", driver, screenshot_name="invalid_login_flow_error.png")
    return driver

