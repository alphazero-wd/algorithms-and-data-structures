// Time complexity: O(nlog2(n)) average, O(n^2) worst case
// Space complexity: O(log2(n))
const quickSort = (array) => {
  return quickSortHelper(array, 0, array.length - 1);
};

const quickSortHelper = (array, low, high) => {
  const index = partition(array, low, high);
  if (low < index - 1) quickSortHelper(array, low, index - 1);

  if (index < high) quickSortHelper(array, index, high);
  return array;
};

const partition = (array, low, high) => {
  const pivot = array[Math.floor((low + high) / 2)];
  while (low <= high) {
    while (array[low] < pivot) low++;
    while (array[high] > pivot) high--;
    if (low <= high) {
      const temp = array[low];
      array[low] = array[high];
      array[high] = temp;
      low++;
      high--;
    }
  }
  return low;
};
