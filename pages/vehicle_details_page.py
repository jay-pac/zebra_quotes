from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VehicleDetailsPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    OWN_OPTION = ""
    COMMUTE_OPTION = ""
    MILES = ""
    FREQUENCY = ""
    SAVE_BUTTON = ""


    def click_own_option(self):
        pass

    def click_commute_option(self):
        pass

    def enter_miles(self):
        pass

    def select_frequency(self):
        pass

    def click_save_button(self):
        pass