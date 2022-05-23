// Time complexity: O(2^n)
// Space complexity: O(n) due to the call stack
const LCSNaive = (text1, text2) => {
  const m = text1.length;
  const n = text2.length;
  if (!m || !n) return 0;
  if (text1[m - 1] === text2[n - 1])
    return 1 + LCSNaive(text1.slice(0, m - 1), text2.slice(0, n - 1));
  else
    return Math.max(
      LCSNaive(text1, text2.slice(0, n - 1)),
      LCSNaive(text1.slice(0, m - 1), text2)
    );
};

// Time complexity: O(mn)
// Space complexity: O(mn)
const LCSDP = (text1, text2) => {
  const m = text1.length;
  const n = text2.length;
  let ans = 0;
  const dp = [...Array(m + 1)].map(() => Array(n + 1).fill(0));
  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      dp[i][j] =
        text1[i - 1] === text2[j - 1]
          ? 1 + dp[i - 1][j - 1]
          : Math.max(dp[i][j - 1], dp[i - 1][j]);
      ans = Math.max(ans, dp[i][j]);
    }
  }
  return ans;
};
