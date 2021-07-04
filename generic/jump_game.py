from dp_common.dp_solve import DpSolveInterface
from dp_common.mode import Mode
import sys

"""
Implementation of Jump Game Problems:
Jump Game 1:
    Problem Stmt: Given an array of non-negative integers nums, you are initially positioned at the first index of the array. 
                   Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index.
    
    Leet Code Link: https://leetcode.com/problems/jump-game/
    
Jump Game 2:
    Problem Stmt: Given an array of non-negative integers nums, you are initially positioned at the first index of the array. 
                  Each element in the array represents your maximum jump length at that position.
                  Your goal is to reach the last index in the minimum number of jumps. You can assume that you can always reach the last index.
    
    Leet Code Link: https://leetcode.com/problems/jump-game-ii/
"""


class JumpGame(DpSolveInterface):

    def jump_game1(self, nums):
        return self.jump_game1_rec(nums, 0)

    def jump_game1_rec(self, nums, i):
        if i >= len(nums) - 1:
            return True

        can_reach = False;
        for j in range(1, nums[i] + 1):
            can_reach = can_reach or self.jump_game1_rec(nums, i+j)

        return can_reach

    def jump_game1_memo(self, nums):
        n = len(nums)
        dp = []

        for i in range(0, n):
            dp.append(-1)

        dp[n-1] = 1

        self.jump_game1_memo_rec(nums, 0, dp)
        #print("Dp Array: " + str(dp))

        return True if dp[0] == 1 else False

    def jump_game1_memo_rec(self, nums, i, dp):
        if i >= len(nums) - 1:
            return True

        if dp[i] != -1:
            return True if dp[i] == 1 else False

        can_reach = False;
        for j in range(1, nums[i] + 1):
            can_reach = can_reach or self.jump_game1_memo_rec(nums, i + j, dp)

        if can_reach:
            dp[i] = 1
        else:
            dp[i] = 0

        return can_reach

    def jump_game1_tab(self, nums):
        n = len(nums)
        last_idx = 0

        for i in range(0, n-1):
            last_idx = max(last_idx, i + nums[i])
            if last_idx >= n-1:
                return True
            #print("Last Idx: " + str(last_idx))

        #print("Last Idx: " + str(last_idx) + str(n-1))
        if last_idx >= n - 1:
            return True
        else:
            return False

    def jump_game2(self, nums):
        return self.jump_game2_rec(nums, 0)

    def jump_game2_rec(self, nums, idx):
        if idx >= len(nums) - 1:
            return 0

        min_val = sys.maxsize -1
        for i in range(idx+1, idx+nums[idx]+1):
            if i > len(nums) - 1:
                continue

            min_val = min(min_val, self.jump_game2_rec(nums, i))

        return min_val + 1

    def jump_game2_memo(self, nums):
        n = len(nums)
        dp = []

        for i in range(0, n):
            dp.append(-1)

        dp[n-1] = 0
        self.jump_game2_memo_rec(nums, 0, dp)

        return dp[0]

    def jump_game2_memo_rec(self, nums, idx, dp):
        if idx >= len(nums) - 1:
            return 0

        if dp[idx] != -1:
            return dp[idx]

        min_val = sys.maxsize -1
        for i in range(idx+1, idx+nums[idx]+1):
            if i > len(nums) - 1:
                continue

            min_val = min(min_val, self.jump_game2_rec(nums, i))

        dp[idx] = min_val + 1
        return dp[idx]

    def jump_game2_tab(self, nums):
        n = len(nums)
        if n == 1:
            return 0

        n = len(nums)
        dp = []

        for i in range(0, n):
            dp.append(-1)

        dp[n - 1] = 0
        jumps = 0

        for i in range(n-2,-1,-1):
            min_val = sys.maxsize-1
            for j in range(1, nums[i]+1):
                if i + j > n - 1:
                    continue

                min_val = min(min_val, dp[i+j])

            dp[i] = min_val + 1

        return dp[0]

    def solve(self, mode, *args):
        args = list(args)

        try:
            arr = args[0]
            ans_jump_game1 = False
            min_moves = 0

            print("Jump Game 1 with array: " + str(arr) + " and run mode: " + str(mode))
            if mode == Mode.RECURSION:
                ans_jump_game1 = self.jump_game1(arr)
                min_moves = self.jump_game2(arr)
            elif mode == Mode.MEMOIZATION:
                ans_jump_game1 = self.jump_game1_memo(arr)
                min_moves = self.jump_game2_memo(arr)
            elif mode == Mode.TABULATION:
                ans_jump_game1 = self.jump_game1_tab(arr)
                min_moves = self.jump_game2_tab(arr)

            print("Answer Jump Game 1: " + str(ans_jump_game1))
            print("Answer Jump Game 2: " + str(min_moves))
        except Exception as e:
            print("Exiting with exception " + str(e))
            raise e