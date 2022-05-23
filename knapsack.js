// Time complexity: O(2^n)
// Space complexity: O(n)
const knapsackNaive = (weights, values, w, n) => {
  if (w <= 0 || n < 0) return 0;
  if (weights[n] > w) return knapsackNaive(weights, values, w, n - 1);
  return Math.max(
    knapsackNaive(weights, values, w, n - 1),
    values[n] + knapsackNaive(weights, values, w - weights[n], n - 1)
  );
};

// Time complexity: O(n * w) (n = number of items(values), w = weights of the knapsack (w))
// Space complexity: O(n * w)
const knapsackMemoized = (weights, values, w, n, memo = {}) => {
  const key = `${n} ${w}`;
  if (key in memo) return memo[key];
  if (w <= 0 || n < 0) return 0;
  if (weights[n] > w) memo[key] = knapsackNaive(weights, values, w, n - 1);
  memo[key] = Math.max(
    knapsackMemoized(weights, values, w, n - 1, memo),
    values[n] + knapsackMemoized(weights, values, w - weights[n], n - 1, memo)
  );
  return memo[key];
};

// Time complexity: O(nw) (n = number of items(values), w = weights of the knapsack (w))
// Space complexity: O(nw)
const knapsackBottomUp = (weights, values, w, n) => {
  const dp = [...new Array(n + 1)].map(() => new Array(w + 1));
  for (let i = 0; i <= n; i++) {
    for (let j = 0; j <= w; j++) {
      if (i === 0 || j === 0) dp[i][j] = 0;
      else if (weights[i - 1] > j) dp[i][j] = dp[i - 1][j];
      else
        dp[i][j] = Math.max(
          dp[i - 1][j],
          values[i - 1] + dp[i - 1][j - weights[i - 1]]
        );
    }
  }
  return dp[n][w];
};
