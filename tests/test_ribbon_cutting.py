import unittest
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from dp_common.mode import Mode
from unbounded_knapsack.ribbon_cutting import RibbonCutting


class TestRibbonCutting(unittest.TestCase):
    def test_something(self):
        ribbon_cutting = RibbonCutting()
        self.assertEqual(ribbon_cutting.ribbon_cutting(2), 1)
        self.assertEqual(ribbon_cutting.ribbon_cutting(3), 2)
        self.assertEqual(ribbon_cutting.ribbon_cutting(4), 4)
        self.assertEqual(ribbon_cutting.ribbon_cutting(5), 6)
        self.assertEqual(ribbon_cutting.ribbon_cutting(10), 36)

        self.assertEqual(ribbon_cutting.ribbon_cutting_memo(2), 1)
        self.assertEqual(ribbon_cutting.ribbon_cutting_memo(3), 2)
        self.assertEqual(ribbon_cutting.ribbon_cutting_memo(4), 4)
        self.assertEqual(ribbon_cutting.ribbon_cutting_memo(5), 6)
        self.assertEqual(ribbon_cutting.ribbon_cutting_memo(10), 36)

        self.assertEqual(ribbon_cutting.ribbon_cutting_tab(2), 1)
        self.assertEqual(ribbon_cutting.ribbon_cutting_tab(3), 2)
        self.assertEqual(ribbon_cutting.ribbon_cutting_tab(4), 4)
        self.assertEqual(ribbon_cutting.ribbon_cutting_tab(5), 6)
        self.assertEqual(ribbon_cutting.ribbon_cutting_tab(10), 36)


if __name__ == '__main__':
    unittest.main()
