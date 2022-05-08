// Time complexity: O(n^2)
// Space complexity: O(n)
const deleteDuplicates = (sll) => {
  const duplicates = [];
  let prev = null;
  let currentHead = sll.head;
  while (currentHead) {
    if (duplicates.indexOf(currentHead.data) >= 0) {
      prev.next = currentHead.next;
    } else {
      duplicates.push(currentHead.data);
      prev = currentHead;
    }
    currentHead = currentHead.next;
  }
  return sll;
};

// Time complexity: O(n)
// Space complexity: O(n)
const deleteDuplicatesImproved = (sll) => {
  const duplicates = {};
  let prev = null;
  let currentHead = sll.head;

  while (currentHead) {
    if (currentHead.data in duplicates && duplicates[currentHead.data]) {
      prev.next = currentHead.next;
    } else {
      duplicates[currentHead.data] = true;
      prev = currentHead;
    }
    currentHead = currentHead.next;
  }
  return sll;
};
