const pascalTriangle = (n) => {
  const result = new Array(n);
  for (let i = 0; i < n; i++) {
    result[i] = new Array(i + 1).fill(1);
  }
  for (let i = 2; i < n; i++) {
    for (let j = 1; j < result[i].length; j++) {
      const num = solve(i, j);
      result[i][j] = num;
    }
  }

  return result;
};

const solve = (row, col) => {
  if (col === 0) return 1;
  if (row === 0) return 0;
  return solve(row - 1, col - 1) + solve(row - 1, col);
};

const triangle = pascalTriangle(6);
console.log(triangle);
