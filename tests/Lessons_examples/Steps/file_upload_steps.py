from Locators.file_upload_locators import MainLocators
# from driver import *
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class MainSteps(MainLocators):
    def __init__(self):
        self.driver = None

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install))
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/")

    @allure.step
    def go_to_fileupload():
        self.driver.find_element(MainLocators.link_text).click()

    @allure.step
    def file_upload(file_name):
        file_path = os.path.abspath(file_name)
        self.driver.find_element(MainLocators.file_upload).send_keys(file_path)

    @allure.step
    def file_submit():
        self.driver.find_element(MainLocators.file_submit).submit()

    def check_results():
        return self.driver.page_source.find("File Uploaded!")

    def tearDown(self) -> None:
        self.driver.close()
