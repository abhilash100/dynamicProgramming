from dp_common.mode import Mode
from dp_common.dp_solve import DpSolveInterface

"""
Implementation of Equal Sum Partition problem
    -> Recursive Approach
    -> Memoization Approach
    -> Tabulation Approach

Problem Stmt: Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Problem Link: https://leetcode.com/problems/partition-equal-subset-sum/

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100

"""


class EqualSumPartition(DpSolveInterface):
    def equal_sum_partition(self, nums):
        return self.equal_sum_partition_rec(nums, len(nums)-1, 0)

    def equal_sum_partition_rec(self, nums, idx, sum):
        if idx < 0:
            if sum == 0:
                return True
            else:
                return False

        can_partition = False
        exclude = self.equal_sum_partition_rec(nums, idx-1, sum-nums[idx])
        include = self.equal_sum_partition_rec(nums, idx-1, sum+nums[idx])
        return can_partition or include or exclude

    def equal_sum_partition_memo(self, nums):
        dp = [[-1] * 400002] * (len(nums))

        for i in range(len(nums)):
            for j in range(400002):
                dp[i][j] = -1

        return self.equal_sum_partition_memo_rec(nums, len(nums)-1, 0, dp)

    def equal_sum_partition_memo_rec(self, nums, idx, sum, dp):
        if idx < 0:
            if sum == 0:
                return True
            else:
                return False

        if dp[idx][sum + 20001] != -1:
            return True if dp[idx][sum + 20001] == 1 else False

        exclude = self.equal_sum_partition_memo_rec(nums, idx - 1, sum - nums[idx], dp);

        include = self.equal_sum_partition_memo_rec(nums, idx - 1, sum + nums[idx], dp);

        ret_val = False or include or exclude
        dp[idx][sum + 20001] = 1 if ret_val else 0

        return ret_val

    def solve(self, mode, *args):
        nums = args[0]
        is_possible = False

        print("Equal sum partition for nums array : " + str(nums) + " solved in mode " + str(mode))
        if mode == Mode.RECURSION:
            is_possible = self.equal_sum_partition(nums)
        elif mode == Mode.MEMOIZATION:
            is_possible = self.equal_sum_partition_memo(nums)
        elif mode == Mode.TABULATION:
            raise Exception("Equal sum partition hasn't yet been implemented using tabulation")

        print("Equal sum partition is possible : " + str(is_possible))
"""
    TODO: Complete Implementation
    def equal_sum_partition_tab(self, nums):
        dp = [[-1] * 400003] * (len(nums)+1)

        for i in range(len(nums)+1):
            for j in range(400003):
                dp[i][j] = -1
                if i == 0 or j == 0:
                    dp[i][j] = 0

        for i in range(1, len(nums)+1):
            for j in range(1, 20002):
                print(str(j+nums[i-1]))
                exclude = dp[i-1][j-nums[i-1]]
                include = dp[i-1][j+nums[i-1]]
                exclude_b = True if exclude == 1 else 0
                include_b = True if include == 1 else 0

                is_possible = False or include_b or exclude_b
                dp[i][j] = 1 if is_possible else 0

        return dp[len(nums)-1][20002]
"""


