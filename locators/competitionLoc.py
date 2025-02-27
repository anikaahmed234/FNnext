from selenium.webdriver.common.by import By

class competitionelement:
    COMP_TITLE = (By.CLASS_NAME, "competition_hero_container_title")
    COMP_SUBTITLE = (By.CLASS_NAME, "competition_hero_container_desc")
    alertcontainer = (By.CLASS_NAME, "competition_alert_text_container")
    tmc = (By.XPATH,  "//div[text()='Trade Master Cup']")
    free = (By.XPATH, "//div[text()='Free']")
    upcoming = (By.XPATH, "//div[text()='Upcoming']")
    comp_list = (By.XPATH, "//div[text()='Competition List']")
    finished = (By.XPATH, "//div[text()='Finished']")
    in_progress = (By.XPATH, "//div[text()='In Progress']")
