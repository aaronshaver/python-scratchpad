from radial_print import radial_print 
import unittest

class TestRadialPrint(unittest.TestCase):

    def test_single_letter(self):
        self.assertEqual('a', radial_print('a'))

    def test_empty(self):
        self.assertEqual('', radial_print(''))

    def test_two_letter(self):
        expected = 'sss\nsis\nsss'
        self.assertEqual(expected, radial_print('is'))

    def test_three_letter(self):
        self.assertEqual('e e e\n hhh \nehthe\n hhh \ne e e',
            radial_print('the'))

    def test_two_word(self):
        self.assertEqual('d   d   d\n c  c  c \n   bbb   \ndc bab cd\n'
            '   bbb   \n c  c  c \nd   d   d',
            radial_print('ab', 'cd'))
