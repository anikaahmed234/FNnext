from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

driver = webdriver.Chrome()
driver.get("URL")
driver.maximize_window() 

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "basic_email"))
)

password = driver.find_element(By.ID, "basic_password")

load_dotenv()  

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

username.send_keys(USERNAME)
password.send_keys(PASSWORD)
                   
login = driver.find_element(By.ID, "login-btn-gtag")
login.click()

dashboard = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "account-hero-v2__text-block--title"))
)

assert dashboard.is_displayed(), "Dashboard is not visible after login"

start_challenge = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Start Challenge"))
)
start_challenge.click()

checkout = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.tw-text-center.tw-font-Rebond"))
)

assert checkout.is_displayed(), "Checkout is not visible after redirect"

image_element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Evaluation')]"))
)
image_element.click()

get_plan = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-plan, 'Evaluation $25,000')]"))
)
get_plan.click()
time.sleep(5)

checkbox_element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#addon-3"))
)
if not checkbox_element.is_selected():
    checkbox_element.click()

button_element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Get Started')]"))
)
button_element.click()

payment_method_text = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Select a payment method')]"))
)

international_card = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//span[text()='International Cards']"))
)
international_card.click()

payment_method_text = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Select a payment method')]"))
)
print("Completed!")
driver.quit()
