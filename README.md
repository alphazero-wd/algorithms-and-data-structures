# AVL Trees

## 1. Definition ([Source: Wiki](https://en.wikipedia.org/wiki/AVL_tree))

An AVL tree (named after inventors Adelson-Velsky and Landis) is a **self-balancing binary search tree** (BST). In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property. Lookup, insertion, and deletion all take `O(log(n))` time in both the average and worst cases, where `n` is the number of nodes in the tree prior to the operation. Insertions and deletions may require the tree to be rebalanced by one or more tree rotations.

In a binary tree, the _balance factor_ of a node `x` is defined to be the height difference between the left and right subtree of `x`:

    BF(x) = height(leftSubtree(x) - rightSubtree(x))

    BF(x) ∈ { -1, 0, 1 } ∀x

- `BF(x) > 0`, node `x` is called "left-heavy".
- `BF(x) < 0`, node `x` is called "right-heavy".
- `BF(x) = 0`, node `x` is called "balanced".

## 2. Implementation

### 1. Rotations

When inserting or deleting a node, the height difference between left and right subtrees might change and exceed over 1. Therefore, **rotations** are the tools to keep the tree balanced. There are 4 possible variants of the violation :

#### 1. Right Rotation

    T1, T2, T3 and T4 are subtrees.
           z                                      y
          / \                                   /   \
         y   T4      Rotate Right (z)          x      z
        / \          - - - - - - - - ->      /  \    /  \
       x   T3                               T1  T2  T3  T4
      / \
    T1   T2

Because the difference between the left and right subtree of `A` i.e. the balance factor of `z`: `BF(z) = 2 > 1`. The node `z` is considered "left heavy".

A rotation is needed, in this case, **right rotation**, which applies for the case where `z.left = y` and `y.left = x`.

```py
def rotate_right(self, z):
    y = z.left
    T2 = y.right
    y.right = z
    z.left = T2
    return y
```

**Algorithm**:

1. Set `y` to `z.left` and have a temporary variable `T3` set to `y.right` (see the visualization above).
2. Let `y.right` point to `z`
3. Let `z.left` point to `T3`

#### 2. Left Rotation

          z                                y
         /  \                            /   \
        T1   y     Rotate Left(z)       z      x
            /  \   - - - - - - - ->    / \    / \
           T2   x                     T1  T2 T3  T4
               / \
             T3  T4

Same as right rotation but this time `BF(z) = -2 < -1`, which means the node `z` is "right heavy". Therefore, we need to do a rotation called **left rotation**.

Left rotations apply for the case where `z.right = y` and `y.right = x`.

**Algorithm**:

1. Set `y` to `z.right` and have a temporary variable `T2` set to `y.left` (see the visualization above).
2. Let `y.left` point to `z`.
3. Let `z.right` point to `T2`.

**Code**:

```py
def rotate_left(z):
    y = z.right
    T3 = y.left
    y.left = z
    z.right = T3
    return y
```

#### 3. Left-Right Rotation

         z                               z                           x
        / \                            /   \                        /  \
       y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
      / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
    T1   x                          y    T3                    T1  T2 T3  T4
        / \                        / \
      T2   T3                    T1   T2

In the previous two cases, `x`, `y`, `z` are on the same side, which is either left or right.
However, this case is slightly more complicated as we need to do two rotations: one left rotation to bring back to case 1, one more right rotation to balance the AVL tree.

This rotation is called **left-right rotation**, which applies for the case where `z.left = y` and `y.right = x`.

**Algorithm**:

1. Perform a `rotate_left(y)`
2. Perform a `rotate_right(z)`

#### 3. Right-Left Rotation

        z                            z                            x
       / \                          / \                          /  \
     T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
         / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
        x   T4                      T2   y                  T1  T2  T3  T4
       / \                              /  \
     T2   T3                           T3   T4

This is a reversed case of the left-right, where `z.right = y` and `y.left = x`.

We also need another rotation called **right-left rotation** to handle this case.

**Algorithm**:

1. Perform a `rotate_right(y)`
2. Perform a `rotate_left(z)`

### 2. Search

> Searching in an AVL tree is the same as in a BST. See branch [6_trees](https://github.com/alphazero-wd/algorithms-and-data-structures/tree/6_trees) for the implementation

**Time complexity**: `O(log(n))`

### 3. Insertion

> Insert a value `val` into a BST `root`.

The first part of the insertion in an AVL tree is the same as in BST. We also need to do rotations

![Animation showing the insertion of several elements into an AVL tree. It includes left, right, left-right and right-left rotations.](https://upload.wikimedia.org/wikipedia/commons/f/fd/AVL_Tree_Example.gif)

_Animation showing the insertion of several elements into an AVL tree. It includes left, right, left-right and right-left rotations._

**Algorithm**:

1. Do the same as insertion in a BST (see branch [6_trees](https://github.com/alphazero-wd/algorithms-and-data-structures/tree/6_trees))
2. Calculate `bf(root)`
3. If `bf(root) > 1` and `val < root.left.val`, perform `rotate_right(root)`
4. If `bf(root) < -1` and `val > root.right.val`, perform `rotate_left(root)`
5. If `bf(root) > 1` and `val > root.left.val`, perform `rotate_left(root.left)` and `rotate_right(root)`
6. If `bf(root) < -1` and `val < root.right.val`, perform `rotate_right(root.right)` and `rotate_left(root)`
7. Return `root` after being updated

**Time complexity**: `O(log(n))`

### 4. Deletion

> Delete a node with a given value `val` from the BST `root`.

The first part of the deletion in an AVL tree is the same as in BST. We also need to do rotations

**Algorithm**:

1. Do the same as deletion in a BST (see branch [6_trees](https://github.com/alphazero-wd/algorithms-and-data-structures/tree/6_trees))
2. Calculate `bf(root)`
3. If `bf(root) > 1` and `bf(root.left) >= 0`, perform `rotate_right(root)`
4. If `bf(root) < -1` and `bf(root.right) <= 0`, perform `rotate_left(root)`
5. If `bf(root) > 1` and `bf(root.left) < 0`, perform `rotate_left(root.left)` and `rotate_right(root)`
6. If `bf(root) < -1` and `bf(root.right) > 0`, perform `rotate_right(root.right)` and `rotate_left(root)`
7. Return `root` after being updated

**Time complexity**: `O(log(n))`

[See the full implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/11_avl-trees/AVLTree.py)

## 3. Summary

| Operations |   Average   | Worst case  |
| :--------: | :---------: | :---------: |
|    Find    | `O(log(n))` | `O(log(n))` |
|   Search   | `O(log(n))` | `O(log(n))` |
|   Insert   | `O(log(n))` | `O(log(n))` |
|   Delete   | `O(log(n))` | `O(log(n))` |
