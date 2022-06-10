## Recursion

1.  Compute the nth fibonacci number in a fibonacci sequence:

        1, 1, 2, 3, 5, 8, 13, 21, ...

    We can see that nth fibonacci number is the sum of the two previous number. We can define the function `fib` like this:

        fib(n) =
            1 if n <= 2
            fib(n - 1) + fib(n - 2)

    > See the code [here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/1_recursion/fibonacci.py)

    Because for every recursive call, there are **two** more recursive calls. Therefore, the time complexity is `O(2^n)`

    See the example of `fib(5)`:

    ![fib(5)](https://i.stack.imgur.com/QVSdv.png)

2.  Pascal Triangle: Compute the value of a cell at position `(row, col)` starting at 0

    ![Pascal Triangle](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

        Input: row = 4, col = 2
        Output: 6

    We can see that the value at position `(row, col)` is the sum of the value at position `(row - 1, col - 1)` and `(row - 1, col)`. We can define function `pascalTriangle` like this:

            pascalTriangle(row, col) =
                1 if col = 0
                0 if row = 0
                pascalTriangle(row - 1, col) + pascalTriangle(row - 1, col - 1)

    > See the code [here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/1_recursion/pascalTriangle.py)

    Because for every recursive call, there are **two** more recursive calls. Therefore, the time complexity is `O(2^row)`
