from typing import List

def coin_change(coins: List[int], target: int) -> int:
  n = len(coins)
  def count_coins(i: int, target: int) -> int:
    if target == 0: return 1
    if target < 0 or (i < 0 and target > 0): return 0
    return count_coins(i - 1, target) + count_coins(i, target - coins[i])
  return count_coins(n - 1, target)

def coin_change_dp(coins: List[int], target: int) -> int:
  dp = [0] * (target + 1)
  dp[0] = 1
  for coin in coins:
    for i in range(target + 1):
      if i - coin >= 0:
        dp[i] += dp[i - coin]
  return dp[target]
