class SinglyLinkedListNode {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null;
  }

  isEmpty() {
    // or return this.head === null
    return this.head === null;
  }

  // insert at the head of the SLL
  // Time complexity: O(1)
  insert(value) {
    if (this.isEmpty()) {
      this.head = new SinglyLinkedListNode(value);
    } else {
      const oldHead = this.head;
      const newHead = new SinglyLinkedListNode(value);
      newHead.next = oldHead;
      this.head = newHead;
    }
  }

  // delete node whose data = given value
  // Time complexity: O(n)
  remove(value) {
    let currentHead = this.head;
    // if the removed node is the head
    if (this.head.data === value) {
      this.head = currentHead.next;
    } else {
      // in the middle of the SLL
      let prev = currentHead;
      while (currentHead) {
        if (currentHead.data === value) {
          prev.next = currentHead.next;
          break;
        } else {
          prev = currentHead;
        }
        currentHead = currentHead.next;
      }
    }
  }

  // Time complexity: O(1)
  deleteAtHead() {
    let toReturn = null;
    if (this.head !== null) {
      toReturn = this.head.data;
      this.head = this.head.next;
    }
    return toReturn;
  }

  // Time complexity: O(n)
  find(value) {
    let currentHead = this.head;
    while (currentHead) {
      if (currentHead.data === value) return true;
      currentHead = currentHead.next;
    }
    return false;
  }

  traverse() {
    let path = "";
    for (let node = this.head; node !== null; node = node.next) {
      path += node.data + " -> ";
    }
    path += "null";
    return path;
  }
}
module.exports = SinglyLinkedList;
