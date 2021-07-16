import unittest
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from dp_common.mode import Mode
from generic.longest_increasing_subsequence import LongestIncreasingSubsequence


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test(self):
        lis = LongestIncreasingSubsequence()
        self.assertEqual(lis.longest_increasing_subsequence_memo([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(lis.longest_increasing_subsequence_memo([0, 1, 0, 3, 2, 3]), 4)
        self.assertEqual(lis.longest_increasing_subsequence_memo([7, 7, 7, 7, 7, 7, 7]), 1)
        self.assertEqual(lis.longest_increasing_subsequence_memo([1, 3, 6, 7, 9, 4, 10, 5, 6]), 6)

        self.assertEqual(lis.longest_increasing_subsequence_tab([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(lis.longest_increasing_subsequence_tab([0, 1, 0, 3, 2, 3]), 4)
        self.assertEqual(lis.longest_increasing_subsequence_tab([7, 7, 7, 7, 7, 7, 7]), 1)
        self.assertEqual(lis.longest_increasing_subsequence_tab([1, 3, 6, 7, 9, 4, 10, 5, 6]), 6)





if __name__ == '__main__':
    unittest.main()
