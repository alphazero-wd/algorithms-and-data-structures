## Master Theorem

> Master Theorem is used to analyse the time complexity of recursive functions

### **1. Decreasing Function**

$T(n) = aT(n - b) + f(n) (a > 0, b > 0, f(n) = O(n^k), k \geq 0)$

If $a = 1$ then $T(n) = O(nf(n))$

If $a > 1$ then $T(n) = O(a^{n\over b}f(n))$

If $a < 1$ then $T(n) = O(f(n))$


_Examples:_

- Case 1:

$T(n) = T(n - 1) + 1 = O(n)$

$T(n) = T(n - 1) + n = O(n^2)$

$T(n) = T(n - 1) + \log_{2} n = O(n\log_{2} n)$


- Case 2:

$T(n) = 2T(n - 1) + 1 = O(2^n)$

$T(n) = 3T(n - 1) + 1 = O(3^n)$

$T(n) = 2T(n - 1) + n = O(n2^n)$

### **2. Dividing Function**

$T(n) = aT(\frac{n}{b}) + f(n) (a \geq 1, b > 1, f(n) = O(n^k{\log^p_{2} n)}), k \geq 0)$

- Case 1: If $\log_{b} a > k$ then $T(n) = Θ(n^{\log_{b} a})$

- Case 2: If $\log_{b} a = k$ then:
  - Case 2.1: If $p > -1$ then $T(n) = Θ({n^k\log^{p + 1}_{2} n})$
  - Case 2.2: If $p = -1$ then $T(n) = Θ(n^k\log_{2}{(\log_{2} n)})$
  - Case 2.3: If $p < -1$ then $T(n) = Θ(n^k)$
- Case 3: If $\log_{b} a < k$ then:
  - Case 3.1: If $p >= 0$ then $T(n) = Θ(n^k{\log^p_{2} n})$
  - Case 3.2: If $p < 0$ then $T(n) = O(n^k)$

_Examples_:

- Case 1: $T(n) = 2T(\frac{n}{2}) + 1$

  Solution:

  $a = 2; b = 2 => \log_{b} a = \log_{2} 2 = 1$
                        
  $f(n) = Θ(1) = Θ(n^0 + \log_{0} n) => k = 0 => \log_{b} a > k$

  Therefore, $T(n) = Θ(n^{\log_{b} a}) = Θ(n^1) = Θ(n)$

- Case 2:
  - Case 2.1: $T(n) = 2T(\frac{n}{2}) + n$
    Solution: 
    
    $\log_{b} a = 1; k = 1 => \log_{b} a = k; p = 0$
    
    Therefore, $T(n) = Θ(n^k\log_{2}^{p + 1} n) = Θ(n\log_{2} n)$


  - Case 2.2: $T(n) = 2T(\frac{n}{2}) + (\frac{n}{\log_{2} n})$
    
    Solution: $\log_{b} a = 1; k = 1; p = -1$
    
    Therefore, $T(n) = Θ(n\log_{2}(\log_{2} n))$

  - Case 2.3: $T(n) = 2T(\frac{n}{2}) + (n\log_{n}^{-2})$
                    
    Solution: $log_{b} a = 1; k = 1; p = -2 > -1$
    
    Therefore, $T(n) = Θ(n)$

- Case 3:
  - Case 3.1: $T(n) = T(frac{n}{2}) + n^2$
    
    Solution: $\log_{b} a = 0; k = 2; p = 0 \geq 0$
    
    Therefore, $T(n) = Θ(n^2)$

  - Case 3.2: $T(n) = T(\frac{n}{2}) + \frac{n^3}{\log_{2} n})$
    
    Solution: $\log_{b} a = 0; k = 3; p = -1 < 0$ 
    
    Therefore, $T(n) = Θ(n^3)$

## Recursion Examples

### **1. Compute the nth fibonacci number in a fibonacci sequence:**

                    1, 1, 2, 3, 5, 8, 13, 21, ...

We can see that nth fibonacci number is the sum of the two previous number. We can define the function `fib` like this:

                    fib(n) = 1 if n <= 2
                           = fib(n - 1) + fib(n - 2) if n > 2

> [See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/1_recursion/fibonacci.py)

**Time complexity**: `O(2^n)`

_Proof:_

```
    T(n) = 1 if n <= 2
         = T(n - 1) + T(n - 2) + 1 if n > 2
         = 2T(n - 1) + 1
    Applying master theorem we for decreasing function have: T(n) = O(2^n)
```

See the example of `fib(5)`:

![fib(5)](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Fibonacci_Tree_5.svg/1280px-Fibonacci_Tree_5.svg.png)

### **2. Pascal Triangle: Compute the value of a cell at position `(row, col)` starting at 0**

![Pascal Triangle](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

    Input: row = 4, col = 2
    Output: 6

We can see that the value at position `(row, col)` is the sum of the value at position `(row - 1, col - 1)` and `(row - 1, col)`. We can define function `pascalTriangle` like this:

    pascalTriangle(row, col) =  1 if col = 0
                             =  0 if row = 0
                             =  pascalTriangle(row - 1, col) + pascalTriangle(row - 1, col - 1) if row > 0 and col > 0

> [See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/1_recursion/pascalTriangle.py)

**Time complexity**: `O(2^n)`, where `n` is the given `row`

_Proof:_

```
    T(n) = 1 if n = 0
         = 2T(n - 1) + 1 if n > 0
    Applying master theorem for decreasing function we have: T(n) = O(2^n)
```
