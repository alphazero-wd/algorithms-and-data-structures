class Graph {
  constructor() {
    this.adjList = {};
  }

  dfs(u, visited = new Set()) {
    visited.add(u[0]);
    console.log(u[0]);
    for (let v of this.adjList[u]) {
      if (!visited.has(v[0])) this.dfs(v[0], visited);
    }
  }

  bfs(src) {
    const visited = new Set();
    const queue = [];
    queue.push(src);

    while (queue.length > 0) {
      const u = queue.shift();
      if (!visited.has(u)) {
        visited.add(u);
        console.log(u[0]);
        for (let v of this.adjList[u]) {
          queue.push(v[0]);
        }
      }
    }
  }
}
module.exports = Graph;
