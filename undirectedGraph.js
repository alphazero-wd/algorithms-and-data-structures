const Graph = require("./graph");

class UndirectedGraph extends Graph {
  constructor() {
    super();
  }

  addEdges(u, v, weight = 0) {
    if (!this.adjList[u]) this.adjList[u] = [];
    if (!this.adjList[v]) this.adjList[v] = [];
    this.adjList[u].push([v, weight]);
    this.adjList[v].push([u, weight]);
  }
}
