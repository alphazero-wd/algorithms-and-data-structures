// Time complexity: O(n)
const linearSearch = (array, target) => {
  for (let i = 0; i < array.length; i++) {
    if (target === array[i]) return i;
  }
  return -1;
};
