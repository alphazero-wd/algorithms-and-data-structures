const invertBinaryTree = (root) => {
  if (!root) return null;

  const temp = root.left;
  root.left = root.right;
  root.right = temp;

  invertBinaryTree(root.left);
  invertBinaryTree(root.right);
};
