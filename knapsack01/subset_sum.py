from dp_common.mode import Mode
from dp_common.dp_solve import DpSolveInterface

"""
Implementation of Subset Sum problem
    -> Recursive Approach
    -> Memoization Approach
    -> Tabulation Approach

Problem Stmt: Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 

Problem Link: https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

"""

class SubsetSum(DpSolveInterface):

    def subset_sum(self, set, sum):
        return self.subset_sum_rec(set, sum, len(set)-1)

    def subset_sum_rec(self, set, sum, idx):
        if idx < 0 and sum != 0:
            return False

        if sum == 0:
            return True

        if set[idx] > sum:
            return self.subset_sum_rec(set, sum, idx-1)
        else:
            return self.subset_sum_rec(set, sum, idx-1) or self.subset_sum_rec(set, sum-set[idx], idx-1)

    def subset_sum_memo(self, set, sum):
        dp = [[-1] * (sum + 1) for _ in range(len(set))]

        for i in range(len(set)):
            dp[i][0] = 1

        self.subset_sum_memo_rec(set, sum, len(set)-1, dp)
        return True if dp[len(set)-1][sum] == 1 else False

    def subset_sum_memo_rec(self, set, sum, idx, dp):
        if idx < 0 or sum < 0:
            return False

        if dp[idx][sum] != -1:
            return True if dp[idx][sum] == 1 else False

        if set[idx] > sum:
            has_subset = self.subset_sum_memo_rec(set, sum, idx-1, dp)
            dp[idx][sum] = 1 if has_subset else 0
        else:
            exclude = True if self.subset_sum_memo_rec(set, sum, idx-1, dp) == 1 else False
            include = True if self.subset_sum_memo_rec(set, sum-set[idx], idx-1, dp) else False
            has_subset = include or exclude
            dp[idx][sum] = 1 if has_subset else 0

        # print(str(idx) + " " + str(sum) + " " + str(dp[idx][sum]))
        return True if dp[idx][sum] == 1 else False


    def subset_sum_tab(self, set, sum):
        dp = [[-1] * (sum + 1) for _ in range(len(set))]

        for i in range(len(set)):
            dp[i][0] = 1

        for i in range(sum+1):
            dp[0][i] = 0

        dp[0][set[0]] = 1
        dp[0][0] = 1

        # print(str(dp))
        for i in range(1, len(set)):
            for j in range(1, sum+1):
                if set[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    exclude = True if dp[i-1][j] == 1 else False
                    include = True if dp[i-1][j-set[i]] else False
                    has_subset = include or exclude
                    dp[i][j] = 1 if has_subset else 0

        # print(str(dp))
        return True if dp[len(set)-1][sum] == 1 else False



    def solve(self, mode, *args):
        set = args[0]
        sum = args[1]
        has_subset_sum = False

        print("Running subset sum algorithm in mode " + str(mode) + " for the following inputs:")
        print("Set: " + str(set))
        print("Sum: " + str(sum))

        if mode == Mode.RECURSION:
            has_subset_sum = self.subset_sum(set, sum)
            pass
        elif mode == Mode.MEMOIZATION:
            has_subset_sum = self.subset_sum_memo(set, sum)
            pass
        elif mode == Mode.TABULATION:
            has_subset_sum = self.subset_sum_tab(set, sum)
            pass

        print("Has Subset Sum: " + str(has_subset_sum))