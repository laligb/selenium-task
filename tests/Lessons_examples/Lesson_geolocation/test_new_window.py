from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import os
import time





class FindLocation(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://the-internet.herokuapp.com/")
        # Chromoptions


    def test_geolocation(self):
        # testcase for https://the-internet.herokuapp.com/geolocation
        self.driver.find_element(By.LINK_TEXT, "Multiple Windows").click()

        original_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) == 1

        self.driver.find_element(By.LINK_TEXT,'Click Here').click()
        time.sleep(5)

        # check there are 2 window-tags open now
        assert len(self.driver.window_handles) == 2

        self.driver.switch_to.new_window('tab')

        assert self.driver.page_source.find("New Window")






    def tearDown(self) -> None:
        self.driver.close()
