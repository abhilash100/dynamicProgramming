import unittest
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from dp_common.mode import Mode
from knapsack01.knapsack01 import Knapsack01


class KnapsackTest(unittest.TestCase):
    def test_knapsack01(self):
        knapsack01 = Knapsack01()
        # Test knapsack with recursion
        self.assertEqual(knapsack01.knapsack01([10,20,30], [60,100,120], 50), 220)
        self.assertEqual(knapsack01.knapsack01([1,1,1], [10,20,30], 2), 50)

        # Test knapsack with memo
        self.assertEqual(knapsack01.knapsack01_memo([10,20,30], [60,100,120], 50), 220)
        self.assertEqual(knapsack01.knapsack01_memo([1,1,1], [10,20,30], 2), 50)

        # Test knapsack with tabulation
        self.assertEqual(knapsack01.knapsack01_tab([10, 20, 30], [60, 100, 120], 50), 220)
        self.assertEqual(knapsack01.knapsack01_tab([1, 1, 1], [10, 20, 30], 2), 50)


if __name__ == '__main__':
    unittest.main()
