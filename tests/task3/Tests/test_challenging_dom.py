import os
import sys
import allure

# Add parent directory to the system path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

from  Steps.challenging_dom_steps import MainSteps
import unittest

class TestChallengingDom(unittest.TestCase):

    @allure.description("Finds elements and checks that every of them is finishing on 0")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Finds elements of Table")
    @allure.suite("grouped by Finding elements")
    @allure.feature("Finding functionality")
    def test_challenging_dom(self):
        MainSteps.setUp(self)
        MainSteps.go_to_challenging_dom(self)
        MainSteps.find_table_row(self)

        # Assertion in test
        # split = MainSteps.find_table_row_
        # for word in split:
        #     self.assertEqual("0", word[-1])

        MainSteps.tearDown(self)




if __name__ == "__main__":
    unittest.main()
