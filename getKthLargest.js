const { MaxHeap } = require("./heaps");

// Time complexity: O(klog(n))
// Time complexity: O(n)
const getKthLargest = (array, k) => {
  const maxHeap = new MaxHeap();
  for (let num of array) maxHeap.add(num);
  for (let i = 1; i < k; i++) {
    maxHeap.poll();
  }
  return maxHeap.poll();
};
