import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *
from .sidebar import *
from .pop_ups_close import *
from .intercom import *

def payout_menu(driver):
    print("🚀 Payout menu...")

    Payout = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBarLocator.PAYOUT) 
    )
    Payout.click(), "sidebar is not visible after login"
    
    driver.set_page_load_timeout(30)
    time.sleep(3)

    expected_url = f'{URL}/payout'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"
        
    payout_list = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ol[style*='list-style: auto']"))
    )

    list_items = payout_list.find_elements(By.CSS_SELECTOR, "li.payment-method__text")

    expected_texts = [
        "The 24 hour payout guarantee will be applicable after you request the payout. Make sure to enter correct payout method details. Press the 'Payout Request' button to start the 24-hour payout guarantee. Remember, incorrect information can cause delays, potentially depriving you of our 24-hour payout promise.",
        "You will be able to withdraw the 15% profit share once you make 10% growth (for Stellar 1-Step challenge phase and Stellar 2-Step Challenge phases) in your FundedNext Account.",
        "If your payout request is marked with an Additional Due Diligence status due to an incorrect wallet address, please re-submit your request using the correct information to avoid further delays.",
        "With the first payout, you will receive the Reward Bonus. For Stellar Lite, you will get it on the third payout.",
        "If you are unable to request the payout, please check your email; the Department of Trading Ethics & Standards (trading@fundednext.com) may have reached out to you regarding some concerns.",
        "Please note that a provider fee of up to 3% for all methods will be applied to every payout requests."
    ]

    for index, item in enumerate(list_items):
        actual_text = item.text.strip()
        expected_text = expected_texts[index]
        assert actual_text == expected_text, f"❌ Mismatch at item {index+1}:\nExpected: {expected_text}\nFound: {actual_text}"
     #    print(f"✅ Item {index+1} text verified.")

#     print("🎉 All payout article items verified successfully!")

    expected_col_names = ["Login", "Date", "Withdrawal ID", "Requested Amount", "Status", "Disbursed Amount", "Timer", "Payout Proof","Tx Id","Note"]

    cols = WebDriverWait(driver, 20).until(
         EC.presence_of_all_elements_located((PayoutLocator.COL_HEAD))
    )

    actual_tab_names = [col.text.strip() for col in cols]

    assert actual_tab_names == expected_col_names, f"Expected tabs {expected_col_names}, but found {actual_tab_names}"

    for expected in expected_col_names:
         assert expected in actual_tab_names, f"Expected tab '{expected}' not found in actual tabs: {actual_tab_names}"

    expected_method_names = ["Rise", "USDT", "USDC", "Wind"]

    methodnames = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((PayoutLocator.METHOD))
    )

    actual_method_names = [method.text.strip() for method in methodnames]

    assert actual_method_names == expected_method_names, f"Expected tabs {expected_method_names}, but found {actual_method_names}"

    for expected in expected_method_names:
           assert expected in actual_method_names, f"Expected tab '{expected}' not found in actual tabs: {actual_method_names}"
   
    print("Exiting Payout!!!")

    return driver