import unittest
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from dp_common.mode import Mode
from unbounded_knapsack.rod_cutting import RodCutting


class TestRodCutting(unittest.TestCase):
    def test(self):
        rod_cutting = RodCutting()
        self.assertEqual(rod_cutting.rod_cutting([1, 5, 8, 9, 10, 17, 17, 20]), 22)
        self.assertEqual(rod_cutting.rod_cutting([3, 5, 8, 9, 10, 17, 17, 20]), 24)

        self.assertEqual(rod_cutting.rod_cutting_memo([1, 5, 8, 9, 10, 17, 17, 20]), 22)
        self.assertEqual(rod_cutting.rod_cutting_memo([3, 5, 8, 9, 10, 17, 17, 20]), 24)

        self.assertEqual(rod_cutting.rod_cutting_tab([1, 5, 8, 9, 10, 17, 17, 20]), 22)
        self.assertEqual(rod_cutting.rod_cutting_tab([3, 5, 8, 9, 10, 17, 17, 20]), 24)


if __name__ == '__main__':
    unittest.main()
