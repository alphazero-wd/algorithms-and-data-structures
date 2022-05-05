const Queue = require("./queue");
// Stack Using Queues
class QueueStack {
  constructor() {
    this.inbox = new Queue();
  }

  // Time complexity: O(1)
  // Space complexity: O(1)
  push(val) {
    this.inbox.enqueue(val);
  }

  // Time complexity: O(n)
  // Space complexity: O(1)
  pop() {
    const size = this.inbox.array.length - 1;
    let counter = 0;
    const bufferQueue = new Queue();
    while (++counter <= size) {
      bufferQueue.enqueue(this.inbox.dequeue());
    }
    const popped = this.inbox.dequeue();
    this.inbox = bufferQueue;
    return popped;
  }

  // Time complexity: O(1)
  // Space complexity: O(1)
  peek() {
    return this.inbox.array[this.inbox.array.length - 1];
  }

  // Time complexity: O(1)
  // Space complexity: O(1)
  isEmpty() {
    return this.inbox.isEmpty();
  }
}
