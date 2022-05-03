const swap = (array, i, j) => {
  const temp = array[i];
  array[i] = array[j];
  array[j] = temp;
};

// Time complexity: O(n^2)
// Space complexity: O(1)
const selectionSort = (array) => {
  for (let i = 0; i < array.length; i++) {
    let minIndex = i;
    for (let j = i + 1; j < array.length; j++) {
      if (array[j] < array[minIndex]) minIndex = j;
    }
    if (i !== minIndex) swap(array, i, minIndex);
  }
  return array;
};
