# Hash Table

## **1. Definition**

A **Hash table** (HT) is a **fixed size data structure** that stores key-value pairs. It provides a mapping from keys to values using a technique called **hashing**.

![Simple hash table overview](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/1280px-Hash_table_3_1_1_0_1_0_0_SP.svg.png)
_A small phone book as a hash table_

A HT contains two main methods: `get(key)` and `put(key, value)`. `get(key)` is used to retrieve data from the HT and `put(key, value)` is used to add a key-value pair into the HT. Both of these operations can have a time complexity of $O(1)$.

The keys in a HT must be **unique**, while the values can be **repeated**.

> Javascript's `localStorage` is a typical example of the application of HT. It lets developers persist data inside the browser, and the data can be accessed after a session.

```js
localStorage.setItem("testKey", "testValue");
location.reload(); // refresh the page

localStorage.getItem("testKey"); // prints "testValue"
```

## **2. Hashing Technique**

The most important part of a HT is the hash function $h(x)$. The hash function $h(x)$ hashes a key $x$ into an index (a whole number in a fixed range) for an array that stores all the data.

A hash function must satisfy three requirements as follows:

1. _Deterministic_: Equal keys produce equal hash values.
2. _Efficiency_: It should be in $O(1)$ time.
3. _Uniform distribution_: It makes the most use of the array.

The main problem with HT is to handle **collisions**. Collisions occur when two keys in a HT both hash to the same index in the array. To address this problem, there are several ways, but only _open addressing (probing)_ will be considered.
In the image below, the keys "John Smith" and "Sandra Dee" both hash to 152, resulting in a collision.

![Hashing Collision](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Hash_table_5_0_1_1_1_1_0_SP.svg/1024px-Hash_table_5_0_1_1_1_1_0_SP.svg.png)
_Hash collision resolved by probing with linear probing._

## **4. Probing (Open addressing)**

Probing works by finding the next available index in the array. There are two types of probing: _linear probing_ and _quadratic probing_.

### 1. Linear Probing

Linear Probing works by finding the next available index in the array via **incremental trials**

An example of sequence using linear probing is: $h(x) + 1$, $h(x) + 2$, $h(x) + 3$, $h(x) + k$.

In the image above, we resolved the collision by finding the next empty spot to insert "Sandra Dee" into index 153 in the array.

However, "Ted Baker" also hashes to index 153, we also find the next available index in the array which is 154 and insert there.

### 2. Quadratic Probing

Quadratic Probing is by taking the original hash index and adding successive values of an arbitrary quadratic polynomial until an open slot is found.

An example of sequence using quadratic probing is: $h(x) + 1^2$, $h(x) + 2^2$, $h(x) + 3^2$, ..., $h(x) + k^2$

### 3. Rehashing/Double-Hashing

Double-Hashing works by having a second hashing function that hashes the result from the original. There are three requirements for a good hashing function:

1. _Different_: It needs to be different to distribute it better.
2. _Efficiency_: It needs to be $O(1)$ in time.
3. _Nonzero_: It should never evaluates to zero as zero gives the initial hash value.

A commonly used double-hashing function is as following:

   $h2(x) = R - (x \mod R) (R \leq n)$, $n$ is the size of the HT

## 4. Implementation

1. Create two arrays `keys` and `values` which both have the size of `size`
2. Algorithm for `put(key, value)`

   1. Get the `index` by calling `H(key)`
   2. If `keys[index] != null` then either perform linear probing or quadratic probing
   3. Repeat step 2 until `keys[index] = null`
   4. Insert `keys[index] = key` and `values[index] = value`

3. Algorithm for `get(key)`
   1. Get the `index` by calling `H(key)`
   2. If `keys[index] != key` then either perform linear probing or quadratic probing
   3. Repeat step 2 until `keys[index] = key`
   4. Get the value by accessing `values[index]`

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/3_hash-tables/HashTable.py)

## 5. Summary

| Operation | Average Case | Worst Case |
| :-------: | :----------: | :--------: |
|  Insert   |    $O(1)$    |   $O(n)$   |
|   Find    |    $O(1)$    |   $O(n)$   |
