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

const coinChangeBottomUp = (coins, amount) => {
  const dp = [...Array(amount)].map(() => 0);
  dp[0] = 1;
  for (let i = 1; i <= coins.length; i++) {
    for (let coin of coins) {
      if (i - coin >= 0) dp[i] += dp[i - coin];
    }
  }
  return dp[amount - 1];
};
