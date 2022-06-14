# Dynamic Programming (DP)

## 1. Definition

Dynamic Programming (DP) is simply an optimazation technique for recursive problems. Whenever a problem can be solved recursively and there are some repeated recursive calls to the same input. We can store the result of the input so that we do not have to recompute it when the input shows up again.

A problem can be solved using DP if it satisfies either conditions:

- _Overlapping subproblems_: DP combines the results of subproblems. Therefore, it is used when the solution of a subproblem is needed again and again by storing in a data structure e.g. array, hash table so it does not have to be recomputed again.
- _Optimal substructure_: A given problem has optimal substructure if optimal solution of the given problem can be obtained by using optimal solutions of its subproblems. In the Dijkstra algorithm for finding the shortest path from vertex `u` to `v`, if vertex `x` lies in the shortest path from `u` to `v`, then the shortest path from `u` to `v` is the shortest path from `u` to `x` and from `x` to `v`.

## 2. Some DP Problems

### 1. Fibonacci

In the recursion chapter, we have discussed about the recursive solution.

```py
def fib(n):
  if n == 0: return 0
  if n == 1: return 1
  return fib(n - 1) + fib(n - 2)
```

However, the time complexity is `O(2^n)`, which is bad. Let's take a look at the recursion tree and see why:

![Recursion tree for fibonacci](https://camo.githubusercontent.com/b105d14612280fb13ddb2aad994dee9cade1a373078c8f7210d5b578ded3cb9f/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f652f65612f4669626f6e616363695f547265655f352e7376672f3132383070782d4669626f6e616363695f547265655f352e7376672e706e67)

We can see that `fib(3)` is being called twice, `fib(2)` is called three times. There are a lot repetitions here. Therefore, we need to store the solution to `fib(3)` and `fib(2)` into a hash map or an array so that when `fib(3)` is called on the right subtree, it does not have to recompute the solution. This technique is called **memoization**.

The code below shows how memoization works. It checks if `n` is in the memo table and return the solution instead of recomputing.
This reduces the time complexity significantly from exponential to linear.

```py
def fib(n, memo={}):
  if n in memo: return memo[n]
  if n == 0: return 0
  if n == 1: return 1
  memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
  return memo[n]
```

**Time complexity**: `O(n)`

**Space complexity**: `O(n + n) = O(n)` (because of `memo` table and the underlying call stack)

Apart from memoization, another solution is the **bottom-up (tabulation)** approach where we build the table from the bottom to the top and accumulate the answers to the top.

Unlike memoization, the bottom-up approach solves a problem **iteratively**, which is a slight advantage.

In the fibonacci example, we compute `dp[0] = 0` and `dp[1] = 1` then `dp[i] = dp[i - 1] + dp[i - 2] (2 <= i <= n)`.

> Memoization will result in a stack over flow error if `n` is too big e.g. `fib(10^6)` due to the limitation of the call stack memory. However, the bottom-up approach works for any `n` value as it approaches a problem iteratively.

The code below shows how bottom-up approach to fibonacci problem.

```py
def fib_dp(n):
  dp = [None] * (n + 1)
  dp[0] = 0
  dp[1] = 1
  for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
  return dp[n]
```

> **Follow up**: Can you think of a solution in `O(1)` space?

**Time complexity**: `O(n)`

**Space complexity**: `O(n)`

[See the full implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/9_dynamic-programming/fibonacci.py)

### 2. 0/1 Knapsack Problem

> Given `n` weights and the values of items, put these items in a
> knapsack of a given capacity, `w`, to get the maximum total value in
> the knapsack.

    Input: items = [[4, 12], [2, 2], [2, 1], [10, 4], [1, 1]], w = 15
    Output: 15
    Explaination: Pick items[3] which has a value of 10, items[1] which has a value of 2, items[2] which has a value of 2 and items[4] which has a value of 1. In total, the value is 15 and the weight is less than 15.

### 1. Recursive Solution:

**Optimal Substructure**:

For every `items[i]` in `items`, we can observe that:

- `items[i]` is included in the knapsack.
- `items[i]` is not included in the knapsack.

The maximum value can only either be:

- Excluding `items[i]`: max value obtained with `i - 1` items.
- Including `items[i]` if only `w(i) <= w`: max value obtained with `i - 1` items and `w - w(i)`.

**Algorithm**:

1. Have `i` denote the current index in `items` and `w` is the maximum weight a knapsack can hold.
2. If `i < 0` or `w = 0`, return 0
3. If `w(i) > w`, skip over `items[i]`
4. Else, pick the max of including `items[i]` and including `items[i]`. If including, reduce `w` by `w(i)`.

**Implementation**:

```py
def knapsack(items, w):
  def solve(i, w):
    if i < 0 or w == 0: return 0

    # items[i][0] = v(i)
    # items[i][1] = w(i)
    if items[i][1] > w:
      return solve(i - 1, w)
    return max(
      solve(i - 1, w),
      items[i][0] + solve(i - 1, w - items[i][1])
    )
  return solve(items.length - 1, w)
```

**Time complexity**: `O(2^n)`

The time complexity is very bad. However, based on the fact that the problem has optimal substructure property, we can apply DP to optimize the time complexity of the problem using memoization.

```py
def knapsack_memoized(items, w):
  memo = {}
  def solve(i, w):
    k = (i, w)
    if k in memo: return memo[k]
    if i < 0 or w == 0: return 0
    if items[i][1] > w:
      memo[k] = solve(i - 1, w)
    else:
      memo[k] = max(
        solve(i - 1, w),
        items[i][0] + solve(i - 1, w - items[i][1])
      )
    return memo[k]
  return solve(items.length - 1, w)
```

**Time complexity**: `O(n * w)`

**Space complexity**: `O(n * w)`

Similar to the fibonacci problem, we can also use the bottom-up approach.

```py
def knapsack_dp(items, w):
  n = len(items)
  dp = [[None for _ in range(w + 1)] for _ in range(n + 1)]

  for i in range(n + 1):
    for j in range(w + 1):
      if i == 0 or j == 0: dp[i][j] = 0
      elif items[i - 1][1] > j:
        dp[i][j] = dp[i - 1][j]
      else:
        dp[i][j] = max(
          dp[i - 1][j],
          items[i - 1][0] + dp[i - 1][j - items[i - 1][1]]
        )
  return dp[n][w]
```

**Time complexity**: `O(n * w)`

**Space complexity**: `O(n * w)`

[See the full implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/9_dynamic-programming/knapsack.py)

> **Follow-up**: Can you optimize the space complexity to `O(w)`?

## 3. Longest Common Subsequence (LCS)

> Problem ([source: leetcode](https://leetcode.com/problems/longest-common-subsequence/))
> <br>
> Given two strings `text1` and `text2`, return _the length of their longest **common subsequence**_.
> <br> <br>
> If there is no **common subsequence**, return 0.
> <br> <br>
> A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
> <br>
>
> For example, `"ace"` is a subsequence of `"abcde"`.
> <br> <br>
> A **common subsequence** of two strings is a subsequence that is common to both strings.)

    Input: text1 = "abcde", text2 = "ace"
    Output: 3
    Explanation: The longest common subsequence is "ace" and its length is 3.

**Optimal Substructure**:
Suppose `m` is the length of `text1` and `n` is the length of `text2` and `result` is the LCS of `text1` and `text2`:

- If both sequences match i.e. `text1[m - 1] = text2[n - 1]` then `result = 1 + LCS(text1[0, m - 2], text2[0, n - 2])`
- If both sequences do not match i.e. `text1[m - 1] != text2[n - 1]` then `result = max(LCS(text1[0, m - 2], text2[0, n - 1]), LCS(text1[0, m - 1], text2[0, n - 2]))`

**Algorithm**:

- If either `text1` or `text2` is empty, return 0
- If `text1[0, m - 1] = text2[0, n - 1]`, return `1 + LCS(text1[0, m - 2], text2[0, n - 2])`
- Otherwise, return `max(LCS(text1[0, m - 2], text2[0, n - 1]), LCS(text1[0, m - 1], text2[0, n - 2]))`

**Implementation**:

```py
def LCS(text1, text2):
  m = len(text1)
  n = len(text2)
  if m == 0 or n == 0: return 0
  if text1[m - 1] == text2[n - 1]:
    return 1 + LCS(text1[:m - 1], text2[:n - 1])
  else:
    return max(
      LCS(text1[:m - 1], text2)
      LCS(text1, text2[:n - 1])
    )
```

**Time complexity**: `O(2^n)`

By using DP, we can optimize the time complexity down to `O(n * m)`:

```py
def LCS_DP(text1, text2):
  m = len(text1)
  n = len(text2)
  dp = [[None for _ in range(n + 1)] for _ in range(m + 1)]

  for i in range(m + 1):
    for j in range(n + 1):
      if i == 0 or j == 0: dp[i][j] = 0
      elif text1[i - 1] == text2[j - 1]:
        dp[i][j] = 1 + dp[i - 1][j - 1]
      else:
        dp[i][j] = max(
          dp[i - 1][j],
          dp[i][j - 1]
        )
  return dp[m][n]
```

**Time complexity**: `O(m * n)`

**Space complexity**: `O(m * n)`

> **Follow up**: Can you come up with a solution in `O(n)` space?

## 4. Coin Change

> Problem ([source: leetcode](https://leetcode.com/problems/coin-change-2/))
> <br>
> You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.
> <br> <br>
> Return _the number of combinations that make up that amount_. If that amount of money cannot be made up by any combination of the coins, return `0`.
> <br> <br>
> You may assume that you have an **infinite** number of each kind of coin.

    Input: amount = 5, coins = [1,2,5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1

**Optimal Substructure**:

We can observe the following about the number of coin changes:

- Solution without `coins[i] (0 <= i < coins.length)`
- Solution with `k` number of `coins[i]` (`k ∈ ℕ*`).

Based on two cases above, we can form a recursive function as following:

    dp(i, target) = dp(i - 1, target) + dp(i, target - coins[i])

**Algorithm**:

1. If `i < 0` or `target = 0`, there is one solution.
2. If `target < 0` or `i < 1` and `target > 0`, there is no solution.
3. Otherwise, sum all solutions excluding `coins[i]` and solutions including `k` times `coins[i]`

**Implementation**:

```py
def coin_change(coins, target):
  def solve(i, target):
    if i < 0 or target == 0: return 1
    if target < 0 or (i < 1 and target > 0): return 0
    return solve(i - 1, target) + solve(i, target - coins[i])
  return solve(coins.length - 1, target)
```

**Time complexity**: `O(n^target)`

By using DP, we can optimize the time complexity down to `O(n * target)`:

```py
def coin_change(coins, target):
  n = len(coins)
  dp = [[None for _ in range(n)] for _ in range(target + 1)]
  for i in range(n):
    dp[0][i] = 1

  for i in range(1, target + 1):
    for j in range(n):
      temp1 = dp[i][j - 1] if j >= 1 else 0
      temp2 = dp[i - coins[j]][j] if i - coins[j] >= 0 else 0
      dp[i][j] = temp1 + temp2
  return dp[target][n - 1]
```

**Time complexity**: `O(n * target)`

**Space complexity**: `O(n * target)`

> **Follow up**: Can you come up with a solution in `O(target)` space?

## 5. Edit Distance (Levenshtein Distance)

> Problem ([source: Leetcode](https://leetcode.com/problems/edit-distance/))
>
> Given two strings `word1` and `word2`, return _the minimum number of operations required to convert `word1` to `word2`._ <br> <br>
> You have the following three operations permitted on a word:
>
> - Insert a character
> - Delete a character
> - Replace a character

    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation:
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')

**Optimal Substructure**:

Suppose the length of `word1` and `word2` are `m` and `n` respectively.

1. If `word1[m - 1] = word2[n - 1]` then do nothing.
2. Otherwise, consider these cases recursively and see which decision gives the minimum:

   1. Insert: for `m` and `n - 1`
   2. Delete: for `m` and `n - 1`
   3. Replace: for `m - 1` and `n - 1`

**Algorithm**:

1. If `m = 0` return `n`
2. Similarly, if `n = 0` return `m`
3. If `word1[m - 1] = word2[n - 1]`, there is nothing to do, so skip by calling `solve(word1[0, m - 2], word2[0, n - 2]`)
4. Otherwise, return `1 + min(solve(word1, word2[0, n - 2], solve(word1[0, m - 2], word2), solve(word1[0, m - 2], word2[0, n - 2]))`

**Implementation**:

```py
def edit_distance(word1, word2):
  m, n = len(word1), len(word2)
  if m == 0: return n
  if n == 0: return m
  if word1[m - 1] == word2[n - 1]:
    return edit_distance(word1[:m - 1], word2[:n - 1])
  else:
    return 1 + min(
      edit_distance(word1, word2[:n - 1]),
      edit_distance(word1[:m - 1], word2),
      edit_distance(word1[:m - 1], word2[:n - 1]),
    )
```

**Time complexity**: `O(3^m)`

By using DP, we can optimize the time complexity down to `O(m * n)`:

```py
def edit_distance_dp(word1, word2):
  m, n = len(word1), len(word2)
  dp = [[None for _ in range(n + 1)] for _ in range(m + 1)]
  for i in range(m + 1):
    for j in range(n + 1):
      if i == 0: dp[i][j] = j
      elif j == 0: dp[i][j] = i
      elif word1[i - 1] == word2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1]
      else:
        dp[i][j] = 1 + min(
          dp[i][j - 1],
          dp[i - 1][j],
          dp[i - 1][j - 1]
        )
  return dp[m][n]
```

**Time complexity**: `O(m * n)`

**Space complexity**: `O(m * n)`

> **Follow up**: Can you come up with a solution that takes `O(n)` space?
