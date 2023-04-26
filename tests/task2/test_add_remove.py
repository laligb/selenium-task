# 1st task from the homework #2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

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

        try:
            # element = WebDriverWait(driver, 5).until\
            #     (EC.presence_of_element_located(By.LINK_TEXT, "Add/Remove Elements"))
            # el = WebDriverWait(self.driver, 5).until\
            #      (EC.presence_of_element_located(By.LINK_TEXT, "Add/Remove Elements"))
            # #print(driver.current_url)
            # el.assertEqual(self.driver.current_url, "https://the-internet.herokuapp.com/add_remove_elements/")
            # assert driver.page_source.find("Add/Remove Elements")
            self.driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()



        except:
            print("ERROR")



    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


# addrem = AddRemoveElements()
# addrem.test_add_remove_elements()
