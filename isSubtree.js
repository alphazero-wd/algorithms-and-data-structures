const isSubtree = (root, subroot) => {
  // solution:
  // do bfs on the main tree
  // at any point, check if a subtree in the main tree is the same as the given subtree
  const queue = [root];
  while (queue.length > 0) {
    const current = queue.shift();
    if (current.value === subroot.value && isSameTree(current, subroot))
      return true;
    if (current.left) queue.push(current.left);
    if (current.right) queue.push(current.right);
  }
  return false;
};

const isSameTree = (root1, root2) => {
  if (!root1 && !root2) return true;
  if (!root1 || !root2) return false;

  return (
    root1.value === root2.value &&
    isSameTree(root1.left, root2.left) &&
    isSameTree(root1.right, root2.right)
  );
};
