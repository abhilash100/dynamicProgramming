from dp_common.mode import Mode
from dp_common.dp_solve import DpSolveInterface
from sys import maxsize

"""
Implementation of Rod Cutting Problem
    -> Recursive Approach
    -> Memoization Approach
    -> Tabulation Approach

Problem Stmt: 
    Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n. 
    Determine the maximum value obtainable by cutting up the rod and selling the pieces.


Problem Link: https://www.geeksforgeeks.org/cutting-a-rod-dp-13/

"""


class RodCutting(DpSolveInterface):

    def rod_cutting(self, prices):
        n = len(prices)
        return self.rod_cutting_rec(n, prices)

    def rod_cutting_rec(self, n, prices):
        if n <= 0:
            return 0

        max_value = 0
        for i in range(n):
            max_value = max(max_value, prices[i] + self.rod_cutting_rec(n-i-1, prices))

        return max_value

    def rod_cutting_memo(self, prices):
        n = len(prices)
        dp = []

        for i in range(len(prices) + 1):
            dp.append(-1)

        dp[0] = 0
        return self.rod_cutting_memo_rec(n, prices, dp)

    def rod_cutting_memo_rec(self, n, prices, dp):
        if n <= 0:
            return 0

        if dp[n] != -1:
            return dp[n]

        max_value = 0
        for i in range(n):
            max_value = max(max_value, prices[i] + self.rod_cutting_memo_rec(n-i-1, prices, dp))

        dp[n] = max_value
        return dp[n]

    def rod_cutting_tab(self, prices):
        n = len(prices)
        dp = []

        for i in range(len(prices) + 1):
            dp.append(-1)

        dp[0] = 0
        for i in range(1, n+1):
            max_value = 0
            for j in range(0, i):
                max_value = max(max_value, prices[j] + dp[i-j-1])

            dp[i] = max_value

        #print(str(dp))
        return dp[n]


    def solve(self, mode, *args):
        prices = args[0]

        print("Rod cutting problem solved in mode " + str(mode) + " : ")
        print("With prices : " + str(prices))
        max_value = 0
        if mode == Mode.RECURSION:
            max_value = self.rod_cutting(prices)
        elif mode == Mode.MEMOIZATION:
            max_value = self.rod_cutting_memo(prices)
        elif mode == Mode.TABULATION:
            max_value = self.rod_cutting_tab(prices)
        print("Max value obtained: " + str(max_value))