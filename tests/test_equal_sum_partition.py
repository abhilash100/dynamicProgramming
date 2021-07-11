import sys
import os
import unittest

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from dp_common.mode import Mode
from knapsack01.equal_sum_partition import EqualSumPartition


class EqualSumPartitionTest(unittest.TestCase):
    def test(self):
        espt = EqualSumPartition()
        self.assertEqual(espt.equal_sum_partition([1,5,11,5]), True)
        self.assertEqual(espt.equal_sum_partition([1,2,3,5]), False)

        self.assertEqual(espt.equal_sum_partition_memo([1,5,11,5]), True)
        self.assertEqual(espt.equal_sum_partition_memo([1,2,3,5]), False)


if __name__ == '__main__':
    unittest.main()
