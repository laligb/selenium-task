from Locators.key_presses_locators import MainLocators
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys



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
        self.driver.find_element(*MainLocators.link_text).click()

    @allure.step
    def input_key(self, key):
        self.driver.find_element(*MainLocators.input_field).send_keys(key)

        return key

    @allure.step
    def result_text(self):
        result = self.driver.find_element(*MainLocators.result).text
        print(result)
        return result


    def tearDown(self) -> None:
        self.driver.close()
