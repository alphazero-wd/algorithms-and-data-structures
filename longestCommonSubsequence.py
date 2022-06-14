class Solution1:
    def LCS(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        if m == 0 or n == 0:
            return 0
        if text1[m - 1] == text2[n - 1]:
            return 1 + self.LCS(text1[:m - 1], text2[:n - 1])
        else:
            return max(
                self.LCS(text1[:m - 1], text2),
                self.LCS(text1, text2[:n - 1])
            )


class Solution2:
    def LCS(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[None for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )
        return dp[m][n]
