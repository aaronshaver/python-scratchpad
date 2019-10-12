import unittest
import word_numbers

class Tests(unittest.TestCase):
    # run tests with this command:
    # python -m unittest word_numbers_test.py

    def test_number_one(self):
        self.assertEqual("one", word_numbers.convert(1))