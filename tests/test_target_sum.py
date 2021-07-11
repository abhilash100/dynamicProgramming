import unittest
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from dp_common.mode import Mode
from knapsack01.target_sum import TargetSum


class TestTargetSum(unittest.TestCase):
    def test_something(self):
        target_sum = TargetSum()
        self.assertEqual(target_sum.target_sum([1,1,1,1,1], 3), 5)
        self.assertEqual(target_sum.target_sum([1], 1), 1)

        self.assertEqual(target_sum.target_sum_memo([1,1,1,1,1], 3), 5)
        self.assertEqual(target_sum.target_sum_memo([1], 1), 1)


if __name__ == '__main__':
    unittest.main()
