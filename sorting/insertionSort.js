// Time complexity: O(n^2)
// Space complexity: O(1)
const insertionSort = (array) => {
  let i, j;
  for (i = 0; i < array.length; i++) {
    // store the current value because it may shift later
    const value = array[i];

    // Whenever the value in the sorted section is greater than the value
    // in the unsorted section, shift all items in the sorted section
    // over by one. This creates space in which to insert the value.
    for (j = i - 1; j > -1 && array[j] > value; j--) {
      array[j + 1] = array[j];
    }
    array[j + 1] = value;
  }
  return array;
};
