import unittest
import subprocess
import sys
import os

class TestIntroduction(unittest.TestCase):

    def run_main(self):
        result = subprocess.run(
            [sys.executable, os.path.join(os.path.dirname(__file__), '..', 'main.py')],
            capture_output=True, text=True
        )
        return result.stdout.strip().splitlines()

    def test_line1_my_name(self):
        lines = self.run_main()
        self.assertTrue(len(lines) >= 1, "Output should have at least 1 line")
        self.assertIn('My name is', lines[0], "Line 1 should start with 'My name is'")

    def test_line2_age(self):
        lines = self.run_main()
        self.assertTrue(len(lines) >= 2, "Output should have at least 2 lines")
        self.assertIn('I am', lines[1], "Line 2 should contain 'I am'")
        self.assertIn('years old', lines[1], "Line 2 should contain 'years old'")

    def test_line3_country(self):
        lines = self.run_main()
        self.assertTrue(len(lines) >= 3, "Output should have at least 3 lines")
        self.assertIn('I am from', lines[2], "Line 3 should contain 'I am from'")

if __name__ == '__main__':
    unittest.main()
