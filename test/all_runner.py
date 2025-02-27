
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

def all():
        
    driver = perform__valid_login()
    close_popUp(driver)
    landingPage(driver)
    # transaction_menu(driver)
    # calc(driver)
    # payout_menu(driver)
    # my_offers_menu(driver)
    # competition_menu(driver)
    # tools_menu(driver)
    # ticket_menu(driver)
    # cardPurchasemenu(driver)

    return driver