from dp_common.mode import Mode
from dp_common.dp_solve import DpSolveInterface

""""
Implementation of Fibonacci Algorithm
    -> Implement Using Recursion only
    -> Implement using Memoization
    -> Implement Using Tabulation
"""


class Fibonacci(DpSolveInterface):
    def fibonacci(self, n):
        return self.fibonacci_rec(n)

    def fibonacci_rec(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.fibonacci_rec(n - 1) + self.fibonacci_rec(n - 2)

    def fibonacci_memo(self, n):
        dp = []
        for i in range(0, n+1):
            dp.append(-1)

        dp[0] = 0
        dp[1] = 1

        if n == 1 or n == 2:
            return dp[n-1]

        return self.fibonacci_rec_memo(n, dp)

    def fibonacci_rec_memo(self, n, dp):
        if dp[n-1] == -1:
            dp[n-1] = self.fibonacci_rec_memo(n-1, dp) + self.fibonacci_rec_memo(n-2, dp)
        return dp[n-1]

    def fibonacci_tab(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1

        ans = 0
        prev = 0
        curr = 1

        for i in range(2, n):
            ans = prev + curr
            prev = curr
            curr = ans

        return ans

    def solve(self, mode, *args):
        args = list(args)

        try:
            n = int(args[0])
            ans = -1

            print("Running fibonacci calculation for n=%d using %s" % (n, str(mode)))
            if mode == Mode.RECURSION:
                ans = self.fibonacci(n)
            elif mode == Mode.MEMOIZATION:
                ans = self.fibonacci_memo(n)
            elif mode == Mode.TABULATION:
                ans = self.fibonacci_tab(n)

            print("Answer: %s" % str(ans))
        except Exception as e:
            print("Exiting with exception " + str(e))
            raise e



