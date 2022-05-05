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

module.exports = Stack;
