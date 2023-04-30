from Steps.file_upload_steps import MainSteps
import unittest


class testFileUpload(unittest.TestCase):

    def test_file_upload(self):
         MainSteps.setUp()
         MainSteps.go_to_fileupload()
         MainSteps.file_upload()
         MainSteps.file_submit()
         self.assertTrue(MainSteps.check_results())
         MainSteps.tearDown()


if __name__ == "__main__":
    unittest.main()
