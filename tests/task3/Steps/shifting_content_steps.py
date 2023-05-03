from Locators.shifting_content_locators import MainLocators
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

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
    def go_to_shifting_content(self):
        self.driver.find_element(*MainLocators.link_text).click()

    @allure.step
    def go_to_example1(self):
        self.driver.find_element(*MainLocators.link_text_example1).click()

    @allure.step
    def move_mouse(self):
        home = self.driver.find_element(*MainLocators.link_text_home)
        home_color_before = home.value_of_css_property('color')
        action = ActionChains(self.driver)
        action.move_to_element(home).perform()
        home_color_after = home.value_of_css_property('color')

        self.assertNotEqual(home_color_before, home_color_after)
        print(home_color_before, home_color_after)

    @allure.step
    def go_back(self):
        self.driver.back()

    @allure.step
    def go_to_example2(self):
        self.driver.find_element(*MainLocators.link_text_example2).click()


    @allure.step
    def click_and_check_image(self):
        image_click = self.driver.find_element(*MainLocators.link_of_image)
        image =  self.driver.find_element(*MainLocators.image_class)
        first_image = image.get_attribute('src')

        image_click.click()
        image =  self.driver.find_element(*MainLocators.image_class)
        second_image = image.get_attribute('src')

        self.assertNotEqual(first_image,second_image)


    @allure.step
    def position_check(self):
        image_click = self.driver.find_element(*MainLocators.link_of_image)
        image = self.driver.find_element(*MainLocators.image_class)
        position_before = image.value_of_css_property('left')

        image_click.click()
        image = self.driver.find_element(*MainLocators.image_class)
        position_after = image.value_of_css_property('left')

        self.assertNotEqual(position_before,position_after)



    def tearDown(self) -> None:
        self.driver.close()
