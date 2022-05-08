const { BinaryTree, TreeNode } = require("./binaryTrees");
class BST extends BinaryTree {
  constructor() {
    super();
  }

  // O(log(n)) for balanced trees
  // O(n) for unbalanced trees
  insert(value) {
    if (this.root === null) {
      this.root = new TreeNode(value);
      return;
    } else {
      let current = this.root;
      while (true) {
        if (value > current.value) {
          if (current.right) current = current.right;
          else {
            current.right = new TreeNode(value);
            break;
          }
        } else if (value < current.value) {
          if (current.left) current = current.left;
          else {
            current.left = new TreeNode(value);
            break;
          }
        } else break;
      }
    }
  }
  // O(log(n)) for balanced trees
  // O(n) for unbalanced trees
  remove(value) {
    return remove(this.root, value);
    function remove(root, value) {
      if (!root) return null;
      else if (root.value > value) root.left = remove(root.left, value);
      else if (root.value < value) root.right = remove(root.right, value);
      else {
        if (!root.left && !root.right) {
          root = null;
          return root;
        } else if (!root.left) {
          root = root.right;
          return root;
        } else if (!root.right) {
          root = root.left;
          return root;
        } else {
          const successor = findMin(root.right);
          root.value = successor.value;
          root.right = remove(root.right, successor.value);
          return root;
        }
      }
      return root;
    }

    function findMin(root) {
      while (root.left) root = root.left;
      return root;
    }
  }
  // O(log(n)) for balanced trees
  // O(n) for unbalanced trees
  find(value) {
    if (!this.root) return null;
    let current = this.root;
    while (current) {
      if (current.value > value) current = current.left;
      else if (current.value < value) current = current.right;
      else return true;
    }
    return false;
  }
}
