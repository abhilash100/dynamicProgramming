import unittest
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from dp_common.mode import Mode
from generic.buy_and_sell_stock import BuyAndSellStock


class TestBuyAndSellStock(unittest.TestCase):
    def test_buy_and_sell_stock1(self):
        buy_and_sell_stock = BuyAndSellStock()

        self.assertEqual(buy_and_sell_stock.buy_and_sell_stock1([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(buy_and_sell_stock.buy_and_sell_stock1([7, 6, 4, 3, 1]), 0)
        self.assertEqual(buy_and_sell_stock.buy_and_sell_stock1([3, 2, 6, 5, 0, 3]), 4)
        self.assertEqual(buy_and_sell_stock.buy_and_sell_stock1([1]), 0)

        self.assertEqual(buy_and_sell_stock.buy_and_sell_stock1_tab([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(buy_and_sell_stock.buy_and_sell_stock1_tab([7, 6, 4, 3, 1]), 0)
        self.assertEqual(buy_and_sell_stock.buy_and_sell_stock1_tab([3, 2, 6, 5, 0, 3]), 4)
        self.assertEqual(buy_and_sell_stock.buy_and_sell_stock1_tab([1]), 0)

if __name__ == '__main__':
    unittest.main()
