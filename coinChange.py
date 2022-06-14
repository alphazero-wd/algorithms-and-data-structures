from typing import List


class Solution1:
    def coin_change(self, coins: List[int], target: int) -> int:
        n = len(coins)

        def count_coins(i: int, target: int) -> int:
            if target == 0:
                return 1
            if target < 0 or (i < 0 and target > 0):
                return 0
            return count_coins(i - 1, target) + count_coins(i, target - coins[i])
        return count_coins(n - 1, target)


class Solution2:
    def coin_change(self, coins: List[int], target: int) -> int:
        n = len(coins)
        dp = [[None for _ in range(n)] for _ in range(target + 1)]

        for i in range(n):
            dp[0][i] = 1

        for i in range(1, target + 1):
            for j in range(n):
                # count solutions including the current coin
                temp1 = dp[i - coins[j]][j] if i - coins[j] >= 0 else 0

                # count solutions including the current coin
                temp2 = dp[i][j - 1] if j >= 1 else 0

                dp[i][j] = temp1 + temp2

        return dp[target][n - 1]
