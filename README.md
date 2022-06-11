# Searching

> Problem: Given an sorted array of numbers `nums` and a number `target`. Return the index of the target if `target` exists in `nums`. Otherwise return `-1`

## **1. Linear Search**

**Idea**:

Scan through every element in `nums` and see if a number in `nums` is equal to `target`

![Visualization](https://icancodeit.files.wordpress.com/2019/08/linear-search-algorithm.gif)

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

![Visualization](https://d18l82el6cdm1i.cloudfront.net/uploads/bePceUMnSG-binary_search_gif.gif)

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

    Input: nums = [3, 2, 1, 5, 6, 4]
    Output: [1, 2, 3, 4, 5, 6]

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

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/2_searching-and-sorting/sorting/selectionSort.py)

**Time complexity**: `O(n^2)`

**Space complexity**: `O(1)`

## **3. Insertion Sort**

**Idea**:

Insertion Sort works by swapping current element with previous elements until it is in the correct position.

![Visualization](https://upload.wikimedia.org/wikipedia/commons/9/9c/Insertion-sort-example.gif)

**Algorithm**:

1. Have `i` scan through every element in `nums`
2. Have `j` scan from the current element to the first element in `nums`
3. If `nums[j] < nums[j - 1]`, swap `nums[j]` with `nums[j - 1]`
4. Repeat step 1 to 3

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/2_searching-and-sorting/sorting/insertionSort.py)

**Time complexity**: `O(n^2)`

**Space complexity**: `O(1)`

## **4. Quicksort**

**Idea**:

Quicksort works by **partitioning** the element, which means we choose a **pivot**, and we want every element **less than** the pivot on the **left** side of the pivot and the remaining on the **right**.

![Visualization](https://upload.wikimedia.org/wikipedia/commons/9/9c/Quicksort-example.gif)

**Algorithm**:

1. Have `left` and `right` initially start at the beginning and end of `nums` respectively
2. Partitioning `nums`
   1. Have `pivot` is an element at the middle of `nums`
   2. Move `left` to the right by 1 while `nums[left] < pivot`
   3. Move `right` to the left by 1 while `nums[right] > pivot`
   4. If `left` and `right` cross, return `left`
   5. Swap `nums[left]` with `nums[right]`
3. Repeat step 2 for `nums[left, p - 1]` and `nums[p + 1, right]` (`p` is the partition index returned from step 2)

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/2_searching-and-sorting/sorting/quickSort.py)

**Time complexity**: `O(nlog(n))`, worst case `O(n^2)`

_Proof_: Using master theorem for dividing functions, we have:

        T(n) = 2T(n / 2) + n
        T(n) = O(nlog(n))

**Space complexity**: `O(log(n))`

### **Extra algorithm: Quick Select**

> Problem: Given an array of numbers `nums` and an integer `k`. Find the kth smallest element in `nums`

    Input: nums = [3, 2, 1, 5, 6, 4], k = 3
    Output: 3

Quick select is an algorithm based on quicksort to find the kth smallest element in an unordered array. Unlike quicksort, we only recur on one side of the array `nums` to find the kth smallest element. Therefore the time complexity reduces from `O(nlog(n))` to `O(n)`

**Algorithm**:

1. Have `left` and `right` initially start at the beginning and end of `nums` respectively
2. Partition `nums` like in quicksort
3. If `p = k`, that is the kth smallest element
4. If `p > k`, search on `nums[left, p - 1]`
5. If `p < k`, search on `nums[p + 1, right]`

[See the code here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/2_searching-and-sorting/sorting/quickSelect.py)

**Time complexity**: `O(n)`, worst case: `O(n^2)`

_Proof_: Using master theorem for dividing functions, we have:

        T(n) = T(n / 2) + n
        T(n) = O(n)

**Space complexity**: `O(1)`

## **5. Merge Sort**

**Idea**:

Merge Sort works by dividing an array into halves until it can be sorted, and merge two sorted halves to form a sorted array

![Visualization](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif?20151222172210)

**Algorithm**:

1. Have `left` and `right` start at the beginning and end of `nums` respectively
2. Find `mid = (left + right) // 2`
3. Recursively sort two subarrays `nums[left, mid]` and `nums[mid + 1, right]` until `left >= right`
4. Merge two sorted subarrays together

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/2_searching-and-sorting/sorting/mergeSort.py)

**Time complexity**: `O(nlog(n))`

_Proof_: Using master theorem for dividing functions, we have:

        T(n) = 2T(n / 2) + n
        T(n) = O(nlog(n))

**Space complexity**: `O(n)`
