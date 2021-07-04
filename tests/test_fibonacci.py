import unittest
#import dp_common
#import generic

import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from dp_common.mode import Mode
from generic.fibonacci import Fibonacci


class FibonacciTest(unittest.TestCase):
    def test_base_case(self):
        fib = Fibonacci()
        self.assertEqual(fib.fibonacci(1), 0)
        self.assertEqual(fib.fibonacci_memo(1), 0)
        self.assertEqual(fib.fibonacci_tab(1), 0)

        self.assertEqual(fib.fibonacci(2), 1)
        self.assertEqual(fib.fibonacci_memo(2), 1)
        self.assertEqual(fib.fibonacci_tab(2), 1)

    def test(self):
        fib = Fibonacci()
        self.assertEqual(fib.fibonacci(5), 3)
        self.assertEqual(fib.fibonacci_memo(5), 3)
        self.assertEqual(fib.fibonacci_tab(5), 3)

        self.assertEqual(fib.fibonacci(20), 4181)
        self.assertEqual(fib.fibonacci_memo(20), 4181)
        self.assertEqual(fib.fibonacci_tab(20), 4181)


if __name__ == '__main__':
    unittest.main()
