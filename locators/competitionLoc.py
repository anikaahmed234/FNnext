from selenium.webdriver.common.by import By

class competitionelement:
    COMP_TITLE = (By.CLASS_NAME, "competition_hero_container_title")
    COMP_SUBTITLE = (By.CLASS_NAME, "competition_hero_container_desc")
    alertcontainer = (By.CLASS_NAME, "competition_alert_text_container")

    tmc = (By.XPATH, "//div[text()='Trade Master Cup' and contains(@class, 'tw-cursor-pointer')]")
    free = (By.XPATH, "//div[text()='Free' and contains(@class, 'tw-cursor-pointer')]")

    upcoming = (By.XPATH, "//div[text()='Upcoming' and contains(@class, 'tw-cursor-pointer')]")
    comp_list = (By.XPATH, "//div[text()='Competition List' and contains(@class, 'tw-cursor-pointer')]")
    finished = (By.XPATH, "//div[text()='Finished' and contains(@class, 'tw-cursor-pointer')]")
    in_progress = (By.XPATH, "//div[text()='In Progress' and contains(@class, 'tw-cursor-pointer')]")
