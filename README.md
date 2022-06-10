# Searching

> Problem: Given an sorted array of numbers `nums` and a number `target`. Return the index of the target if `target` exists in `nums`. Otherwise return `-1`

## **1. Linear Search**

**Algorithm**:

1. Scan through `nums`
2. If at any point `i`, `nums[i] = target`, return `i`
3. After the loop, if `target` is not found, return `-1`

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/2_searching-and-sorting/searching/linearSearch.py)

**Time complexity**: `O(n)` (`n` is the number of elements in `nums`)

## **2. Binary Search**

We can see in the problem statement that we are given a **sorted** array. Therefore, we can reduce the time complexity even further by implementing **binary search**.

**Idea**:

The idea is if `nums` is sorted, then we will find the middle element `nums[mid]` to see if it is the `target`. If `nums[mid]` is not `target`, we can just cut off half of `nums` and only search on the other half. This reduces the time complexity significantly.

**Algorithm**:

1. Find the middle index `mid` of `nums`
2. If `nums[mid] = target`, return `mid`
3. If `nums[mid] > target`, search the left half of `nums`
4. Otherwise, search the right half of `nums`
5. Repeat step 1 to 4
6. Return `-1` if `target` is not found in `nums`

**Time complexity**: `O(log(n))`

# Sorting

> Problem: Given an array of numbers `nums`. Sort `nums` in ascending order.

In this sorting section, we will be discussing some sorting algorithms.

## **1. Bubble Sort**

**Idea**:

Bubble Sort is the simplest sorting algorithm among all. It works by swapping an element with the previous one if they are in the wrong order.

![Visualization](https://upload.wikimedia.org/wikipedia/commons/0/06/Bubble-sort.gif)

**Algorithm**:

1. Have `i` scan through every element in `nums`
2. Have `j` Scan through every previous element of `nums`
3. If `nums[i] < nums[j]`, swap `nums[i]` with `nums[j]`
4. Repeat step 1 to 3

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/2_searching-and-sorting/sorting/bubbleSort.py)

**Time complexity**: `O(n^2)`

**Space complexity**: `O(1)`

## **2. Selection Sort**

**Idea**:

Selection Sort works by finding the minimum element after every element and swap them

![Visualization](https://i2.wp.com/algorithms.tutorialhorizon.com/files/2019/01/Selection-Sort-Gif.gif?ssl=1)

**Algorithm**:

1. Have `i` scan through every element in `nums`
2. Have `j` scan through every element after `i`
3. Find the minimum element `nums[min_index]` whose index is not equal to `i`
4. Swap `nums[i]` with `nums[min_index]`
5. Repeat step 1 to 4

**Time complexity**: `O(n^2)`

**Space complexity**: `O(1)`

## **3. Insertion Sort**
