const reverseSinglyLinkedList = (sll) => {
  if (!sll) return null;
  let currentHead = sll.head;
  let prev = null;
  let next = sll.next;
  while (currentHead) {
    next = currentHead.next;
    currentHead.next = prev;
    prev = currentHead;
    currentHead = next;
  }
  return prev;
};
