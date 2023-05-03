from Locators.challenging_dom_locators import MainLocators
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MainSteps(MainLocators):
    def __init__(self):
        self.driver = None

    def setUp(self) -> None:
        driver_path = ChromeDriverManager().install()
        self.driver = webdriver.Chrome(service=Service(executable_path=driver_path))
        #self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install))
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/")

    @allure.step
    def go_to_challenging_dom(self):
        print(self.driver)
        self.driver.find_element(*MainLocators.link_text).click()

    @allure.step
    def find_table_row(self):
        row = self.driver.find_element(*MainLocators.table_row)
        split = row.text.split()[0:6]
        print(split)
        for word in split:
            self.assertEqual("0", word[-1])


    def find_table_row_(self):
        row = self.driver.find_element(*MainLocators.table_row)
        split = row.text.split()[0:6]
        print(split)
        return split










    def tearDown(self) -> None:
        self.driver.close()
