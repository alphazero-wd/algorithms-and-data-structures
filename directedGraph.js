const Graph = require("./graph");

class DirectedGraph extends Graph {
  constructor() {
    super();
  }

  addEdge(u, v, weight = 0) {
    if (!this.adjList[u]) this.adjList[u] = [];
    if (!this.adjList[v]) this.adjList[v] = [];
    this.adjList[u].push([v, weight]);
  }
}
