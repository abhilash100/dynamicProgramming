import unittest
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from dp_common.mode import Mode
from knapsack01.subset_sum import SubsetSum


class SubsetSumTest(unittest.TestCase):
    def test_knapsack01(self):
        subset_sum = SubsetSum()
        # Test subset sum with recursion
        self.assertEqual(subset_sum.subset_sum([3, 34, 4, 12, 5, 2], 9), True)
        self.assertEqual(subset_sum.subset_sum([3, 34, 4, 12, 5, 2], 35), False)
        self.assertEqual(subset_sum.subset_sum([3, 4, 5, 2], 6), True)
        self.assertEqual(subset_sum.subset_sum([3, 4, 5, 2], 15), False)

        # Test subset sum with memo
        self.assertEqual(subset_sum.subset_sum_memo([3, 34, 4, 12, 5, 2], 9), True)
        self.assertEqual(subset_sum.subset_sum_memo([3, 34, 4, 12, 5, 2], 35), False)
        self.assertEqual(subset_sum.subset_sum_memo([3, 4, 5, 2], 6), True)
        self.assertEqual(subset_sum.subset_sum_memo([3, 4, 5, 2], 15), False)

        # Test subset sum with tabulation
        self.assertEqual(subset_sum.subset_sum_tab([3, 34, 4, 12, 5, 2], 9), True)
        self.assertEqual(subset_sum.subset_sum_tab([3, 34, 4, 12, 5, 2], 35), False)
        self.assertEqual(subset_sum.subset_sum_tab([3, 4, 5, 2], 6), True)
        self.assertEqual(subset_sum.subset_sum_tab([3, 4, 5, 2], 15), False)

if __name__ == '__main__':
    unittest.main()
