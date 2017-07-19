from towers import Tower
import unittest

class TestTowers(unittest.TestCase):

    def test_1_disc(self):
        t = Tower()
        self.assertEqual(1, t.solve(1, 'A', 'B', 'C'))
    
    def test_2_discs(self):
        t = Tower()
        self.assertEqual(3, t.solve(2, 'A', 'B', 'C'))
    
    def test_3_discs(self):
        t = Tower()
        self.assertEqual(7, t.solve(3, 'A', 'B', 'C'))
    
    def test_4_discs(self):
        t = Tower()
        self.assertEqual(15, t.solve(4, 'A', 'B', 'C'))

    def test_5_discs(self):
        t = Tower()
        self.assertEqual(31, t.solve(5, 'A', 'B', 'C'))

    def test_6_discs(self):
        t = Tower()
        self.assertEqual(63, t.solve(6, 'A', 'B', 'C'))

    def test_20_discs(self):
        t = Tower()
        self.assertEqual(1048575, t.solve(20, 'A', 'B', 'C'))
