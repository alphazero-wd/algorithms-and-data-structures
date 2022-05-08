class Heap {
  constructor() {
    this.items = [];
  }

  parentIndex(index) {
    return Math.floor((index - 1) / 2);
  }

  leftChildIndex(index) {
    return Math.floor(index * 2 + 1);
  }

  rightChildIndex(index) {
    return Math.floor(index * 2 + 2);
  }

  parent(index) {
    return this.items[this.parentIndex(index)];
  }

  leftChild(index) {
    return this.items[this.leftChildIndex(index)];
  }

  rightChild(index) {
    return this.items[this.rightChildIndex(index)];
  }

  peek() {
    return this.items[0];
  }

  swap(index1, index2) {
    const temp = this.items[index1];
    this.items[index1] = this.items[index2];
    this.items[index2] = temp;
  }

  // O(log(n)) because of the bubble-up
  add(item) {
    this.items.push(item);
    this.bubbleUp();
  }

  // O(log(n)) because of the bubble-down
  poll() {
    this.swap(0, this.items.length - 1);
    const item = this.items.pop();
    this.bubbleDown();
    return item;
  }

  heapsort() {
    const res = [];
    while (this.items.length > 0) {
      res.push(this.poll());
    }
    return res;
  }

  size() {
    return this.items.length;
  }
}

class MinHeap extends Heap {
  constructor() {
    super();
  }

  bubbleUp() {
    let index = this.items.length - 1;
    while (this.parent(index) && this.parent(index) > this.items[index]) {
      this.swap(this.parentIndex(index), index);
      index = this.parentIndex(index);
    }
  }

  bubbleDown() {
    let index = 0;
    while (this.leftChild(index) && this.leftChild(index) < this.items[index]) {
      let smallerChildIndex = this.leftChildIndex(index);
      if (
        this.rightChild(index) &&
        this.items[smallerChildIndex] > this.rightChild(index)
      ) {
        smallerChildIndex = this.rightChildIndex(index);
      }

      this.swap(index, smallerChildIndex);
      index = smallerChildIndex;
    }
  }
}

class MaxHeap extends Heap {
  constructor() {
    super();
  }

  bubbleUp() {
    let index = this.items.length - 1;
    while (this.parent(index) && this.parent(index) < this.items[index]) {
      this.swap(this.parentIndex(index), index);
      index = this.parentIndex(index);
    }
  }

  bubbleDown() {
    let index = 0;
    while (this.leftChild(index) && this.leftChild(index) > this.items[index]) {
      let greaterChildIndex = this.leftChildIndex(index);
      if (
        this.rightChild(index) &&
        this.rightChild(index) > this.items[greaterChildIndex]
      ) {
        greaterChildIndex = this.rightChildIndex(index);
      }
      this.swap(greaterChildIndex, index);
      index = greaterChildIndex;
    }
  }
}

module.exports = { MinHeap, MaxHeap };
