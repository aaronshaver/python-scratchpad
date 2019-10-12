import unittest
from word_numbers import WordNumbers

class Tests(unittest.TestCase):
    # run tests with this command:
    # python -m unittest word_numbers_test.py

    def setUp(self):
        self.converter = WordNumbers()
        
    def test_get_digit_count_0(self):
        self.assertEqual(1, self.converter.get_digit_count(0))

    def test_get_digit_count_1(self):
        self.assertEqual(1, self.converter.get_digit_count(1))

    def test_get_digit_count_10(self):
        self.assertEqual(2, self.converter.get_digit_count(10))

    def test_get_digit_count_999(self):
        self.assertEqual(3, self.converter.get_digit_count(999))

    def test_convert_0(self):
        self.assertEqual("zero", self.converter.convert(0))

    def test_convert_1(self):
        self.assertEqual("one", self.converter.convert(1))

    def test_convert_2(self):
        self.assertEqual("two", self.converter.convert(2))

    def test_convert_4(self):
        self.assertEqual("four", self.converter.convert(4))

    def test_convert_5(self):
        self.assertEqual("five", self.converter.convert(5))

    def test_convert_6(self):
        self.assertEqual("six", self.converter.convert(6))

    def test_convert_7(self):
        self.assertEqual("seven", self.converter.convert(7))

    def test_convert_8(self):
        self.assertEqual("eight", self.converter.convert(8))

    def test_convert_9(self):
        self.assertEqual("nine", self.converter.convert(9))

    def test_convert_9_000(self):
        self.assertEqual("nine thousand", self.converter.convert(9000))
    
    def test_convert_17_000(self):
        self.assertEqual("seventeen thousand", self.converter.convert(17000))

    def test_convert_20(self):
        self.assertEqual("twenty", self.converter.convert(20))

    def test_convert_90_000(self):
        self.assertEqual("ninety thousand", self.converter.convert(90000))

    def test_convert_1_000_000(self):
        self.assertEqual("one million", self.converter.convert(1000000))

    def test_convert_82_000(self):
        self.assertEqual("eighty two thousand", self.converter.convert(82000))

    def test_convert_123(self):
        self.assertEqual("one hundred twenty three", self.converter.convert(123))

    def test_convert_876(self):
        self.assertEqual("eight hundred seventy six", self.converter.convert(876))
    
    def test_convert_900_000(self):
        self.assertEqual("nine hundred thousand", self.converter.convert(900000))

    def test_convert_145_000(self):
        self.assertEqual("one hundred forty five thousand", self.converter.convert(145000))

    def test_convert_140_000(self):
        self.assertEqual("one hundred forty thousand", self.converter.convert(140000))
    
    def test_convert_106(self):
        self.assertEqual("one hundred six", self.converter.convert(106))

    def test_convert_106_000(self):
        self.assertEqual("one hundred six thousand", self.converter.convert(106000))

    def test_convert_3(self):
        self.assertEqual("three", self.converter.convert(3))

    def test_convert_33(self):
        self.assertEqual("thirty three", self.converter.convert(33))

    def test_convert_333(self):
        self.assertEqual("three hundred thirty three", self.converter.convert(333))

    def test_convert_3333(self):
        self.assertEqual("three thousand three hundred thirty three", self.converter.convert(3333))

    def test_convert_33333(self):
        self.assertEqual("thirty three thousand three hundred thirty three", self.converter.convert(33333))

    def test_convert_333333(self):
        self.assertEqual("three hundred thirty three thousand three hundred thirty three", self.converter.convert(333333))
    
    def test_convert_123456(self):
        self.assertEqual("one hundred twenty three thousand four hundred fifty six", self.converter.convert(123456))
    
    def test_convert_987654(self):
        self.assertEqual("nine hundred eighty seven thousand six hundred fifty four", self.converter.convert(987654))
    
    def test_convert_101010(self):
        self.assertEqual("one hundred one thousand ten", self.converter.convert(101010))

    def test_convert_20002(self):
        self.assertEqual("twenty thousand two", self.converter.convert(20002))