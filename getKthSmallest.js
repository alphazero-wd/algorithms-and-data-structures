const { MinHeap } = require("./heaps");

// Time complexity: O(klog(n))
// Time complexity: O(n)
const getKthSmallest = (array, k) => {
  const minHeap = new MinHeap();
  for (let num of array) {
    minHeap.add(num);
  }
  for (let i = 1; i < k; i++) {
    minHeap.poll();
  }
  return minHeap.poll();
};
