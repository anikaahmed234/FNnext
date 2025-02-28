
from locators import *
from .login import *
from .pop_ups_close import *
from .intercom import *
from .sidebar import *
from .transaction import *
from .tools import *
from .offers import *
from .tickets import *
from .dashboard import *
from .calculator import *
from .competition import *
from .card_purchase import *
from .payout import *
from .free_Trial import *
from .logout import *

def all():
    print("🚀 Starting yeee...")

    driver = perform__valid_login()
    close_popUp(driver)
    landingPage(driver)
    free_trial(driver)
    transaction_menu(driver)
    calc(driver)
    payout_menu(driver)
    my_offers_menu(driver)
    free_trial(driver)
    competition_menu(driver)
    tools_menu(driver)
    ticket_menu(driver)
    cardPurchasemenu(driver)
    # doLogout(driver)

    print("Exiting project!!!")

    return driver