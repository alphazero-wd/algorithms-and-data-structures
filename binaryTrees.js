class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BinaryTree {
  constructor() {
    this.root = null;
  }

  inorder() {
    const inorder = (root) => {
      if (!root) return;
      inorder(root.left);
      console.log(root.value);
      inorder(root.right);
    };
    inorder(this.root);
  }

  postorder() {
    const postorder = (root) => {
      if (!root) return;
      postorder(root.left);
      postorder(root.right);
      console.log(root.value);
    };
    postorder(this.root);
  }

  preorder() {
    const preorder = (root) => {
      if (!root) return;
      preorder(root.left);
      console.log(root.value);
      preorder(root.right);
    };
    preorder(this.root);
  }

  bfs() {
    if (!this.root) return;
    const queue = [this.root];
    while (queue.length > 0) {
      const current = queue.shift();
      console.log(current.value);
      if (current.left) queue.push(current.left);
      if (current.right) queue.push(current.right);
    }
  }
}
module.exports = { TreeNode, BinaryTree };
