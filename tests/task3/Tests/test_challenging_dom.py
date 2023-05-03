import os
import sys

# Add parent directory to the system path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

from  Steps.challenging_dom_steps import MainSteps
import unittest

class TestChallengingDom(unittest.TestCase):
    def test_challenging_dom(self):
        MainSteps.setUp(self)
        MainSteps.go_to_challenging_dom(self)
        MainSteps.find_table_row(self)

        # ERROR NEEDS TO BE SOLVE


if __name__ == "__main__":
    unittest.main()
