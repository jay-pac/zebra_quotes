from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VehicleSelectPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    VEHICLE_YEAR = "[data-cy='year-0Input']"
    VEHICLE_MAKE = "[data-cy='make-0Input']"
    VEHICLE_MODEL = "[data-cy='model-0Input']"
    VEHICLE_TRIM = "[data-cy='submodel-0Input']"
    SAVE_BUTTON = "vehiclesSelectSaveBtn"

    def select_vehicle_year(self):
        select_year = WebDriverWait(self.driver, 20, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.VEHICLE_YEAR))
        )
        select_year.click()
        select_year.send_keys("2018")
        select_year.send_keys(Keys.ENTER)

    def select_vehicle_make(self):
        select_make = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.VEHICLE_MAKE))
        )
        select_make.click()
        select_make.send_keys("BMW")
        select_make.send_keys(Keys.ENTER)

    def select_vehicle_model(self):
        select_modal = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.VEHICLE_MODEL))
        )
        select_modal.click()
        select_modal.send_keys("3 Series")
        select_modal.send_keys(Keys.ENTER)

    def select_vehicle_trim(self):
        select_trim = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.VEHICLE_TRIM))
        )
        select_trim.send_keys("320i 4dr Sedan SA")
        select_trim.send_keys(Keys.ENTER)

    def click_save_button(self):
        vehicle_save_btn = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.ID, self.SAVE_BUTTON))
        )
        vehicle_save_btn.click()

    def verify_newcar_discount(self):
        new_car = WebDriverWait(self.driver, 20, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".d-xl-block .discount-item:nth-child(3) > .discount-title-short"))
        ).text

        return new_car
