from dp_common.mode import Mode
from dp_common.dp_solve import DpSolveInterface
from sys import maxsize

"""
Implementation of Ribbon Cutting Problem
    -> Recursive Approach
    -> Memoization Approach
    -> Tabulation Approach

Problem Stmt: 
    Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that maximizes 
    product of lengths of all parts. You must make at least one cut. 
    Assume that the length of rope is more than 2 meters. 


Problem Link: https://www.geeksforgeeks.org/maximum-product-cutting-dp-36/

"""


class RibbonCutting(DpSolveInterface):
    def ribbon_cutting(self, n):
        return self.ribbon_cutting_rec(n)

    def ribbon_cutting_rec(self, n):
        if n <= 0:
            return 0

        if n == 1:
            return 1

        max_value = 0
        for i in range(1, n):
            max_value = max(max_value, max(n-i, self.ribbon_cutting_rec(n-i)) * i)

        return max_value

    def ribbon_cutting_memo(self, n):
        dp = []
        for i in range(0, n+1):
            dp.append(-1)

        dp[0] = 0
        dp[1] = 1

        return self.ribbon_cutting_memo_rec(n, dp)

    def ribbon_cutting_memo_rec(self, n, dp):
        if n <= 0:
            return 0

        if dp[n] != -1:
            return dp[n]

        max_value = 0
        for i in range(1, n):
            max_value = max(max_value, max(n-i, self.ribbon_cutting_memo_rec(n-i, dp)) * i)

        dp[n] = max_value
        return dp[n]

    def ribbon_cutting_tab(self, n):
        dp = []
        for i in range(0, n+1):
            dp.append(-1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            max_value = 0
            for j in range(1, n+1):
                max_value = max(max_value, max(i-j, dp[i-j]) * j)
            dp[i] = max_value

        #print(str(dp))

        return dp[n]

    def solve(self, mode, *args):
        ribbon_length = args[0]
        max_product = -1

        print("Solving max product problem in mode " + str(mode) + " for ribbon length: " + str(ribbon_length))
        if mode == Mode.RECURSION:
            max_product = self.ribbon_cutting(ribbon_length)
        elif mode == Mode.MEMOIZATION:
            max_product = self.ribbon_cutting_memo(ribbon_length)
        elif mode == Mode.TABULATION:
            max_product = self.ribbon_cutting_tab(ribbon_length)

        print("Max product: " + str(max_product))


