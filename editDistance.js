// Time complexity: O(3^n) (n is the length of text1)
// Space complexity: O(n)
const editDistanceNaive = (text1, text2) => {
  const m = text1.length;
  const n = text2.length;
  if (m === 0) return n;
  if (n === 0) return m;

  if (text1[m - 1] === text2[n - 1])
    return editDistanceNaive(text1.slice(0, m - 1), text2.slice(0, n - 1));
  return (
    1 +
    Math.min(
      // insert
      editDistanceNaive(text1, text2.slice(0, n - 1)),
      // remove
      editDistanceNaive(text1.slice(0, m - 1), text2),
      // replace
      editDistanceNaive(text1.slice(0, m - 1), text2.slice(0, n - 1))
    )
  );
};

const editDistanceDP = (text1, text2) => {
  const m = text1.length;
  const n = text2.length;
  const dp = [...Array(m + 1)].map(() => Array(n + 1).fill(0));
  for (let i = 0; i <= m; i++) {
    for (let j = 0; j <= n; j++) {
      if (i === 0) dp[i][j] = j;
      else if (j === 0) dp[i][j] = i;
      else
        dp[i][j] =
          text1[i - 1] === text2[j - 1]
            ? dp[i - 1][j - 1]
            : 1 + Math.min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]);
    }
  }
  return dp[m][n];
};
