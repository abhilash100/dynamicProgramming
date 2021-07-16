import unittest
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from dp_common.mode import Mode
from unbounded_knapsack.unbounded_knapsack import UnboundedKnapsack


class TestUnboundedKnapsack(unittest.TestCase):
    def test(self):
        unbounded_knapsack = UnboundedKnapsack()
        self.assertEqual(unbounded_knapsack.unbounded_knapsack(8, [1, 3, 4, 5], [10, 40, 50, 70]), 110)
        self.assertEqual(unbounded_knapsack.unbounded_knapsack(100, [1, 50], [1, 30]), 100)

        self.assertEqual(unbounded_knapsack.unbounded_knapsack_memo(8, [1, 3, 4, 5], [10, 40, 50, 70]), 110)
        self.assertEqual(unbounded_knapsack.unbounded_knapsack_memo(100, [1, 50], [1, 30]), 100)

        self.assertEqual(unbounded_knapsack.unbounded_knapsack_tab(8, [1, 3, 4, 5], [10, 40, 50, 70]), 110)
        self.assertEqual(unbounded_knapsack.unbounded_knapsack_tab(100, [1, 50], [1, 30]), 100)


if __name__ == '__main__':
    unittest.main()
