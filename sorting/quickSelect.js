const findKthLargest = (nums, k) => {
  return quickSelect(nums, 0, nums.length - 1, nums.length - k);
};
const quickSelect = (nums, left, right, k) => {
  const pivot = Math.floor((left + right) / 2);
  if (pivot === k - 1) return nums[k];
  else if (pivot > k - 1) return quickSelect(nums, left, pivot - 1, k);
  else return quickSelect(nums, pivot + 1, right, k);
};

const array = [3, 2, 1, 5, 6, 4];
const k = 2;
console.time("method 1");
console.log("Method 1: ", array.sort((a, b) => a - b)[array.length - k]);
console.timeEnd("method 1");

console.time("method 2");
console.log("Method 2: ", findKthLargest(array, k));
console.timeEnd("method 2");
