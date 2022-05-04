// Time complexity: O(nlog(n))
// Space complexity: O(n)
const mergeSort = (array) => {
  if (array.length < 2) return array;
  const midpoint = Math.floor(array.length / 2);
  const leftArray = array.slice(0, midpoint);
  const rightArray = array.slice(midpoint);
  return merge(mergeSort(leftArray), mergeSort(rightArray));
};

const merge = (leftArray, rightArray) => {
  const result = [];
  let left = 0,
    right = 0;
  while (left < leftArray.length && right < rightArray.length) {
    if (leftArray[left] < rightArray[right]) {
      result.push(leftArray[left++]);
    } else {
      result.push(rightArray[right++]);
    }
  }

  const leftRemains = leftArray.slice(left),
    rightRemains = rightArray.slice(right);
  return result.concat(leftRemains).concat(rightRemains);
};
