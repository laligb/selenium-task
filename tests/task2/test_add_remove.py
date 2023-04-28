# 1st task from the homework #2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import allure

class AddRemoveElements(unittest.TestCase):
    def setUp(self) -> None:
        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            print("driver installed..")
            try:
                self.driver.get("https://the-internet.herokuapp.com/")
                print("website got..")
            except:
                print("Error in website.")
        except:
            print("driver not installed")

        finally:
            print("Setup finished.")


    def test_add_remove_elements(self):
        print("testing start...")
        print("Trying to enter on https://the-internet.herokuapp.com/add_remove_elements/")
        try:
            self.driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
            print(self.driver.current_url)
            self.assertEqual(self.driver.current_url, "https://the-internet.herokuapp.com/add_remove_elements/")
            print("Done!")
        except:
            print("There is some problem with URL")

        # Adding elements
        print("Adding 10 elements...")
        try:
            for i in range(10):
                self.driver.find_element(By.XPATH, '//button[normalize-space()="Add Element"]').click()

            elements = self.driver.find_elements(By.XPATH, '//button[normalize-space()="Delete"]')
            print(f"Amount of added elements: {len(elements)}")

            # Assertion

            self.assertEqual(len(elements), 10)
            print("Done!")

        except:
            print("There is problem with adding elements")


        # Removing elements
        print("Removing 7 element")

        try:
            for i in range(7):
                self.driver.find_element(By.XPATH, '//button[normalize-space()="Delete"]').click()

            remained_elements = self.driver.find_elements(By.XPATH, '//button[normalize-space()="Delete"]')
            print(f"Amount of remained elements: {len(remained_elements)}")

            # Assertion
            self.assertEqual(len(remained_elements), 3)
            print("Done!")

        except:
            print("Problem with deleting elements")



    def tearDown(self) -> None:
        self.driver.close()
