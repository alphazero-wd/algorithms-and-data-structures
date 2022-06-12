# Linked Lists

## Singly Linked Lists

### **1. Definition**

A Singly Linked List (SLL) is a **data structure** that consists of nodes where each node has a value and a pointer (reference) to the next node.

![Singly Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/1920px-Singly-linked-list.svg.png)

**Some terminologies used in the linked list** (see the image above):

- Node e.g. `A`, `B`, `C`, `D` are nodes.
- Pointer (reference) e.g. node `A` has a pointer (reference) to node `B`.
- Head: the first node in a SLL e.g. node `A` is the head of the SLL above.
- Tail: the last node in a SLL, i.e. the node that has a pointer to `null` e.g. node `D` is the tail of the SLL.

### **2. Implementation**

A node has two attributes: `val` is the value a node holds, `next` is a pointer to the next node.
We can create a class `ListNode` as following:

```py
class ListNode:
   def __init__(self, val: int):
      self.val = val
      self.next = None
```

We also need a class `SLL` that has one attribute, which is the `head` of the SLL:

```py
class SLL:
   def __init__(self):
      self.head = None
```

1. Insert node at the head of a SLL:

   1. Create a new node `new_node`
   2. If `head` is `null`, `head = new_node`
   3. Store `old_head = head` because we will update `head`.
   4. Set `head` to `new_node`
   5. Set `new_node.next` to `old_head`

   **Time complexity**: `O(1)`

2. Delete node at the head of a SLL:

   1. If `head` is `null`, then there is nothing to do
   2. Set `head` to `head.next`

   **Time complexity**: `O(1)`

3. Delete node by a value in a SLL:

   1. If `head` is `null`, then there is nothing to do
   2. If `head.val = given_val`, solve case 2.
   3. Have temporary variables `cur` to keep track of the current node and `prev` to keep track the node before `cur`.
   4. While `cur` is not `null`,
      1. If `cur.val = given_val`, set `prev.next` to `cur.next`
      2. Move `prev` to `cur` and `cur` to `cur.next`

   **Time complexity**: `O(n)`

4. Search (check if there is a node that satisfies `node.val = given_val`)

   1. If `head` is `null`, return `false` as there is no node that satisfies `val = given_val`.
   2. If `head.val = given_val`, return `true`.
   3. Have a temporary variable `cur` to keep track of the current node.
   4. While `cur` is not `null`,
      1. If `cur.val = given_val`, return `true`.
      2. Move `cur` to `cur.next`.
   5. Return `false` if there is no node that satisfies `node.val = given_val`.

   **Time complexity**: `O(n)`

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/5_linked-lists/SinglyLinkedList.py)

| Operation               | Time complexity |
| ----------------------- | :-------------: |
| Insert at head          |     `O(1)`      |
| Delete at head          |     `O(1)`      |
| Delete by a given value |     `O(n)`      |
| Search                  |     `O(n)`      |

## Doubly Linked Lists

### 1. Definition

A Doubly Linked List (DLL) is the pretty much the same as a SLL. However, a node in a DLL also has a **pointer to the previous node** (see the image below).

![Doubly Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/1920px-Doubly-linked-list.svg.png)

### **2. Implementation**

A node in the DLL has three attributes: `val` is the value a node holds, `next` is a pointer to the next node and `prev` is a pointer to the previous node.
We can create a class `ListNode` as following:

```py
class ListNode:
   def __init__(self, val: int):
      self.val = val
      self.next = None
      self.prev = None
```

We also need a class `DLL` that has two attributes, which are `head` and `tail` of the DLL:

```py
class DLL:
   def __init__(self):
      self.head = None
      self.tail = None
```

1. Insert node at the head of a DLL:

   1. Create a new node `new_node`
   2. If `head` is `null`, `head = tail = new_node`
   3. Store `old_head = head` because we will update `head`.
   4. Set `head` to `new_node`
   5. Set `new_node.next` to `old_head`
   6. Set `old_head.prev` to `new_node`

   **Time complexity**: `O(1)`

2. Insert node at the head of a DLL:

   1. Create a new node `new_node`
   2. If `head` is `null`, `head = tail = new_node`
   3. Store `old_tail = tail` because we will update `tail`.
   4. Set `tail` to `new_node`
   5. Set `tail.prev` to `old_tail`
   6. Set `old_tail.next` to `new_node`

   **Time complexity**: `O(1)`

3. Delete node at the head of a DLL:

   1. If `head` is `null`, then there is nothing to do
   2. Set `head` to `head.next`
   3. Set `head.next.prev` to `null`

   **Time complexity**: `O(1)`

4. Delete node at the tail of a DLL:

   1. If `head` is `null`, then there is nothing to do
   2. If `head` is `tail`, then set both `head` and `tail` to `null`
   3. Else, set `tail` to `tail.prev` and `tail.next` to `null`

   **Time complexity**: `O(1)`

5. Search (same as SLL)

   **Time complexity**: `O(n)`

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/5_linked-lists/DoublyLinkedList.py)

| Operation      | Time complexity |
| -------------- | :-------------: |
| Insert at head |     `O(1)`      |
| Insert at tail |     `O(1)`      |
| Delete at head |     `O(1)`      |
| Delete at tail |     `O(1)`      |
| Search         |     `O(n)`      |
