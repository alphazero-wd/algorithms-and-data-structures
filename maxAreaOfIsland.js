const maxAreaOfIsland = (grid) => {
  let maxArea = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === 1) {
        let area = dfs(grid, i, j);
        maxArea = Math.max(maxArea, area);
      }
    }
  }
  console.log("grid", grid);
  return maxArea;
};

const dfs = (grid, row, col) => {
  if (
    row < 0 ||
    col < 0 ||
    col >= grid[0].length ||
    row >= grid.length ||
    grid[row][col] !== 1
  )
    return 0;
  grid[row][col] = 0;
  return (
    1 +
    dfs(grid, row - 1, col) +
    dfs(grid, row + 1, col) +
    dfs(grid, row, col - 1) +
    dfs(grid, row, col + 1)
  );
};