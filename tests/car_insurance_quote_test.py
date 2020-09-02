from selenium import webdriver
import pytest


class TestCarQuotes():

    def setup(self):
        base_url = "https://www.thezebra.com/"
        self.driver = webdriver.Chrome()
        self.driver.get(base_url)
        self.driver.maximize_window()

    def test_create_quote(self):
        pass

    def teardown(self):
        self.driver.quit()
