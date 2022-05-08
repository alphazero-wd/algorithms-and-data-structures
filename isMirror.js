const isMirrorTree = (root1, root2) => {
  // solution:
  // check if every node of the left subtree of root1 = every node of the right subtree of root2
  if (!root1 && !root2) return true;
  if (!root1 || !root2) return false;

  return (
    root1.value === root2.value &&
    isMirrorTree(root1.left, root2.right) &&
    isMirrorTree(root1.right, root2.left)
  );
};
