class DoublyLinkedListNode {
  constructor(data) {
    this.data = data;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  isEmpty() {
    return this.head === null;
  }

  // Time complexity: O(1)
  insertAtHead(value) {
    if (this.head === null) {
      this.head = new DoublyLinkedListNode(value);
      this.tail = this.head;
    } else {
      const newHead = new DoublyLinkedListNode(value);
      this.head.prev = newHead;
      newHead.next = this.head;
      this.head = newHead;
    }
  }

  // Time complexity: O(1)
  insertAtTail(value) {
    if (this.tail === null) {
      this.tail = new DoublyLinkedListNode(value);
      this.head = this.tail;
    } else {
      const newTail = new DoublyLinkedListNode(value);
      newTail.prev = this.tail;
      this.tail.next = newTail;
      this.tail = newTail;
    }
  }

  // Time complexity: O(1)
  deleteAtHead() {
    let toReturn = null;
    if (this.head !== null) {
      toReturn = this.head.data;
      if (this.head === this.tail) {
        this.head = null;
        this.tail = null;
      } else {
        this.head = this.head.next;
        this.head.prev = null;
      }
    }
    return toReturn;
  }

  // Time complexity: O(1)
  deleteAtTail() {
    let toReturn = null;
    if (this.tail !== null) {
      toReturn = this.tail.data;
      if (this.head === this.tail) {
        this.head = null;
        this.tail = null;
      } else {
        this.tail = this.tail.prev;
        this.tail.next = null;
      }
    }
    return toReturn;
  }

  // Time complexity: O(n)
  find(value) {
    let currentHead = this.head;
    while (currentHead !== null) {
      if (currentHead.data === value) return true;
      currentHead = currentHead.next;
    }
    return false;
  }

  traverse() {
    let path = "";
    for (let node = this.head; node !== null; node = node.next) {
      path += node.data + " ⇆ ";
    }
    path += "null";
    return path;
  }
}
