from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverDetailsPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    GENDER = "[data-cy='gender-0-Male-Radiobutton']"
    MARTIAL_STATUS = "[data-cy='marital_status-0-Single-Radiobutton']"
    CREDIT_SCORE = "#credit_score-0 .custom-control:nth-child(1) > .custom-control-label-wrap"
    EDUCATION = "[data-cy='education-0-Bachelor'SDegree-Radiobutton']"
    YEARS = "[data-cy='insured_length-0-MoreThan3Years-Radiobutton']"
    PROVIDER = "[data-cy='current_carrierInput']"
    ACCIDENTS = "[data-cy='violations-0-No-Radiobutton']"
    EMAIL = "[data-cy='email']"
    DRIVER_OPTION = "[data-cy='add_another-0-No-Radiobutton']"
    QUOTES_BTN = "[data-cy='show_my_quotes']"

    def click_gender(self):
        gender_radio = WebDriverWait(self.driver, 20, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.GENDER))
        )
        gender_radio.click()

    def click_martial_status(self):
        matrial_status_radio = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.MARTIAL_STATUS))
        )
        matrial_status_radio.click()

    def click_credit_score(self):
        credit_score_radio = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.CREDIT_SCORE))
        )
        credit_score_radio.click()

    def click_eduction(self):
        eduction_radio = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.EDUCATION))
        )
        eduction_radio.click()

    def click_years(self):
        years_radio = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.YEARS))
        )
        years_radio.click()

    def enter_provider(self):
        provider = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.PROVIDER))
        )
        provider.send_keys()

    def click_accidents(self):
        accidents_radio = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.ACCIDENTS))
        )
        accidents_radio.click()

    def enter_email(self):
        email = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.EMAIL))
        )
        email.send_keys('xxxx@gmail.com')

    def click_driver_option(self):
        driver_radio = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.DRIVER_OPTION))
        )
        driver_radio.click()

    def click_show_quotes_btn(self):
        quotes_btn = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.QUOTES_BTN))
        )
        quotes_btn.click()