from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StartDetailsPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    ADDRESS = "[data-cy='garaging_address_input']"
    FIRST_NAME = "[data-cy='first_name']"
    LAST_NAME = "[data-cy='last_name']"
    BIRTHDATE = "[data-cy='date_of_birth']"
    SAVE_BTN = "[data-cy='section_continue']"

    def enter_address(self):
        address_field = self.driver.find_element(By.CSS_SELECTOR, self.ADDRESS)
        address_field.send_keys("615 West 7th Street, Austin, TX, USA")

    def enter_first_name(self):
        fn = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.FIRST_NAME))
        )
        fn.click()
        fn.send_keys("John")
        fn.send_keys(Keys.ENTER)

    def enter_last_name(self):
        ln = self.driver.find_element(By.CSS_SELECTOR, self.LAST_NAME)
        ln.send_keys("Rambo")
        ln.send_keys(Keys.ENTER)

    def enter_birth_date(self):
        birth_date = self.driver.find_element(By.CSS_SELECTOR, self.BIRTHDATE)
        birth_date.send_keys("03/12/1989")
        birth_date.send_keys(Keys.ENTER)

    def click_continue_button(self):
        details_save_btn = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.SAVE_BTN))
        )
        details_save_btn.click()

    def verify_driver_name(self):
        driver_name = WebDriverWait(self.driver, 20, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".d-xl-block .fs-block > .item-info"))
        ).text

        return driver_name



