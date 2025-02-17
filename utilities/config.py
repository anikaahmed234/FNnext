import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from dotenv import load_dotenv

load_dotenv()

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  

USERNAME = os.getenv("TESTUSERNAME")
PASSWORD = os.getenv("PASSWORD")
URL = os.getenv("URL")

def get_driver():
    driver = webdriver.Chrome(options=options) 
    
    return driver
