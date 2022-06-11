# Hash Table

## **1. Definition**

A **Hash table** (HT) is a **fixed size data structure** that stores key-value pairs. It provides a mapping from keys to values using a technique called **hashing**.

![Simple hash table overview](https://f4-zpcloud.zdn.vn/8931703298542969541/2023738c4d1e8d40d40f.jpg)

A HT contains two main methods: `get()` and `put()`. `get()` is used to retrieve data from the HT and `put()` is used to add a key-value pair into the HT. Both of these operations can have a time complexity of `O(1)`.

The keys in a HT must be **unique**, while the values can be **repeated**.

> Javascript's `localStorage` is a typical example of the application of HT. It lets developers persist data inside the browser, and the data can be accessed after a session.

```js
localStorage.setItem("testKey", "testValue");
location.reload(); // refresh the page

localStorage.getItem("testKey"); // prints "testValue"
```

## **2. Hashing Technique**

The most important part of a HT is the hash function `H(x)`. The hash function `H(x)` hashes a key `x` into an index (a whole number in a fixed range) for an array that stores all the data.

A hash function must satisfy three requirements as follows:

1. _Deterministic_: Equal keys produce equal hash values.
2. _Efficiency_: It should be in `O(1)` time.
3. _Uniform distribution_: It makes the most use of the array.

## **3. Prime Number Hashing**

Prime numbers in hashing is important because the modulus division using prime number yields an array index in a distributed manner.

In this example, the hashing function is `H(x) = x % 11`
We create two arrays of size 11, an array for keys, an array for values

![Hash table of size 11, with all empty elements](https://f6-zpcloud.zdn.vn/1551328453689960363/e1b7aca39131516f0820.jpg)

We are going to store keys as integers, values as strings

      { key: 7,  value: "hi" }
      { key: 24, value: "hello" }
      { key: 42, value: "sunny" }
      { key: 34, value: "weather" }

We hash the keys to indexes in the array using a hash function `H(x)` we have just created. The hash results are as following:

      7 % 11 = 7
      24 % 11 = 2
      42 % 11 = 9
      34 % 11 = 1

After all the key-value pairs have been inserted, the result of the HT is shown below.

![Hash table after inserting the value pairs](https://f5-zpcloud.zdn.vn/4352543056116679770/c90401162b84ebdab295.jpg)

Now, let's hash `{ key: 18, value: "wow" }`

      18 % 11 = 7

This is a problem because 7 already exists in the array at index 7. This problem is known as **collision**. Therefore, there are some strategies to handle collisions. One of which is called **probing**.

## **4. Probing**

Probing works by finding the next available index in the array. There are two types of probing: _linear probing_ and _quadratic probing_.

### 1. Linear Probing

Linear Probing works by finding the next available index in the array via **incremental trials**.
For the case where `18` and `7` hashing to the same key, `18` would be hashed into `8` because that is the next empty spot.

![Hash table 1 after using linear probing](https://f7-zpcloud.zdn.vn/6930013798889742499/836ade47b1d5718b28c4.jpg)

When we want to get the key `18`, we start at the original index `7` and keep moving to the next index until the key at that array index is `18`.

The main disadvantage of linear probing is it creates _clusters_ because we would have to go through every element in the array to look for a key, which results in worst case being `O(n)` time.

### 2. Quadratic Probing

Quadratic Probing is a good way to address the cluster issues in linear probing, as it uses perfect square instead of incrementing by 1 each time, and this helps to make the most use of the array.

> Below is the image of linear probing (on top) and quadratic probing (on bottom).

![Linear probing (on top) and quadratic probing (on bottom)](https://f7-zpcloud.zdn.vn/3384153603141016818/c218d9116a83aaddf392.jpg)

### 3. Rehashing/Double-Hashing

Double-Hashing works by having a second hashing function that hashes the result from the original. There are three requirements for a good hashing function:

1. _Different_: It needs to be different to distribute it better.
2. _Efficiency_: It needs to be `O(1)` in time.
3. _Nonzero_: It should never evaluates to zero as zero gives the initial hash value.

A commonly used double-hashing function is as following:

                  H2(x) = R - (x % R) (R <= the size of the HT)

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
|  Insert   |    `O(1)`    |   `O(n)`   |
|   Find    |    `O(1)`    |   `O(n)`   |
