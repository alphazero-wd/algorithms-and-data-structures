# Big-O Notation

## 1. Definition

In computer science, Big-O Notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows become arbitrary large in the **worst** case.

We denote the time complexity as $O(...)$, where the $...$ represents a function (e.g. $O(n)$ where $n$ denotes the input size. Usually, if the input is an array of numbers then $n$ will be the size of the array. If the input is a string then $n$ is the size of the string).

## 2. Examples

### 1. Loops

A common reason why an algorithm is slow is that it contains many loops that go through the input. The more nested loops it contains, the slower it is. If there are $k$ nested loop(s), the time complexity is $O(n^k)$. Here are some examples:

In this example, because there is only one loop. Therefore, the time complexity is $O(n)$

```py
for i in range(1, n):
   print(i)
```

Similarly, because there are two nested loops. Therefore, the time complexity is $O(n^2)$

```py
for i in range(1, n):
   for j in range(1, n):
      print(i, j)
```

### 2. Drop Constant

Suppose $c = const$ and $c > 0$ then:

$O(c + n) = O(n)$

$O(cn) = O(n)$

In these examples, the code inside the loop is executed $3n$, $n + 5$ and $n/2$ times, but the overall time complexity is still `O(n)`.

```py
for i in range(1, 3 * n):
   print(i)
```

```py
for i in range(1, n + 5):
   print(i)
```

```py
for i in range(1, n, 2):
   print(i)
```

As another example, the time complexity of the example below is still $O(n^2)$

```py
for i in range(1, n):
   for j in range(i + 1, n):
      print(i, j)
```

### 3. Phases

If an algorithm consists of multiple phases then the total time complexity is the largest time complexity of a single phase as the slowest phase is the bottleneck of the code.

For example, the time complexities of three phases are $O(n)$, $O(n^2)$ and $O(n)$ respectively, so the overall time complexity is $O(n^2)$.

```py
for i in range(1, n):
   print(i)

for i in range(1, n):
   for j in range(1, n):
      print(i, j)

for i in range(1, n):
   print(i)
```

### 4. Several Factors

Sometimes the time complexity depends on several factors. In this case, the time complexity is $O(nm)$:

```py
for i in range(1, n):
   for j in range(1, m):
      print(i, j)
```

### 5. Recursion (see branch [1_recursion](https://github.com/alphazero-wd/algorithms-and-data-structures/tree/1_recursion))

### 6. Complexity Classes (from lowest to highest)

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Comparison_computational_complexity.svg/1024px-Comparison_computational_complexity.svg.png" width="60%" />

_Some common complexity classes_

- $O(1)$: **Constant Time**

```py
for i in range(1, 1000):
   print(i)
```

- $O(\log_{2} n)$: **Logarithmic Time**

```py
i = 1
while i < n:
   print(i)
   i = i * 2
```

- $O(n)$: **Linear Time**

```py
for i in range(1, n):
   print(i)
```

- $O(n\log_{2} n)$: **Lineararithmic Time**

```py
for i in range(1, n):
   j = 1
   print(i, j)
   while j < n:
      j = j * 2
```

- $O(n^2)$: **Quadratic Time**

```py
for i in range(1, n):
   for j in range(1, n):
      print(i, j)
```

- $O(n^3)$: **Cubric Time**

```py
for i in range(1, n):
   for j in range(1, n):
      for k in range(1, n):
         print(i, j, k)
```

- $O(2^n)$: **Exponential Time** usually appears in recursive functions such as _computing the nth fibonacci number_ or _generate subsets_.

- $O(n!)$: **Factorial Time** usually relating to _finding permutations_.
