from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def announcement_close(driver):
    while True:
        try:
            hover_element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "ant-notification-notice"))
            )
            ActionChains(driver).move_to_element(hover_element).perform()

            pops = driver.find_elements(By.CSS_SELECTOR, "a.ant-notification-notice-close")
            
            if not pops:
                print("No more pop-ups found.")
                break
            
            for pop in pops:
                try:
                    ActionChains(driver).move_to_element(pop).click().perform()
                    print("Pop-up closed.")
                except Exception as e:
                    print(f"Error closing pop-up: {e}")
        
        except Exception as e:
            print("No pop-ups found or timeout reached.")
            break

    return driver
