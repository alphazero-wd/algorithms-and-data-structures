# Trees

A tree is a data structure composed of nodes with children nodes. The top/first node is called the _root_.

![Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Tree_%28computer_science%29.svg/330px-Tree_%28computer_science%29.svg.png)

However, the most commonly used types of trees are _Binary Tree_ and _Binary Search Tree_. We will be discussing different ways of traversing a tree and
performing some operations on a Binary Search Tree efficiently.

**Some terminologies used in trees** (see the image above as an example):

- Root: The first/top node in the tree e.g. node `2` (circled in red). NOTE: A tree only has **one root**.
- Leaf node: a node that has no children e.g. node `5`, `11`, `4`.

## Binary Trees

A binary tree is a tree where every node holds a value `val` and has `left` and `right` children nodes.

![Binary Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Binary_tree_v2.svg/800px-Binary_tree_v2.svg.png)

From the properties mentioned above, we have a `TreeNode` class as following:

```py
class TreeNode:
  def __init__(self, val: int):
    self.val = val
    self.left = None
    self.right = None
```

We also need a class `BinaryTree` that has only a property `root`:

```py
class BinaryTree:
  def __init__(self):
    self.root = None
```

### 1. Tree Traversal

![Tree Traversal](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Sorted_binary_tree_ALL_RGB.svg/1024px-Sorted_binary_tree_ALL_RGB.svg.png)
_Pre-order (node visited at position red):_
<br>
_In-order (node visited at position green):_
<br>
_Post-order (node visited at position blue):_

<br>

1. **Inorder Traversal** (visit nodes in the following order: left, root, right)

   > In the image, the order would be `F, B, A, D, C, E, G, I, H`

2. **Preorder Traversal** (visit nodes in the following order: root, left, right)

   > In the image, the order would be `A, B, C, D, E, F, G, H, I`

3. **Postorder Traversal** (visit nodes in the following order: left, right, root)

   > In the image, the order would be `A, C, E, D, B, H, I, G, F`.

4. **Level-order Traversal** is also known as _breadth-first search_ (BFS) (visit nodes level by level)

   > In the image below, the order would be `A, C, E, D, B, H, I, G, F`.
   > <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Sorted_binary_tree_breadth-first_traversal.svg/1280px-Sorted_binary_tree_breadth-first_traversal.svg.png">

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/6_trees/BinaryTree.py)

**Time complexity**: `O(n)` where `n` is the number of nodes in a binary tree.

## Binary Search Trees

A Binary Search Tree (BST) is a binary tree where the left child is smaller than the parent and the right right child is greater than the parent.
The structure of a **balanced** BST (the first image) would enable insertion, search and deletion within `O(log(n))` time.
If the BST is **unbalanced** (the second image), it is no longer efficient and the time it takes for the operations above in worst case is `O(n)`.

![Balanced BST](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/1024px-Binary_search_tree.svg.png)

![Unbalanced BST](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Unbalanced_binary_tree.svg/1024px-Unbalanced_binary_tree.svg.png)

Because a BST is also a binary tree, so we just need to inherit all the properties of the class `BinaryTree` we have created above:

```py
class BST(BinaryTree):
  def __init__(self):
    super().__init__()
```

### 1. Search

**Idea**:

If the value we are searching for is less than the root value, we search on the left. Otherwise, we search on the right until we visit a node whose value is equal to the value we are looking for.

**Algorithm**:

1. If `root` is `null`, then `given_val` is not found so return `false`
2. If `root.val = given_val`, then return `true`.
3. If `root.val > given_val`, recursively search on `root.left`
4. Otherwise, recursively search on `root.right`

**Time complexity for balanced BSTs**: `O(log(n))`

**Time complexity for unbalanced BSTs**: `O(n)`

### 2. Insertion

**Idea**:

Same as search, if the root value is greater than the value of the node we want to insert then we traverse the left. Otherwise we look on the right subtree until we reach a `null` node and insert it.

**Algorithm**:

1. Create a new node `new_node` whose `val` is the value we want to insert
2. If `root` is `null`, then set `root` to `new_node`
3. If `root.val > given_val`

   1. If `root.left` is `null`, set `root.left` to `new_node`
   2. Else, recursively traversing `root.left`

4. Otherwise

   1. If `root.right` is `null`, set `root.right` to `new_node`
   2. Else, recursively traversing `root.right`

**Time complexity for balanced BSTs**: `O(log(n))`

**Time complexity for unbalanced BSTs**: `O(n)`

### 3. Deletion

**Idea**:

![Visualization](https://upload.wikimedia.org/wikipedia/commons/f/f3/Binary_search_tree_deletion_illustration.png)
_Binary search tree special cases deletion illustration._

We do exactly the same as search until we find the node we want to delete.
Suppose node `z` is the node we want to delete:
Then there are three cases that can happen:

- `z` is a leaf node. Set that node to `null`
- `z` has either left or right child. Set that node to either `left` or `right`, whichever one is not `null` (case a and b)
- `z` has both left and right child (case c and d). We can do the following:

  1. Find either the maximum node on the left or the minimum on the right. In this case, we find the minimum node on the right `y`
  2. Replace `z` with `y`
  3. Delete `y`, which falls into either 2 cases above like deleting `z`.

**Algorithm**:

1. Recursively search for the node we want to delete like we did in search in a BST.
2. If we find the node we want to delete, there are three cases to handle:

   1. If `node.left` is `null` and `node.right` is `null`, set `node` to `null`
   2. If `node.left` is `null`, set `node` to `node.right`
   3. If `node.right` is `null`, set `node` to `node.left`
   4. If `node.left` and `node.right` are not `null`

      1. Find the minimum node on the right of `root` by going to the most left of `root.right` and call it `right_min_node`
      2. Set `node.val` to `right_min_node.val`
      3. Recursively delete the `right_min_node`, which falls into case 1 as the `right_min_node` does not have any children.

**Time complexity for balanced BSTs**: `O(log(n))`

**Time complexity for unbalanced BSTs**: `O(n)`
