import unittest
import subprocess
import sys
import os

class TestNumberDictionary(unittest.TestCase):

    def run_main(self):
        result = subprocess.run(
            [sys.executable, os.path.join(os.path.dirname(__file__), '..', 'main.py')],
            capture_output=True, text=True
        )
        return result.stdout.strip().splitlines()

    def get_numbers_dict(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "main", os.path.join(os.path.dirname(__file__), '..', 'main.py'))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.numbers

    def test_seven(self):
        d = self.get_numbers_dict()
        self.assertEqual(d[7], 'seven', "numbers[7] should be 'seven'")

    def test_ten(self):
        d = self.get_numbers_dict()
        self.assertEqual(d[10], 'ten', "numbers[10] should be 'ten'")

    def test_output_has_ten_lines(self):
        lines = self.run_main()
        self.assertEqual(len(lines), 10, "Output should have exactly 10 lines")

    def test_output_format(self):
        lines = self.run_main()
        self.assertEqual(lines[0], '1 = one', "First line should be '1 = one'")
        self.assertEqual(lines[6], '7 = seven', "7th line should be '7 = seven'")

if __name__ == '__main__':
    unittest.main()
