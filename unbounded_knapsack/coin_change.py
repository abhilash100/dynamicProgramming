from dp_common.dp_solve import DpSolveInterface
from dp_common.mode import Mode
import sys

"""
Implementation of Coin Change Problems:
    Coin Change Problem 1:
    Problem Stmt: You are given an integer array coins representing coins of different denominations and an integer 
    amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount.
    If that amount of money cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.

    Leet Code Link: https://leetcode.com/problems/coin-change/
    
    Coin Change Problem 2:
    You are given an integer array coins representing coins of different denominations and an integer amount 
    representing a total amount of money. Return the number of combinations that make up that amount. If that amount 
    of money cannot be made up by any combination of the coins, return 0. 
    You may assume that you have an infinite number of each kind of coin.
    
    Leet Code Link: https://leetcode.com/problems/coin-change-2/
"""


class CoinChange(DpSolveInterface):

    def coin_change1(self, coins, amount):
        return self.coin_change1_rec(coins, amount)

    def coin_change1_rec(self, coins, amount):
        if amount < 0:
            return -1

        if amount == 0:
            return 0

        min_val = sys.maxsize
        for i in range(len(coins)):
            l_max = -1
            if coins[i] <= amount:
                l_max = self.coin_change1_rec(coins, amount - coins[i])

            if l_max != -1 and l_max != sys.maxsize:
                min_val = min(l_max, min_val)

        if min_val == sys.maxsize:
            ret_val = -1
        else:
            ret_val = 1 + min_val

        return ret_val

    def coin_change1_memo(self, coins, amount):
        dp = []
        for i in range(amount+1):
            dp.append(-1)

        dp[0] = 0

        return self.coin_change1_memo_rec(coins, amount, dp)

    def coin_change1_memo_rec(self, coins, amount, dp):
        if amount < 0:
            return -1

        if dp[amount] != -1:
            return dp[amount]

        min_val = sys.maxsize
        for i in range(len(coins)):
            l_max = -1
            if coins[i] <= amount:
                l_max = self.coin_change1_memo_rec(coins, amount - coins[i], dp)

            if l_max != -1 and l_max != sys.maxsize:
                min_val = min(l_max, min_val)

        if min_val == sys.maxsize:
            ret_val = -1
        else:
            ret_val = 1 + min_val

        dp[amount] = ret_val
        return dp[amount]

    def coin_change1_tab(self, coins, amount):
        dp = []
        for i in range(amount+1):
            dp.append(-1)

        dp[0] = 0

        for i in range(1, amount+1):
            min_val = sys.maxsize
            for j in range(len(coins)):
                l_max = -1
                if coins[j] <= i:
                    l_max = dp[i - coins[j]]

                if l_max != -1 and l_max != sys.maxsize:
                    min_val = min(l_max, min_val)

            if min_val == sys.maxsize:
                ret_val = -1
            else:
                ret_val = 1 + min_val

            dp[i] = ret_val

        return dp[amount]

    def coin_change2(self, coins, amount):
        dp = [[0] * (amount + 1) for _ in range(len(coins))]

        # Base condition for amount 0
        for i in range(len(coins)):
            dp[i][0] = 1

        # Base condition for top row
        for i in range(amount+1):
            if i % coins[0] == 0:
                dp[0][i] = 1


        print(str(dp))
        for i in range(1, len(coins)):
            for j in range(1, amount+1):
                if j < coins[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]

        print(str(dp))

        return dp[len(coins)-1][amount]




    def solve(self, mode, *args):
        coins = args[0]
        amount = args[1]

        print("Solving coin change problem 1 in mode " + str(mode) + " ...")
        print("Coins: " + str(coins))
        print("Amount: " + str(amount))

        min_coins = -1
        if mode == Mode.RECURSION:
            min_coins = self.coin_change1(coins, amount)
        elif mode == Mode.MEMOIZATION:
            min_coins = self.coin_change1_memo(coins, amount)
        elif mode == Mode.TABULATION:
            min_coins = self.coin_change1_tab(coins, amount)

        no_of_combinations = self.coin_change2(coins, amount)

        print("Min coins needed to gather amount " + str(min_coins))
        print("No of possible combinations to gather amount " + str(no_of_combinations))
