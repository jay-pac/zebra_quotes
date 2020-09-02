from selenium.webdriver.common.by import By


class SelectInsurancePage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    ZIPCODE = "(//input[@data-cy='zipcode-form-control'])[1]"
    START_BTN = "(//button[@data-cy='zipcode-submit-button'])[1]"

    def enter_zipcode(self):
        zip = self.driver.find_element(By.XPATH, self.ZIPCODE)
        zip.send_keys(78702)

    def click_start_button(self):
        start_btn = self.driver.find_element(By.XPATH, self.START_BTN )
        start_btn.click()


