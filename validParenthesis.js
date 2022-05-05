const Stack = require("./stack");

// Time complexity: O(n)
// Space complexity: O(n) (stack)
const isValidParenthesis = (s) => {
  const stack = new Stack();
  const validPairs = {
    ")": "(",
    "]": "[",
    "}": "{",
  };

  for (let char of s) {
    if (!stack.isEmpty() && char in validPairs) {
      if (stack.peek() !== validPairs[char]) return false;
      stack.pop();
    } else {
      stack.push(char);
    }
  }
  return stack.isEmpty();
};

console.log(isValidParenthesis("((()")); // false;
console.log(isValidParenthesis("((((")); // false;
console.log(isValidParenthesis("()()")); // true;
