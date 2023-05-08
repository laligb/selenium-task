import os
import sys
import allure

# Add parent directory to the system path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

from  Steps.key_presses_steps import MainSteps
import unittest

class TestKeyPresses(unittest.TestCase):

    def test_key_presses(self):
        MainSteps.setUp(self)
        MainSteps.go_to_challenging_dom(self)
        #MainSteps.input_key(self)


        self.assertIn(MainSteps.input_key(self,  "B"), MainSteps.result_text(self))
