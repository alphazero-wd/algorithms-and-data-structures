// works only on sorted arrays
// time complexity: O(nlog2(n))
const binarySearch = (array, target) => {
  let low = 0,
    high = array.length - 1;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (array[mid] === target) return mid;
    else if (array[mid] > target) high = mid - 1;
    else low = mid + 1;
  }
  return -1;
};
