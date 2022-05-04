const select = (array, left, right, k) => {
  if (left == right)
    // If the array contains only one element,
    return array[left]; // return that element
  const pivotIndex = partition(array, left, right);
  // The pivot is in its final sorted position
  if (k == pivotIndex) return array[k];
  else if (k < pivotIndex) return select(array, left, pivotIndex - 1, k);
  else return select(array, pivotIndex + 1, right, k);
};
const partition = (array, left, right) => {
  const pivotIndex = Math.floor((left + right) / 2);
  const pivot = array[pivotIndex];
  swap(array, pivotIndex, right);
  let storeIndex = left;
  for (let i = left; i <= right; i++) {
    if (array[i] < pivot) {
      swap(array, i, storeIndex);
      storeIndex++;
    }
  }
  swap(array, right, storeIndex);
  return storeIndex;
};

const swap = (array, i, j) => {
  const temp = array[i];
  array[i] = array[j];
  array[j] = temp;
};

const findKthLargest = (array, k) => {
  k = array.length - k;
  return select(array, 0, array.length - 1, k);
};
