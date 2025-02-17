import os
from selenium import webdriver
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