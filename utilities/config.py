import os
from selenium import webdriver
from dotenv import load_dotenv

from locators import *

load_dotenv()

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--disable-notifications")
# options.add_argument("--disable-popup-blocking")

USERNAME = os.getenv("TESTUSERNAME")
PASSWORD = os.getenv("PASSWORD")
URL = os.getenv("URL")
DASHBOARD = os.getenv("DASHBOARD")


def get_driver():
    driver = webdriver.Chrome(options=options)
    return driver
