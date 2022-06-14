class Solution1:
    def edit_distance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m == 0:
            return n
        if n == 0:
            return m
        if word1[m - 1] == word2[n - 1]:
            return self.edit_distance(word1[:m - 1], word2[:n - 1])
        else:
            return 1 + min(
                self.edit_distance(word1[:m - 1], word2),
                self.edit_distance(word1, word2[:n - 1]),
                self.edit_distance(word1[:m - 1], word2[:n - 1])
            )


class Solution2:
    def edit_distance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[None for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i]
                                       [j - 1], dp[i - 1][j - 1])
        return dp[m][n]
