from dp_common.mode import Mode
from dp_common.dp_solve import DpSolveInterface

"""
Implementation of Target Sum problem
    -> Recursive Approach
    -> Memoization Approach

Problem Stmt: You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Problem Link: https://leetcode.com/problems/target-sum/

"""


class TargetSum(DpSolveInterface):
    def target_sum(self, nums, target):
        return self.target_sum_rec(nums, target, 0)

    def target_sum_memo(self, nums, target):
        dp = []
        for r in range(20001):
            dp.append([-1 for c in range(len(nums))])

        return self.target_sum_memo_rec(nums, target, 0, dp)

#    def target_sum_tab(self, nums, target):
#        dp = []
#        for r in range(20001):
#            dp.append([-1 for c in range(len(nums)+1)])
#
#        # base condition
#        for r in range(20001):
#            dp[r][0] = 0
#
#        dp[10000][0] = 1
#
#        for r in range(20001, -1, -1):
#            for c in range(len(nums)-1, -1, -1):
#                dp[r][c] = dp[r+nums[c]][c+1] + dp[r-nums[c]][c+1]
#
#        return dp[10000+target][0]

    def target_sum_memo_rec(self, nums, target, idx, dp):
        # base case
        if idx >= len(nums):
            if target == 0:
                return 1
            else:
                return 0

        if dp[10000+target][idx] != -1:
            return dp[10000+target][idx]

        # actual
        # include
        include = self.target_sum_memo_rec(nums, target+nums[idx], idx+1, dp)

        # exclude
        exclude = self.target_sum_memo_rec(nums, target-nums[idx], idx+1, dp)

        dp[10000+target][idx] = include + exclude
        # print(str(target) + " " + str(idx) + str(include + exclude))
        return dp[10000+target][idx]

    def target_sum_rec(self, nums, target, idx):
        # base case
        if idx >= len(nums):
            if target == 0:
                return 1
            else:
                return 0

        # actual
        # include
        include = self.target_sum_rec(nums, target + nums[idx], idx + 1)
        # exclude
        exclude = self.target_sum_rec(nums, target - nums[idx], idx + 1)

        return include + exclude

    def solve(self, mode, *args):
        nums = args[0]
        target = args[1]
        count = 0

        print("Running target sum algorithm in mode " + str(mode))
        print("Nums: " + str(nums))
        print("Target: " + str(target))

        if mode == Mode.RECURSION:
            count = self.target_sum(nums, target)
        elif mode == Mode.MEMOIZATION:
            count = self.target_sum_memo(nums, target)
        elif mode == Mode.TABULATION:
            raise Exception("Target sum algorithm hasn't yet been implemented using tabulation")

        print("Count : " + str(count))


