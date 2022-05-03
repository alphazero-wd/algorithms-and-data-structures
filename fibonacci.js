// iterative
// Time complexity: O(n)
// Space complexity: O(1)
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
// Time complexity: O(2^n)
// Space complexity: O(n) because of the call stack
const fibRecursive = (n) => {
  if (n === 0) return 0;
  if (n === 1) return 1;

  return fibRecursive(n - 1) + fibRecursive(n - 2);
};

// tail recursive
// Time complexity: O(n)
// Space complexity: O(n) because of the call stack
const fibTailRecursive = (n, lastTwo = 0, lastOne = 1) => {
  if (n === 0) return lastTwo;
  if (n === 0) return lastOne;
  return fibTailRecursive(n - 1, lastOne, lastTwo + lastOne);
};
