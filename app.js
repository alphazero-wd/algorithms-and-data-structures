// iterative
const fibIterative = (n) => {
  if (n === 0) return 0;
  if (n === 1) return 1;
  let sum = 0,
    lastOne = 1,
    lastTwo = 0;
  for (let i = 2; i <= n; i++) {
    sum = lastOne + lastTwo;
    lastTwo = lastOne;
    lastOne = sum;
  }
  return sum;
};

// recursive
const fibRecursive = (n) => {
  if (n === 0) return 0;
  if (n === 1) return 1;

  return fibRecursive(n - 1) + fibRecursive(n - 2);
};
