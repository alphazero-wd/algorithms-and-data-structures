# Stacks and Queues

Stacks and queues are **dynamically sized data structures**. They are used in the implementation of other data structures and algorithms e.g. DFS, BFS. Stacks and queues are very similar in the way we add elements but different when it comes to removing elements.
A stack is a **LIFO** (last in first out) data structure, while a queue is a **FIFO** (first in first out) data structure.

## 1. Stacks

### 1. Introduction

A stack is a **LIFO** (last in first out) because the last element to be added is also the first one to be removed.
We add elements on top of the stack (push), while also removing elements from the top of the stack (pop).
These operations can be done in $O(1)$ time using a stack.

> We can think about a stack of plates, to get the bottom plate, you would have to remove all the top ones first.
> <img src=https://upload.wikimedia.org/wikipedia/commons/1/19/Tallrik_-_Ystad-2018.jpg alt="Stack of plates" />

### 2. Implementation

The simplest way to implement a stack is to use a dynamic array i.e. list

1. Peek (get the top element of a stack):

- We simply get the last element in the list, i.e. `stack[stack.length - 1]`
- Time complexity: $O(1)$

2. Push (add elements on top of a stack):

- In Python, we can add elements on to the end of the list by using the `stack.append(val)` method.
- Time complexity: $O(1)$

3. Pop (pop elements from the top of a stack):

- In Python, we can remove the last element of the list by using the `stack.pop()` method and return the value has just been removed.
- Time complexity: $O(1)$

4. Search (check if an element exists in a stack)

- We have to keep popping until the given `target` is found or the stack is empty, which means the element does not exist in a stack.
- Time complexity: $O(n)$

5. Access (access the nth node from the top of a stack)

- We have to keep popping `k` times until `k = n`. In worst case, we might have to pop the entire stack.
- Time complexity: $O(n)$

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Lifo_stack.svg/1280px-Lifo_stack.svg.png" alt="Stack Operation">

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/4_stacks-and-queues/Stack.py)

### 3. Summary

| Operation | Time complexity |
| :-------: | :-------------: |
|   Peek    |     $O(1)$      |
|   Push    |     $O(1)$      |
|    Pop    |     $O(1)$      |
|  Search   |     $O(n)$      |
|  Access   |     $O(n)$      |

## 2. Queues

1. Introduction
   A queue is a **FIFO** (first in first out) because the first element to be added is also the first one to be removed.
   We add elements add the back of the queue (enqueue), while removing elements from the front of the queue (dequeue).
   These operations can be done in $O(1)$ time using a queue.

> We can think about a queue of people, the first people of the queue is removed, while new people waiting in the queue stand at the back of the queue.
> <img src="https://images.pexels.com/photos/761295/pexels-photo-761295.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1">

<br>

![Queue, FIFO](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/1280px-Data_Queue.svg.png)

### 2. Implementation

Same as stack, the simplest way to implement a queue is to use a dynamic array

1. Peek (get the first element of a queue):

- We simply get the first element in the queue, i.e. `queue[0]`
- Time complexity: $O(1)$

2. Enqueue (add elements to the back of a queue):

- Same as stack, we use the `queue.append(val)` method.
- Time complexity: $O(1)$

3. Dequeue (remove elements from the front of a queue):

- In Python, we can remove the first element of the queue by using the `queue.pop(0)` method and return the value has just been removed.
- Time complexity: $O(1)$

4. Search (check if an element exists in a queue)

- We have to keep dequeuing until the given `target` is found or the queue is empty, which means the element does not exist in a queue.
- Time complexity: $O(n)$

5. Access (access the nth node from the front of a queue)

- We have to keep dequeuing `k` times until `k = n`. In the worst case, we might have to dequeue the entire queue.
- Time complexity: $O(n)$

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/4_stacks-and-queues/Queue.py)

### 3. Summary

| Operation | Time complexity |
| :-------: | :-------------: |
|   Peek    |     $O(1)$      |
|  Enqueue  |     $O(1)$      |
|  Dequeue  |     $O(1)$      |
|  Search   |     $O(n)$      |
|  Access   |     $O(n)$      |
