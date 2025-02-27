import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *
from .popupsclose import *
from .intercom import *

def comps():
        
    driver = perform__valid_login()
    close_popUp(driver)
    
    #Competition
    Competition = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBar.Competition)
    )
    Competition.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/competition'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    expected_header_title = "FundedNext Trade Master Cup"
    expected_header_subtitle = "Join the Trade Master Cup, showcase your trading skills, climb the leaderboard, and compete for a $35,000 grand prize with just a $35 entry fee!"

    headertitle = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(competitionelement.COMP_TITLE)
    )
    assert headertitle.is_displayed(), "title not displayed"
    actual_header_titile = headertitle.text.strip()
    assert actual_header_titile == expected_header_title, f"Expected '{expected_header_title}', but found '{actual_header_titile}'"

    headersubtitle = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(competitionelement.COMP_SUBTITLE)
    )
    assert headersubtitle.is_displayed(), "subtitle not displayed"
    actual_header_subtitle =  " ".join(headersubtitle.text.split()).strip()
    assert actual_header_subtitle == expected_header_subtitle, f"Expected '{expected_header_subtitle}', but found '{actual_header_subtitle}'"

    intercomicon(driver)

    alertnocomp = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(competitionelement.alertcontainer)
    )
    alertnocomp.is_displayed()

    #tmc Tabs
    tmcup = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((competitionelement.tmc))
    )
    assert tmcup.is_displayed()

   #free Tabs
    freetab = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((competitionelement.free))
    )
    assert freetab.is_displayed()

    #comp list Tabs
    complist = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((competitionelement.comp_list))
    )
    assert complist.is_displayed()

   #upcoming Tabs
    upcoming = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((competitionelement.upcoming))
    )
    assert upcoming.is_displayed()

    #inprogress Tabs
    inprogress = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((competitionelement.in_progress))
    )
    assert inprogress.is_displayed()

   #finished Tabs
    finished = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((competitionelement.finished))
    )
    assert finished.is_displayed()

    return driver