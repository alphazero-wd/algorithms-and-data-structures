const lowestCommonAncestor = (root, p, q) => {
  // solution:
  // if the max between p and q < root value then search on the left
  // if the max between p and q > root value then search on the right
  function findLCA(root, p, q) {
    if (!root) return null;
    if (Math.max(p, q) < root.value) {
      return findLCA(root.left, p, q);
    }

    if (Math.min(p, q) > root.value) {
      return findLCA(root.right, p, q);
    }
    return root.value;
  }
  return findLCA(root, p, q);
};
