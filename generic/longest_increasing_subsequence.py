from dp_common.dp_solve import DpSolveInterface
from dp_common.mode import Mode
import sys

"""
Implementation of Longest Increasing Subsequence:
    Problem Stmt: Given an integer array nums, return the length of the longest strictly increasing subsequence.

    Leet Code Link: https://leetcode.com/problems/longest-increasing-subsequence/
"""


class LongestIncreasingSubsequence(DpSolveInterface):
    def longest_increasing_subsequence_tab(self, nums):
        dp = []
        for i in range(len(nums)):
            dp.append(-1)

        dp[0] = 1

        for i in range(1, len(nums)):
            max_val = -1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    max_val = max(max_val, dp[j])

            if max_val == -1:
                dp[i] = 1
            else:
                dp[i] = 1 + max_val

        lis = dp[0]
        for i in range(len(nums)):
            if dp[i] > lis:
                lis = dp[i]

        return lis

    def longest_increasing_subsequence_memo(self, nums):
        dp = []
        for i in range(len(nums)):
            dp.append(-1)

        dp[0] = 1
        #self.longest_increasing_subsequence_memo_rec(nums, len(nums)-1, dp)

        lis = dp[0]
        for i in range(len(nums)):
            self.longest_increasing_subsequence_memo_rec(nums, i, dp)
            if dp[i] > lis:
                lis = dp[i]

        #print(str(dp))
        return lis

    def longest_increasing_subsequence_memo_rec(self, nums, idx, dp):
        if idx < 0:
            return 0

        if dp[idx] != -1:
            return dp[idx]

        max_val = -1
        for i in range(0, idx):
            if nums[i] < nums[idx]:
                max_val = max(max_val, self.longest_increasing_subsequence_memo_rec(nums, i, dp))

        if max_val == -1:
            dp[idx] = 1
        else:
            dp[idx] = max_val + 1

        return dp[idx]

    def solve(self, mode, *args):
        nums = args[0]

        print("Solving Longest increasing subsequence problem in mode " + str(mode))
        print("Nums array: " + str(nums))

        max_lis = -1
        if mode == Mode.RECURSION:
            max_lis = self.longest_increasing_subsequence_memo(nums)
        elif mode == Mode.MEMOIZATION:
            max_lis = self.longest_increasing_subsequence_memo(nums)
        elif mode == Mode.TABULATION:
            max_lis = self.longest_increasing_subsequence_tab(nums)

        print("Length of longest increasing subsequence : " + str(max_lis))