from dp_common.mode import Mode
from dp_common.dp_solve import DpSolveInterface

"""
Implementation of 0/1 Knapsack problem
    -> Recursive Approach
    -> Memoization Approach
    -> Tabulation Approach
    
Problem Stmt: Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
               In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. 
               Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.
               You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
               
Problem Link: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
    
"""


class Knapsack01(DpSolveInterface):
    def knapsack01(self, weights, values, max_weight):
        return self.knapsack01_rec(weights, values, max_weight, len(weights)-1)

    def knapsack01_rec(self, weights, values, curr_rem_weight, idx):
        if curr_rem_weight <= 0 or idx < 0:
            return 0

        ret_val = 0
        # If current object weight is greater than remaining weight, we cannot include it
        if weights[idx] > curr_rem_weight:
            ret_val = self.knapsack01_rec(weights, values, curr_rem_weight, idx-1)
        else:
            ret_val = max(self.knapsack01_rec(weights, values, curr_rem_weight, idx-1), self.knapsack01_rec(weights, values, curr_rem_weight-weights[idx], idx-1) + values[idx])

        # print(str(idx) + " " + str(curr_rem_weight) + " " + str(ret_val))
        return ret_val

    def knapsack01_memo(self, weights, values, max_weight):
        dp = [[-1] * (max_weight + 1)]*(len(weights))
        self.knapsack01_memo_rec(weights, values, max_weight, len(weights)-1,dp)
        # print(str(dp))
        return dp[len(weights)-1][max_weight]

    def knapsack01_memo_rec(self, weights, values, curr_rem_weight, idx, dp):
        if curr_rem_weight == 0 or idx == 0:
            return 0

        if dp[idx][curr_rem_weight] != -1:
            return dp[idx][curr_rem_weight]

        # If current object weight is greater than remaining weight, we cannot include it
        if weights[idx-1] > curr_rem_weight:
            dp[idx][curr_rem_weight] = self.knapsack01_memo_rec(weights, values, curr_rem_weight, idx-1,dp)
        else:
            dp[idx][curr_rem_weight] = max(self.knapsack01_memo_rec(weights, values, curr_rem_weight, idx-1, dp),
                                           self.knapsack01_memo_rec(weights, values, curr_rem_weight-weights[idx], idx-1, dp) + values[idx])
        # print(str(idx) + " " + str(curr_rem_weight) + " " + str(dp[idx][curr_rem_weight]))
        return dp[idx][curr_rem_weight]

    def knapsack01_tab(self, weights, values, max_weight):
        dp = [[-1] * (max_weight + 1) for _ in range(len(weights))]

        # print(str(dp))
        # Base condition
        for i in range(max_weight+1):
            dp[0][i] = 0

        # print(str(dp))
        for i in range(1, len(weights), 1):
            for j in range(0, max_weight+1, 1):
                if weights[i] > j:
                    dp[i][j] = dp[i-1][j]
                    # print("Setting to " + str(dp[i][j]))
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i])
                    # print("Setting to " + str(dp[i][j]))

        # print(str(dp))

        return dp[len(weights)-1][max_weight]




    def solve(self, mode, *args):
        weights = []
        values = []

        weights = args[0]
        values = args[1]
        max_weight = int(args[2])
        max_value = 0

        print("Running knapsack01 algorithm in " + str(mode) + " for the following inputs:")
        print("Weight Array: " + str(weights))
        print("Value  Array: " + str(values))
        print("Max weight: " + str(max_weight))

        if mode == Mode.RECURSION:
            max_value = self.knapsack01(weights, values, max_weight)
        elif mode == Mode.MEMOIZATION:
            max_value = self.knapsack01_memo(weights, values, max_weight)
        elif mode == Mode.TABULATION:
            max_value = self.knapsack01_tab(weights, values, max_weight)

        print("Max value of knapsack: %d" % max_value)