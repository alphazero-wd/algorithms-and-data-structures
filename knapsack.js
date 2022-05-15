// Time complexity: O(2^n)
// Space complexity: O(n)
const knapsackNaive = (weights, values, w, n) => {
  if (n < 0 || w <= 0) return 0;
  if (weights[n] > w) return knapsackNaive(weights, values, w, n - 1);
  return Math.max(
    knapsackNaive(weights, values, w, n - 1),
    values[n] + knapsackNaive(weights, values, w - weights[n], n - 1)
  );
};

// Time complexity: O(n * w) (n = number of items(values), w = weights of the knapsack (w))
// Space complexity: O(n * w)
const knapsackMemoized = (weights, values, w, n, memo = {}) => {
  if (memo[`${n},${w}`]) return memo[`${n},${w}`];
  if (n < 0 || w <= 0) return 0;
  if (weights[n] > w) return knapsackNaive(weights, values, w, n - 1, memo);
  memo[`${n},${w}`] = Math.max(
    knapsackMemoized(weights, values, w, n - 1, memo),
    values[n] + knapsackMemoized(weights, values, w - weights[n], n - 1, memo)
  );
  return memo[`${n},${w}`];
};

// Time complexity: O(n * w) (n = number of items(values), w = weights of the knapsack (w))
// Space complexity: O(n * w)
const knapsackBottomUp = (weights, values, w, n) => {
  let result = 0;
  if (w <= 0 || n <= 0) return result;
  const dp = [...new Array(n + 1)].map(() => new Array(w + 1));

  for (let i = 0; i <= n; i++) {
    for (let j = 0; j <= w; j++) {
      // if either the weight or the number of items is 0 then the max value = 0
      if (i === 0 || j === 0) dp[i][j] = 0;
      // if the current weight > max weight, skip it
      else if (weights[i - 1] > j) dp[i][j] = dp[i - 1][j];
      // else take the max between what's in the knapsack and either include or exclude the value going to be put in
      else
        dp[i][j] = Math.max(
          dp[i - 1][j],
          values[i - 1] + dp[i - 1][j - weights[i - 1]]
        );
    }
  }
  return dp[n][w];
};

const weights = [1, 2, 4, 2, 5],
  values = [5, 3, 5, 3, 2],
  w = 10;

console.log(bottomUp(weights, values, w, weights.length));
