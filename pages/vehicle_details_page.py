from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VehicleDetailsPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    OWN_OPTION = "[data-cy='ownership-0-Own-PaidInFull-Radiobutton']"
    COMMUTE_OPTION = "[data-cy='primary_use-0-Personal/Commuting-Radiobutton']"
    MILES = "miles-input-0"
    FREQUENCY = '[data-cy="mileage_periodInput"]'
    SAVE_BUTTON = '[data-cy="section_continue"]'

    # TODO - Verify Selected Car
    def click_own_option(self):
        paid_full_radio = WebDriverWait(self.driver, 20, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.OWN_OPTION))
        )
        paid_full_radio.click()

    def click_commute_option(self):
        commute_radio = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.COMMUTE_OPTION))
        )
        commute_radio.click()

    def enter_miles(self):
        miles = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.ID, self.MILES))
        )
        miles.send_keys("10000")
        miles.send_keys(Keys.ENTER)

    def select_frequency(self):
        select = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.FREQUENCY))
        )
        select.click()

    def click_save_button(self):
        save_btn = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.SAVE_BUTTON))
        )
        save_btn.click()

    def verify_paid_in_full(self):
        paid = WebDriverWait(self.driver, 20, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".d-xl-block > .summary-rail-section:nth-child(1) .response-item:nth-child(1)"))
        ).text

        return paid