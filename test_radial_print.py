from radial_print import RadialPrint
import unittest

class TestRadialPrint(unittest.TestCase):

    def setUp(self):
        self.r = RadialPrint()

    def test_single_letter(self):
        self.assertEqual('a', self.r.radial('a'))

    def test_empty(self):
        self.assertEqual('', self.r.radial(''))

    def test_two_letter(self):
        self.assertEqual('sss\nsis\nsss', self.r.radial('is'))

    def test_three_letter(self):
        self.assertEqual('e e e\n hhh \nehthe\n hhh \ne e e\n',
            self.r.radial('the'))
