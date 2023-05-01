from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import os
import time

from selenium.webdriver.common.alert import Alert



class FindLocation(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://the-internet.herokuapp.com/")
        # Chromoptions
        webdriver.ChromeOptions().add_argument('--allow-geolocation=true')

    def test_geolocation(self):
        # testcase for https://the-internet.herokuapp.com/geolocation
        self.driver.find_element(By.LINK_TEXT, "Geolocation").click()

        self.driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(5)

        latitude = self.driver.find_element(By.ID, "lat-value").text
        print(latitude)

        longtitude = self.driver.find_element(By.ID, "long-value").text
        print(longtitude)





    def tearDown(self) -> None:
        self.driver.close()
