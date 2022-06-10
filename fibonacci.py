def fib(n: int) -> int:
  if n <= 2: return n
  return fib(n - 1) + fib(n - 2)
# Time complexity: O(2^n)
# Space complexity: O(n)

def fib_memo(n: int, memo={}) -> int:
  if n in memo: return memo[n]
  if n <= 2: return 1
  return fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
# Time complexity: O(n)
# Space complexity: O(n)

def fib_dp(n: int) -> int:
  dp = [0] * (n + 1) 
  dp[1] = 1
  for i in range(n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
  return dp[n]
# Time complexity: O(n)
# Space complexity: O(n)