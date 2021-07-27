from dp_common.mode import Mode
from dp_common.dp_solve import DpSolveInterface

""""
Implementation of Solution for Buy and Sell Stock Problem
    -> Implement Using Recursion only
    -> Implement using Memoization
    -> Implement Using Tabulation

    Leetcode Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class BuyAndSellStock(DpSolveInterface):

    def buy_and_sell_stock1(self, prices):
        if len(prices) == 1:
            return 0

        profit = self.buy_and_sell_stock1_rec(prices, -1, 0)
        if profit <= 0:
            return 0
        else:
            return profit

    def buy_and_sell_stock1_rec(self, prices, min_val, idx):
        # Base case
        if min_val == -1:
            min_val = prices[idx]
            return self.buy_and_sell_stock1_rec(prices, min_val, idx+1)
        if idx == len(prices) - 1:
            if min_val == -1:
                return 0
            else:
                return prices[idx] - min_val

        # Actual algorithm
        # Option 1: Sell at idx
        opt1 = prices[idx] - min_val

        # Option 2: Sell later
        new_min_val = min(min_val, prices[idx])
        opt2 = self.buy_and_sell_stock1_rec(prices, new_min_val, idx+1)

        return max(opt1, opt2)

    def buy_and_sell_stock1_tab(self, prices):
        dp = []
        for i in range(len(prices)):
            dp.append(-1)

        min_val = prices[0]
        dp[0] = 0

        for i in range(1, len(prices)):
            if prices[i - 1] >= prices[i]:
                dp[i] = dp[i - 1]
            else:
                dp[i] = max(dp[i - 1], prices[i] - min_val)

            if prices[i] < min_val:
                min_val = prices[i]

        # print(str(dp))
        return dp[len(prices) - 1]


    def solve(self, mode, *args):
        prices = args[0]

        max_profit = 0
        print("Solving buy and sell stock problem in mode " + str(mode) + "...")
        if mode == Mode.RECURSION:
            max_profit = self.buy_and_sell_stock1(prices)
        elif mode == Mode.MEMOIZATION:
            max_profit = self.buy_and_sell_stock1_tab(prices)
        elif mode == Mode.TABULATION:
            max_profit = self.buy_and_sell_stock1_tab(prices)

        print("Max profit: " + str(max_profit))
