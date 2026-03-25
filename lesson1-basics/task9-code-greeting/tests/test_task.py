import unittest
import importlib.util
import os

def load_main():
    spec = importlib.util.spec_from_file_location(
        "main", os.path.join(os.path.dirname(__file__), '..', 'main.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

class TestGetGreeting(unittest.TestCase):

    def setUp(self):
        self.mod = load_main()

    def test_morning(self):
        self.assertEqual(self.mod.get_greeting(8), 'Good morning!',
                         "Hour 8 should return 'Good morning!'")

    def test_afternoon(self):
        self.assertEqual(self.mod.get_greeting(14), 'Good afternoon!',
                         "Hour 14 should return 'Good afternoon!'")

    def test_evening(self):
        self.assertEqual(self.mod.get_greeting(19), 'Good evening!',
                         "Hour 19 should return 'Good evening!'")

    def test_night(self):
        self.assertEqual(self.mod.get_greeting(23), 'Good night!',
                         "Hour 23 should return 'Good night!'")

    def test_midnight(self):
        self.assertEqual(self.mod.get_greeting(0), 'Good morning!',
                         "Hour 0 (midnight) should return 'Good morning!'")

    def test_noon(self):
        self.assertEqual(self.mod.get_greeting(12), 'Good afternoon!',
                         "Hour 12 (noon) should return 'Good afternoon!'")

if __name__ == '__main__':
    unittest.main()
