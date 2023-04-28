# 2nd task from the homework #2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class DynamicContent(unittest.TestCase):
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

    def test_dynamic_content(self):
        print("testing start...")
        print("Trying to enter on https://the-internet.herokuapp.com/dynamic_content/")

        # Get URL
        self.driver.find_element(By.LINK_TEXT, "Dynamic Content").click()
        print(self.driver.current_url)
        self.assertEqual(self.driver.current_url, "https://the-internet.herokuapp.com/dynamic_content")
        print("Done!")

        # Check the primary content
        print("\n --------------------------------------------\n \nPrimary Content:\n")
        content_before = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "large-10")))
        content_before_text = content_before.text
        print(content_before_text)

        # Refresh the page and check if content changed
        print("\n--------------------------------------------")
        print("Refreshing page and expect changing content")
        self.driver.refresh()

        print("\n--------------------------------------------\n \nContent after refresh:\n")
        content_after = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "large-10")))
        content_after_text = content_after.text
        print(content_after_text)

        # Check with assertion
        self.assertNotEqual(content_before_text, content_after_text)

        print("Done!")


    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "main":
    unittest.main()
