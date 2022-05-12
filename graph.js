class Graph {
  constructor() {
    this.adjList = {};
  }

  // V = number of vertices/nodes; E = number of adjList in a graph
  // Time complexity: O(V + E)
  dfs(u, visited = new Set()) {
    visited.add(u[0]);
    console.log(u[0]);
    for (let v of this.adjList[u]) {
      if (!visited.has(v[0])) this.dfs(v[0], visited);
    }
  }

  // Time complexity: O(V + E)
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

  // Time complexity: O(V^2 + E)
  dijkstra(source) {
    // create vertex set Q
    const Q = new Set(),
      dist = {};
    function extractMin() {
      let minimumDistance = Infinity,
        nodeWithMinimumDistance = null;
      for (var node of Q) {
        if (dist[node] <= minimumDistance) {
          minimumDistance = dist[node];
          nodeWithMinimumDistance = node;
        }
      }
      return nodeWithMinimumDistance;
    }
    for (let vertex in this.adjList) {
      // unknown distances set to Infinity
      dist[vertex] = Infinity;
      // add v to Q
      Q.add(vertex);
    }
    // Distance from source to source init to 0
    dist[source] = 0;

    while (Q.size > 0) {
      var u = extractMin(Q, dist); // get the min distance

      // remove u from Q
      Q.delete(u);

      // for each neighbor, v, of u:
      // where v is still in Q.
      for (let neighbor of this.adjList[u]) {
        const [v, w] = neighbor;
        let alt = dist[u] + w;
        if (alt < dist[v]) {
          dist[v] = alt;
        }
      }
    }
    return dist;
  }

  // Time complexity: O(V + E)
  topologicalSort() {
    const visited = new Set(),
      stack = [];
    function topologicalSortUtil(v, adjList) {
      visited.add(v);
      for (let item of adjList[v]) {
        if (!visited.has(item[0])) topologicalSortUtil(item[0], adjList);
      }
      stack.unshift(v);
    }
    for (let item in this.adjList) {
      if (!visited.has(item)) topologicalSortUtil(item, this.adjList);
    }
    return stack;
  }
}

module.exports = Graph;
