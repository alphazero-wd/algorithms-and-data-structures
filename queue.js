// Queue is a FIFO (first in first out) data structure
class Queue {
  constructor(array = []) {
    this.array = array;
  }

  // O(1)
  peek() {
    if (this.isEmpty()) return null;
    return this.array[0];
  }

  // O(1)
  enqueue(value) {
    this.array.push(value);
  }

  // O(1)
  isEmpty() {
    return this.array.length === 0;
  }

  // O(1)
  dequeue() {
    return this.array.shift();
  }
}

module.exports = Queue;
