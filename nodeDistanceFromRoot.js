const nodeDistanceFromNode = (root, k) => {
  if (!root) return 0;
  const nodesAtKthHeight = [];
  const queue = [[root, 0]];
  while (queue.length > 0) {
    const [current, height] = queue.shift();

    if (height === k) {
      nodesAtKthHeight.push(current.value);
    }

    if (current.left) queue.push([current.left, height + 1]);
    if (current.right) queue.push([current.right, height + 1]);
  }
  return nodesAtKthHeight;
};
