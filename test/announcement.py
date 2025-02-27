from selenium.webdriver import ActionChains

from locators import *
from .login import *

def announcement_close(driver):
    hover_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-notification-notice"))  
    )
    ActionChains(driver).move_to_element(hover_element).perform()

    pops = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "anticon-close-circle"))
    )
    for pop in pops:
         ActionChains(driver).move_to_element(pop).click().perform()
                    
    return driver