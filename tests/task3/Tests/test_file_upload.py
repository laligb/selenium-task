import os
import sys
import allure

# Add parent directory to the system path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

from  Steps.file_upload_steps import MainSteps
import unittest

class TestFileUpload(unittest.TestCase):

    @allure.description("checking if file is uploaded")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Uploading elements")
    @allure.suite("grouped by Finding elements")
    @allure.feature("Finding functionality")
    def test_file_upload(self):
        MainSteps.setUp(self)
        MainSteps.go_to_fileupload(self)
        MainSteps.file_upload(self, "images/khinkali.jpg")
        MainSteps.file_submit(self)
        self.assertTrue(MainSteps.check_results(self))
        MainSteps.tearDown(self)



if __name__ == "__main__":
    unittest.main()
