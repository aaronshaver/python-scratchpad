import unittest
from word_numbers import WordNumbers

class Tests(unittest.TestCase):
    # run tests with this command:
    # python -m unittest word_numbers_test.py

    def test_get_digit_count_0(self):
        self.assertEqual(1, WordNumbers.get_digit_count(0))

    def test_get_digit_count_1(self):
        self.assertEqual(1, WordNumbers.get_digit_count(1))

    def test_get_digit_count_10(self):
        self.assertEqual(2, WordNumbers.get_digit_count(10))

    def test_get_digit_count_999(self):
        self.assertEqual(3, WordNumbers.get_digit_count(999))

    def test_number_one(self):
        self.assertEqual("one", WordNumbers.convert(1))