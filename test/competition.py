import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from .login import *
from .sidebar import *
from .pop_ups_close import *
from .intercom import *

def competition_menu(driver):
    print("🚀 Competition Menu...")

    #Competition
    Competition = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(SideBarLocator.COMPETITION)
    )
    Competition.click(), "sidebar is not visible after login"

    time.sleep(3)

    expected_url = f'{URL}/competition'
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    expected_header_title = "FundedNext Trade Master Cup"
    expected_header_subtitle = "Join the Trade Master Cup, showcase your trading skills, climb the leaderboard, and compete for a $35,000 grand prize with just a $35 entry fee!"

    headertitle = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(CompetitionLocator.COMP_TITLE)
    )
    assert headertitle.is_displayed(), "title not displayed"
    actual_header_titile = headertitle.text.strip()
    assert actual_header_titile == expected_header_title, f"Expected '{expected_header_title}', but found '{actual_header_titile}'"

    headersubtitle = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(CompetitionLocator.COMP_SUBTITLE)
    )
    assert headersubtitle.is_displayed(), "subtitle not displayed"
    actual_header_subtitle =  " ".join(headersubtitle.text.split()).strip()
    assert actual_header_subtitle == expected_header_subtitle, f"Expected '{expected_header_subtitle}', but found '{actual_header_subtitle}'"

    intercomicon(driver)
    
    #refer & earn
    # refer = WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located(DashboardPageLocators.REFER_AND_EARN)
    # )
    # try:
    #     assert refer.is_displayed(), "refer & earn button is not visible on dashboard header"
    #     print("✅ Refer button is visible!!!")

    # except AssertionError as msg:
    #     print(msg)

    alertnocomp = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(CompetitionLocator.ALERT_CONTAINER)
    )
    alertnocomp.is_displayed()

    #tmc Tabs
    tmcup = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((CompetitionLocator.TMC))
    )
    try:
        assert tmcup.is_displayed()
        print("✅ Trade Master Cup tab is visible!!!")

    except AssertionError as msg:
        print(msg)

    #free Tabs
    freetab = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((CompetitionLocator.FREE))
    )
    try:
        assert freetab.is_displayed()
        print("✅ Free tab is visible!!!")

    except AssertionError as msg:
        print(msg)

    #comp list Tabs
    complist = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((CompetitionLocator.COMP_LIST))
    )
    try:
        assert complist.is_displayed()
        print("✅ Competition List tab is visible!!!")

    except AssertionError as msg:
        print(msg)

    #upcoming Tabs
    upcoming = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((CompetitionLocator.UPCOMING))
    )
    try:
        assert upcoming.is_displayed()
        print("✅ Upcoming tab is visible!!!")

    except AssertionError as msg:
        print(msg)

    #inprogress Tabs
    inprogress = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((CompetitionLocator.IN_PROGRESS))
    )
    try:
        assert inprogress.is_displayed()
        print("✅ Inprogress tab is visible!!!")

    except AssertionError as msg:
        print(msg)

    #finished Tabs
    finished = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((CompetitionLocator.FINISHED))
    )
    try:
        assert finished.is_displayed()
        print("✅ Finish tab is visible!!!")

    except AssertionError as msg:
        print(msg)
        
    print("Exiting Competition!!!")

    return driver