# Trees

A tree is a data structure composed of nodes with children nodes. The top/first node is called the _root_.

![Tree](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20201129105858/Tree-Basic-Terminology.png)

However, the most commonly used types of trees are _Binary Tree_ and _Binary Search Tree_. We will be discussing different ways of traversing a tree and
performing some operations on a Binary Search Tree efficiently.

**Some terminologies used in trees** (see the image above as an example):

- Root: The first/top node in the tree e.g. node `1`. NOTE: A tree only has **one root**.
- Leaf node: a node that has no children e.g. node `6`, `11`.

## Binary Trees

A binary tree is a tree where every node holds a value `val` and has `left` and `right` children nodes.

![Binary Tree](https://f4-zpcloud.zdn.vn/6649685002220047165/90be833529ace9f2b0bd.jpg)

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

1. Inorder Traversal (visit nodes in the following order: left, root, right)

![Inorder Traversal](https://f4-zpcloud.zdn.vn/1033149422736303716/babe959b4702875cde13.jpg)

2. Preorder Traversal (visit nodes in the following order: root, left, right)

![Preorder Traversal](https://f7-zpcloud.zdn.vn/2330802758405483801/9f882fe8ff713f2f6660.jpg)

3. Postorder Traversal (visit nodes in the following order: left, right, root)

![Postorder Traversal](https://f7-zpcloud.zdn.vn/3997607245947337510/89c333fef66736396f76.jpg)

4. Level-order Traversal is also known as _breadth-first search_ (BFS) (visit nodes level by level)

![Level-order Traversal](https://f4-zpcloud.zdn.vn/3688770531550857192/5b3b8b324bab8bf5d2ba.jpg)

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/6_trees/BinaryTree.py)

**Time complexity**: `O(n)` where `n` is the number of nodes in a binary tree.

## Binary Search Trees

A Binary Search Tree (BST) is a binary tree where the left child is smaller than the parent and the right right child is greater than the parent.
The structure of a **balanced** BST (the first image) would enable insertion, search and deletion within `O(log(n))` time.
If the BST is **unbalanced** (the second image), it is no longer efficient and the time it takes for the operations above in worst case is `O(n)`.

![Balanced BST](https://www.baeldung.com/wp-content/uploads/sites/4/2021/12/binary-search-tree-1024x580.jpg)

![Unbalanced BST](https://f7-zpcloud.zdn.vn/5699400827380355363/ad5f23c5d45e14004d4f.jpg)

Because a BST is also a binary tree, so we just need to inherit all the properties of the class `BinaryTree` we have created above:

```py
class BST(BinaryTree):
  def __init__(self):
    super().__init__()
```

### 1. Search

**Idea**:

If the value we are searching for is less than the root value, we search on the left. Otherwise, we search on the right until we visit a node whose value is equal to the value we are looking for.

![Search Visualization](https://miro.medium.com/max/1280/1*jm9XjZAplj5Sb6MRpMa_-Q.gif)

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

![Insertion Visualization](https://blog.penjee.com/wp-content/uploads/2015/11/binary-search-tree-insertion-animation.gif)

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

We do exactly the same as search until we find the node we want to delete.
Then there are three cases that can happen:

- The node is a leaf node. This is the easiest case as we just set that node to `null`
- The node has either left or right child. This is still easy as we just set that node to either `left` or `right`, whichever one is not `null`
- The node has both left and right child. This is a very tricky case. We can do the following:

  1. Find either the maximum node on the left or the minimum on the right
  2. Replace the node we want to delete with the node we found in step 1
  3. Delete the node we found in step 1, which falls into case 1 as the minimum node on the right is always a leaf node.

  _See the image below for case 3 visualization_

  ![Visualization](https://media.geeksforgeeks.org/wp-content/uploads/deletion-in-binary-tree.png)

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
