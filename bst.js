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
  deletefromBST(value) {
    const deletefromBST = (root, value) => {
      if (root === null) return null;
      else if (root.val > value) root.left = deletefromBST(root.left, value);
      else if (root.val < value) root.right = deletefromBST(root.right, value);
      else {
        if (!root.left && !root.right) return null;
        else if (!root.left) {
          root = root.right;
          return root;
        } else if (!root.right) {
          root = root.left;
          return root;
        } else {
          const deleteNode = findMin(root.right);
          root.value = deleteNode.value;
          root.right = deletefromBST(root.right, deleteNode.value);
          return root;
        }
      }
      return root;
    };
    const findMin = (root) => {
      while (root.left) root = root.left;
      return root;
    };
    return deletefromBST(this.root, value);
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
