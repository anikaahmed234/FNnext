from selenium.webdriver.common.by import By

class CompetitionLocator:
    COMP_TITLE = (By.CLASS_NAME, "competition_hero_container_title")
    COMP_SUBTITLE = (By.CLASS_NAME, "competition_hero_container_desc")
    ALERT_CONTAINER = (By.CLASS_NAME, "competition_alert_text_container")
    TMC = (By.XPATH,  "//div[text()='Trade Master Cup']")
    FREE = (By.XPATH, "//div[text()='Free']")
    UPCOMING = (By.XPATH, "//div[text()='Upcoming']")
    COMP_LIST = (By.XPATH, "//div[text()='Competition List']")
    FINISHED = (By.XPATH, "//div[text()='Finished']")
    IN_PROGRESS = (By.XPATH, "//div[text()='In Progress']")
