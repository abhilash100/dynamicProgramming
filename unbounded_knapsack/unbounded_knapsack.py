from dp_common.mode import Mode
from dp_common.dp_solve import DpSolveInterface
from sys import maxsize

"""
Implementation of Unbounded Knapsack Problem
    -> Recursive Approach
    -> Memoization Approach
    -> Tabulation Approach

Problem Stmt: 
    Given a knapsack weight W and a set of n items with certain value vli and weight wti, we need to calculate 
    the maximum amount that could make up this quantity exactly. This is different from classical Knapsack problem, 
    here we are allowed to use unlimited number of instances of an item.


Problem Link: https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/

"""

class UnboundedKnapsack(DpSolveInterface):
    def unbounded_knapsack(self, max_weight, wti, vli):
        return self.unbounded_knapsack_rec(max_weight, wti, vli)

    def unbounded_knapsack_rec(self, max_weight, wti, vli):
        if max_weight < 0:
            return 0

        max_value = 0
        for i in range(len(wti)):
            if wti[i] <= max_weight:
                rest_of_knap_sack = self.unbounded_knapsack_rec(max_weight-wti[i], wti, vli)
                max_value = max(max_value, vli[i] + rest_of_knap_sack)

        # print(str(max_weight) + " : " + str(max_value))
        return max_value

    def unbounded_knapsack_memo(self, max_weight, wti, vli):
        dp = []
        for i in range(max_weight+1):
            dp.append(-1)

        return self.unbounded_knapsack_memo_rec(max_weight, wti, vli, dp)

    def unbounded_knapsack_memo_rec(self, max_weight, wti, vli, dp):
        if max_weight < 0:
            return 0

        if dp[max_weight] != -1:
            return dp[max_weight]

        max_value = 0
        for i in range(len(wti)):
            if wti[i] <= max_weight:
                rest_of_knap_sack = self.unbounded_knapsack_memo_rec(max_weight-wti[i], wti, vli, dp)
                max_value = max(max_value, vli[i] + rest_of_knap_sack)

        dp[max_weight] = max_value
        return dp[max_weight]

    def unbounded_knapsack_tab(self, max_weight, wti, vli):
        dp = []
        for i in range(max_weight+1):
            dp.append(-1)

        dp[0] = 0

        for i in range(1, max_weight+1):
            max_value = 0
            for j in range(len(wti)):
                if i - wti[j] >= 0:
                    max_value= max(max_value, dp[i-wti[j]] + vli[j])

            dp[i] = max_value

        return dp[max_weight]

    def solve(self, mode, *args):
        max_weight = args[0]
        wti = args[1]
        vli = args[2]

        max_value = -1
        print("Unbounded knapsack problem in mode " + str(mode) + " with: ")
        print("Max Knapsack weight: " + str(max_weight))
        print("Weight array: " + str(wti))
        print("Value array: " + str(vli))

        if mode == Mode.RECURSION:
            max_value = self.unbounded_knapsack(max_weight, wti, vli)
        elif mode == Mode.MEMOIZATION:
            max_value = self.unbounded_knapsack_memo(max_weight, wti, vli)
        elif mode == Mode.TABULATION:
            max_value = self.unbounded_knapsack_tab(max_weight, wti, vli)
        print("Max value: " + str(max_value))




