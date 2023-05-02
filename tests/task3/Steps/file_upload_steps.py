from Locators.file_upload_locators import MainLocators
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class MainSteps(MainLocators):
    def __init__(self):
        self.driver = None

    def setUp(self) -> None:
        driver_path = ChromeDriverManager().install()
        self.driver = webdriver.Chrome(service=Service(executable_path=driver_path))
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install))
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/")

    @allure.step
    def go_to_fileupload(self):
        self.driver.find_element(*MainLocators.link_text).click()

    @allure.step
    def file_upload(self, file_name):
        file_path = os.path.abspath(file_name)
        self.driver.find_element(*MainLocators.file_upload).send_keys(file_path)
        time.sleep(2)

    @allure.step
    def file_submit(self):
        self.driver.find_element(*MainLocators.file_submit).submit()
        time.sleep(2)

    def check_results(self):
        return self.driver.page_source.find(MainLocators.success)

    def tearDown(self) -> None:
        self.driver.close()
