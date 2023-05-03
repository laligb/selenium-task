import os
import sys
import allure

# Add parent directory to the system path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

from  Steps.shifting_content_steps import MainSteps
import unittest

class TestShiftingContent(unittest.TestCase):

    @allure.description("checking changing of image and its position")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("changing image")
    @allure.suite("grouped by Finding elements")
    @allure.feature("Finding functionality")
    def test_shifting_content(self):
        MainSteps.setUp(self)
        MainSteps.go_to_shifting_content(self)
        MainSteps.go_to_example1(self)
        MainSteps.move_mouse(self)
        MainSteps.go_back(self)
        MainSteps.go_to_example2(self)
        MainSteps.click_and_check_image(self)
        MainSteps.position_check(self)
        MainSteps.tearDown(self)


if __name__ == "__main__":
    unittest.main()
