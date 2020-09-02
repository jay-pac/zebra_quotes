from selenium import webdriver
from pages.select_insurance_page import SelectInsurancePage
from pages.start_page import StartPage
import pytest


class TestCarQuotes():

    def setup(self):
        base_url = "https://www.thezebra.com/"
        self.driver = webdriver.Chrome()
        self.driver.get(base_url)
        self.driver.maximize_window()

    def test_create_quote(self):
        sip = SelectInsurancePage(self.driver)
        sp = StartPage(self.driver)

        # Select Insurance Page - Select Auto or Home Insurance
        sip.enter_zipcode()
        sip.click_start_button()

        # Start page - enter insurance, housing, reason for shopping info
        sp.click_yes_option()
        discount_insured = sp.verify_discount_insured()
        assert discount_insured == "Currently Insured"

        sp.click_condo_option()
        discount_condo = sp.verify_discount_condo()
        assert discount_condo == "Condo Owner"
        sp.click_reason_option()
        sp.click_save_button()

    def teardown(self):
        self.driver.quit()
