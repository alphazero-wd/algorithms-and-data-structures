// Stack is a LIFO (last in first out) data structure
class Stack {
  constructor(array = []) {
    this.array = array;
  }

  // O(1)
  peek() {
    return this.array[this.array.length - 1];
  }

  // O(1)
  push(value) {
    this.array.push(value);
  }

  // O(1)
  isEmpty() {
    return this.array.length === 0;
  }

  // O(1)
  pop() {
    return this.array.pop();
  }
}

// Queue Using Stacks
class TwoStackQueue {
  constructor() {
    this.inbox = new Stack(); // new Stack();
    this.outbox = new Stack(); // new Stack();
  }

  // Time complexity: O(1)
  // Space complexity: O(1)
  enqueue(val) {
    this.inbox.push(val);
  }

  // Time complexity: Amortized O(1), Worst O(n)
  // Space complexity: O(1)
  // See more about Amortized Analysis here: https://leetcode.com/problems/implement-queue-using-stacks/solution/
  dequeue() {
    if (this.outbox.isEmpty()) {
      while (!this.inbox.isEmpty()) {
        this.outbox.push(this.inbox.pop());
      }
    }
    return this.outbox.pop();
  }

  // Time complexity: O(1)
  // Space complexity: O(1)
  peek() {
    if (this.outbox.isEmpty()) {
      while (!this.inbox.isEmpty()) {
        this.outbox.push(this.inbox.pop());
      }
    }
    return this.outbox.peek();
  }

  // Time complexity: O(1)
  // Space complexity: O(1)
  isEmpty() {
    return this.inbox.isEmpty && this.outbox.isEmpty();
  }
}
