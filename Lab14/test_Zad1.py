import unittest
import numpy as np
from Zad1 import zad1


class Zad1TestCase(unittest.TestCase):
    def test_poprawny_wynik(self):
        self.assertRaises(AssertionError, zad1, 'test', '')
        self.assertWarns(UserWarning, zad1, 'chess_games.csv', '')
        np.testing.assert_array_almost_equal(zad1('chess_games.csv','white'),[20058.,49.86], decimal=2)



if __name__ == '__main__':
    unittest.main()
