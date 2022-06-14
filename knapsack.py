from typing import Dict, List, Tuple


class Solution1:
    def knapsack(self, items: List[Tuple[int]], w: int) -> int:
        n = len(items)

        def recurse(w: int, i: int) -> int:
            if i < 0 or w <= 0:
                return 0
            if items[i][1] > w:
                return recurse(w, i - 1)
            else:
                return max(
                    recurse(w, i - 1),
                    items[i][0] + recurse(w - items[i][1], i - 1)
                )
        return recurse(w, n - 1)


class Solution2:
    def knapsack(self, items: List[Tuple[int]], w: int) -> int:
        memo: Dict[Tuple, int] = {}
        n = len(items)

        def memoize(w: int, i: int) -> int:
            k = (i, w)
            if k in memo:
                return memo[k]
            if i < 0 or w <= 0:
                return 0
            if items[i][1] > w:
                memo[k] = memoize(w, i - 1)
            else:
                memo[k] = max(
                    memoize(w, i - 1),
                    items[i][0] + memoize(w - items[i][1], i - 1)
                )
            return memo[k]
        return memoize(w, n - 1)


class Solution3:
    def knapsack(self, items: List[Tuple[int]], w: int) -> int:
        n = len(items)
        dp = [[None for _ in range(w + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(w + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif items[i - 1][1] > w:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        items[i - 1][0] + dp[i - 1][j - items[i - 1][1]]
                    )
        return dp[n][w]
