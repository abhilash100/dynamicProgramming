import unittest
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from dp_common.mode import Mode
from unbounded_knapsack.coin_change import CoinChange


class TestCoinChange(unittest.TestCase):
    def test_coin_change1(self):
        coin_change = CoinChange()
        self.assertEqual(coin_change.coin_change1_rec([1, 2, 5], 11), 3)
        self.assertEqual(coin_change.coin_change1_rec([2], 3), -1)
        self.assertEqual(coin_change.coin_change1_rec([1], 0), 0)
        self.assertEqual(coin_change.coin_change1_rec([1], 1), 1)
        self.assertEqual(coin_change.coin_change1_rec([1], 2), 2)

        self.assertEqual(coin_change.coin_change1_memo([1, 2, 5], 11), 3)
        self.assertEqual(coin_change.coin_change1_memo([2], 3), -1)
        self.assertEqual(coin_change.coin_change1_memo([1], 0), 0)
        self.assertEqual(coin_change.coin_change1_memo([1], 1), 1)
        self.assertEqual(coin_change.coin_change1_memo([1], 2), 2)

        self.assertEqual(coin_change.coin_change1_tab([1, 2, 5], 11), 3)
        self.assertEqual(coin_change.coin_change1_tab([2], 3), -1)
        self.assertEqual(coin_change.coin_change1_tab([1], 0), 0)
        self.assertEqual(coin_change.coin_change1_tab([1], 1), 1)
        self.assertEqual(coin_change.coin_change1_tab([1], 2), 2)


    def test_coin_change2(self):
        coin_change = CoinChange()
        self.assertEqual(coin_change.coin_change2([1,2,5], 5), 4)
        self.assertEqual(coin_change.coin_change2([2], 3), 0)
        self.assertEqual(coin_change.coin_change2([10], 10), 1)


if __name__ == '__main__':
    unittest.main()
