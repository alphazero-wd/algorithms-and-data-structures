def fib(n):
  if n <= 2: return n
  return fib(n - 1) + fib(n - 2)
# Time complexity: O(2^n)
# Space complexity: O(n)