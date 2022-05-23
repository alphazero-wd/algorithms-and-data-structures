// Time complexity: O(n^m) (n is number of coins, m is the amount required)
// Space complexity: O(n)
const coinChange = (coins, amount) => {
  const coinChangeUtils = (coins, n, amount) => {
    if (amount === 0) return 1;
    if (amount < 0 || (n <= 0 && amount >= 1)) return 0;
    return (
      coinChangeUtils(coins, n - 1, amount) +
      coinChangeUtils(coins, n, amount - coins[n - 1])
    );
  };
  return coinChangeUtils(coins, coins.length, amount);
};

// Time complexity: O(nm)
// Space complexity: O(m)
const coinChangeBottomUp = (coins, amount) => {
  const dp = [...Array(amount + 1)].map(() => 0);
  dp[0] = 1;
  for (let coin of coins) {
    for (let i = 1; i <= amount; i++) {
      if (i - coin >= 0) dp[i] += dp[i - coin];
    }
  }
  return dp[amount];
};
