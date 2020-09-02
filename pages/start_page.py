from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StartPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    YES_RADIO = "#currently_insuredstart .custom-control:nth-child(1) > .custom-control-label-wrap"
    CONDO_RADIO = "#residence_ownershipstart .custom-control:nth-child(2) > .custom-control-label-wrap"
    REASON_RADIO = "#user_intentstart .custom-control:nth-child(1) > .custom-control-label-wrap"
    SAVE_BTN = "startSaveBtn"

    def click_yes_option(self):
        select_car_radio = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.YES_RADIO))
        )
        select_car_radio.click()

    def click_condo_option(self):
        select_condo_radio = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.CONDO_RADIO))
        )
        select_condo_radio.click()

    def click_reason_option(self):
        select_paytoomuch_radio = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.REASON_RADIO))
        )
        select_paytoomuch_radio.click()

    def click_save_button(self):
        start_save_btn = self.driver.find_element(By.ID, self.SAVE_BTN)
        start_save_btn.click()

    def verify_discount_insured(self):
        text = self.driver.find_element(
            By.CSS_SELECTOR, ".d-xl-block .discount-item:nth-child(1) > .discount-title-short").text

        return text

    def verify_discount_condo(self):
        text = self.driver.find_element(
            By.CSS_SELECTOR, ".d-xl-block .discount-item:nth-child(2) > .discount-title-short").text

        return text







