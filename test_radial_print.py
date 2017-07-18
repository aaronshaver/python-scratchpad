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
        expected = 'b b b\n     \nb A b\n     \nb b b'
        self.assertEqual(expected, radial_print('A', 'b'))
