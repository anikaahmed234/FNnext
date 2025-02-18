import os
from selenium import webdriver
from dotenv import load_dotenv

from locators import *
from test import login

load_dotenv()

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-notifications")

USERNAME = os.getenv("TESTUSERNAME")
PASSWORD = os.getenv("PASSWORD")
URL = os.getenv("URL")

def get_driver():
    driver = webdriver.Chrome(options=options) 
    driver.get(URL)

    return driver