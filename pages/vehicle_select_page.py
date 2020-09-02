from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VehicleSelectPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    VEHICLE_YEAR = ""
    VEHICLE_MAKE = ""
    VEHICLE_MODEL = ""
    VEHICLE_TRIM = ""
    SAVE_BUTTON = ""

    def select_vehicle_year(self):
        pass

    def select_vehicle_make(self):
        pass

    def select_vehicle_model(self):
        pass

    def select_vehicle_trim(self):
        pass

    def click_save_button(self):
        pass
