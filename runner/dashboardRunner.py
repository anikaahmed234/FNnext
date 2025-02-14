import sys
import os

# Add both 'main' and 'locators' folders to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))

from main.dashboard import *
from main.login import *

from utilities.config import get_driver, USERNAME, PASSWORD, URL, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = perform_login()
driver = dashboard(driver)
