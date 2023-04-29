# 3rd task from the homework #2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import os

class FileDownload(unittest.TestCase):
    def setUp(self) -> None:
        try:
            # Install driver with download directory options
            self.download_dir = os.path.abspath("tests/task2/Downloads")

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("prefs", {"download.default_directory": self.download_dir})

            # Here are adding options in driver:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
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

    def test_file_download(self):
        print("Testing start...")
        print("Trying to enter on https://the-internet.herokuapp.com/download/")

        # Get URL
        try:
            self.driver.find_element(By.LINK_TEXT, "File Download").click()
            print(self.driver.current_url)
            self.assertEqual(self.driver.current_url, "https://the-internet.herokuapp.com/download")
            print("Done!")
        except:
            print("Some problem with URL")

        # Get element
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Test.txt")))
        self.assertTrue(element)

        # Download element in directory "tests/task2/Downloads"
        element.click()
        downloaded_file_path = os.path.join(self.download_dir, "Test.txt")
        WebDriverWait(self.driver, 10).until(lambda x: os.path.exists(downloaded_file_path))

        # Assertion
        self.assertTrue(os.path.exists(downloaded_file_path))

        # Get Cookies
        print("----------------------------")
        print("Getting cookies...")
        self.driver.back()
        cookies = self.driver.get_cookies()
        print(cookies)

        # Assestion
        self.assertTrue(cookies)

        # Writing cookies in tests/task2/Cookies/cookies.txt
        print("Writing coookies in file...")
        f = open(os.path.abspath("tests/task2/Cookies/cookies.txt"), "a")
        f.write(str(cookies))
        f.close()

        print("Done!")



    def tearDown(self) -> None:
        self.driver.close()
