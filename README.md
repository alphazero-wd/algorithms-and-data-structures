## Master Theorem

> Master Theorem is used to analyse the time complexity of recursive functions

### **1. Decreasing Function**

                    T(n) = aT(n / b) + f(n) (a > 0, b > 0, f(n) = O(n^k) where k >= 0)

                    If a = 1 then T(n) = O(nf(n))
                    If a > 1 then T(n) = O(a^(n/b) * f(n))
                    If a < 1 then T(n) = O(f(n))

## Recursion Examples

### **1. Compute the nth fibonacci number in a fibonacci sequence:**

    1, 1, 2, 3, 5, 8, 13, 21, ...

We can see that nth fibonacci number is the sum of the two previous number. We can define the function `fib` like this:

    fib(n) =
        1 if n <= 2
        fib(n - 1) + fib(n - 2)

> [See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/1_recursion/fibonacci.py)

**Time complexity**: `O(n^2)`

Proof:

```
    T(n) = 1 if n = 0
         = T(n - 1) + T(n - 2) + 1
         = 2T(n - 1) + 1
         = 2^2 * T(n - 2) + 2 + 1
         = 2^3 * T(n - 3) + 4 + 2 + 1
         = ...
         = 2^k * T(n - k) + 2^(k - 1) + 2^(k - 2) + ... + 4 + 2 + 1
         = ...
         = 2^n * T(0) + 2^(n - 1) + 2^(n - 2) + ... + 4 + 2 + 1
         = 2^n + 2^n - 1
         = 2^(n + 1) - 1
         = O(2^n)
```

See the example of `fib(5)`:

![fib(5)](https://i.stack.imgur.com/QVSdv.png)

### **2. Pascal Triangle: Compute the value of a cell at position `(row, col)` starting at 0**

![Pascal Triangle](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

    Input: row = 4, col = 2
    Output: 6

We can see that the value at position `(row, col)` is the sum of the value at position `(row - 1, col - 1)` and `(row - 1, col)`. We can define function `pascalTriangle` like this:

    pascalTriangle(row, col) =
        1 if col = 0
        0 if row = 0
        pascalTriangle(row - 1, col) + pascalTriangle(row - 1, col - 1)

> [See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/1_recursion/pascalTriangle.py)

**Time complexity**: `O(2^n)`, where `n` is the given `row`

Proof:

```
   T(n) = 1 if n = 0
        = 2T(n - 1) + 1
        = 2^2 * T(n - 2) + 2 + 1
        = 2^3 * T(n - 3) + 4 + 2 + 1
        = ...
        = 2^k * T(n - k) + 2^(k - 1) + 2^(k - 2) + ... + 4 + 2 + 1
        = ...
        = 2^n * T(0) + 2^(n - 1) + 2^(n - 2) + ... + 4 + 2 + 1
        = 2^n + 2^n - 1
        = 2^(n + 1) - 1
        = O(2^n)
```
