# Heaps and Heapsort

## Heaps

### 1. Introduction to Heaps

A _heap_ is a **tree-like data structure** in which the parent is greater than its children (if _max-heap_) or less than its children (if _min-heap_).
A heap is an important data structure that returns the lowest or highest element in `O(1)` time. This property of heap is useful for sorting data (heapsort) in `O(nlog(n))` time.

![Heap](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Min-heap.png/330px-Min-heap.png)

There are many types of heaps that have different number of children. Only **binary heaps** will be considered for simplicity.

Unlike a tree, we use an **array** to represent a heap instead of pointers to children nodes (see the image below). We can easily calculate the parent, left child and right child of a node in a binary heap.

![Heap indices](https://hyosup0513.github.io/public/images/2heap1.PNG)

> Note that the first element in a heap starts at 1. This is because it is easier to compute the indices of the parent, left and right children of an element in a heap.

### 2. Binary Heap Array Index Structure

| Node        |  Index   |
| ----------- | :------: |
| Itself      |   `k`    |
| Parent      | `k / 2`  |
| Left Child  |   `2k`   |
| Right Child | `2k + 1` |

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/7_heaps/Heap.py)

### 3. Implementation

When an element is added or removed from the heap, we need to maintain the structure of a heap.
We will only consider the case in a **max-heap** as it is almost similar in a **min-heap**

1. Swim:

   2. If `last > parent(last)`, swap `last` with `parent(last)`.
   3. Set `last` to `parent(last)`.
   4. Repeat step 2 and 3 until `last` is in the correct position.

   **Time complexity**: `O(log(n))`

   ![Insertion in a Max Heap](https://cdn-media-1.freecodecamp.org/images/v7W4gtqZZ4vknoz9-Qj28CuXtviStsYYXAS8)

2. Sink:

   4. If `last < left_child(last)`, compare `left_child(last)` and `right_child(last)`

      1. Swap `last` with `max(left_child(last), right_child(last))`
      2. Set `last` to `max(left_child(last), right_child(last))`

   5. Repeat step 4 until `last` is in the correct position.
   6. Return `max`

   **Time complexity**: `O(log(n))`

   ![Deletion in a Heap](https://media.hoclaptrinh.vn/images/cau-truc-du-lieu-heap5c3465ea021c3.gif)

3. Insert an element into a max heap:

   1. Insert the element at the end of the array and call it `last`.

      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Heap_add_step1.svg/225px-Heap_add_step1.svg.png" >

      _Suppose we want to insert 15 into the heap_

   2. Perform `swim(n)`

       <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Heap_add_step2.svg/225px-Heap_add_step2.svg.png">

      The heap property has been violated 15 > 8 so we swap 8 with 15

       <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Heap_add_step3.svg/225px-Heap_add_step3.svg.png">

      15 > 11, swap 15 with 11 which is now a valid max-heap.

4. Delete the max element from a max heap:

   1. Call the first/max element `max` and the last element in the array `last`

      Suppose we have a heap as before and we want to delete the max element which is 11 from the heap.

       <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Heap_add_step3.svg/225px-Heap_add_step3.svg.png">

   2. Swap `max` with `last`, `max` is now at the end of the array and remove `max` by popping the array

      We swap 11 with 4 and remove the 11

       <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Heap_remove_step1.svg/225px-Heap_remove_step1.svg.png">

   3. Perform `sink(1)`

      Now the heap property is violated so we swap 8 with 4. This is now a valid max-heap.

       <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Heap_remove_step2.svg/225px-Heap_remove_step2.svg.png">

5. Get the max element in a max-heap: Simply returns `array[1]`

   **Time complexity**: `O(1)`

[See the implementation for max-heap](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/7_heaps/MaxHeap.py)

[See the implementation for min-heap](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/7_heaps/MinHeap.py)

### 4. Summary

| Operation    | Time complexity |
| ------------ | :-------------: |
| Insertion    |   `O(log(n))`   |
| Deletion     |   `O(log(n))`   |
| Find Max/Min |     `O(1)`      |

## Heapsort

**Idea**:

We can construct a max-heap from the array we want to sort `nums` (in-place). See the visualization below:

> Convert the array `nums` which stores a complete binary tree with `n` nodes to a max-heap by repeatedly using `sink` function in a bottom-up manner. The array elements indexed by `floor(n/2) + 1, floor(n/2) + 2, ..., n` are all leaves for the tree (assuming that indices start at 1) - thus each is a one-element heap, and does not need to be sunk.

![Heapsort Visualization](https://upload.wikimedia.org/wikipedia/commons/4/4d/Heapsort-example.gif)

**Algorithm**:

1. Construct a max-heap from `nums`

   1. Have `k` start at `parent(n)`, i.e. `n / 2` and move down by 1 until `k = 1`
   2. Perform `sink(k, n)`

2. Perform heapsort
   1. If `n > 1` then
      1. Swap `nums[1]` with `nums[n]` and decrement `n` by 1
      2. Perform `sink(1, n)`
   2. Repeat step 1

**Time complexity**: `O(nlog(n))`
