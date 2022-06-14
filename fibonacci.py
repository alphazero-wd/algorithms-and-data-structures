class Solution1:
    def fib(self, n: int) -> int:
        if n <= 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


class Solution2:
    def fib(self, n: int, memo={}) -> int:
        if n in memo:
            return memo[n]
        if n <= 2:
            return 1
        return self.fib(n - 1, memo) + self.fib(n - 2, memo)


class Solution3:
    def fib(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
