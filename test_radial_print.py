from radial_print import radial_print 
import unittest

class TestRadialPrint(unittest.TestCase):

    def test_single_letter(self):
        self.assertEqual('a', radial_print('a'))

    def test_empty(self):
        self.assertEqual('', radial_print(''))

    def test_two_letter(self):
        self.assertEqual('sss\nsis\nsss', radial_print('is'))

    def test_three_letter(self):
        self.assertEqual('e e e\n hhh \nehthe\n hhh \ne e e\n',
            radial_print('the'))
