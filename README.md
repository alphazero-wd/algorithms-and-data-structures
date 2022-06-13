# Graph

## Introduction to Graphs

### 1. Definition

A **graph** is a **non-linear data structure** consisting of nodes (vertices) and edges. Edges are lines that connect any two vertices in a graph.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/1280px-6n-graf.svg.png" width="30%" />

In the image above, the set of vertices is `V = { 1, 2, 3, 4, 5, 6 }` and the set of edges is `E = { 1-2, 1-5, 2-3, 2-5, 3-4, 4-5, 4-6 }`

Graphs are visual representations of the connections between objects. Such representations can be seen anywhere in real life and have various applications.
Here are some examples:

| Application  | Item         | Connection              |
| ------------ | ------------ | ----------------------- |
| Web site     | Web page     | Links                   |
| Map          | Intersection | Road                    |
| Circuit      | Component    | Wiring                  |
| Social media | Person       | “Friendship”/connection |
| Telephone    | Phone number | Landline                |

There are two main types of graphs: **undirected graph** (on the left) and **directed graph** (on the right):

**Some graph terminologies** (see the image above):

- _Vertex_ (`V` for Big-O analysis): In the image above, vertices are A, B, C, D, E.
- _Edge_ (`E` for Big-O analysis) is a connection i.e. line between any two vertices e.g. A-B, B-C, D-E
- _Degree_ of vertex is the number of edges on a vertex e.g. In the undirected graph, node C has a degree of 3 as there are 3 edges on C.
- _Sparse Graph_ is a graph where there are **a few connections** between vertices.

- _Dense Graph_ is a graph where there are **a lot of connections** between vertices.

- _Cycle Graph_ is a **directed graph** where there is a vertex that travels from and back to itself.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Undirected_6_cycle.svg/240px-Undirected_6_cycle.svg.png">

- _Weights_ are used to signify various things e.g. distance, cost, etc. depends on the context. For example, the distance to get from one vertex to another, as shown in the image below:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Weighted_network.svg/1920px-Weighted_network.svg.png" width="50%" />

### 2. Graph Representation

There are different ways to represent graphs. Two most common ways of doing this are using **adjacency matrix** and **adjacency list**.

1. Adjacency List Representation: by using a hash table data structure we have learned. The keys will be the vertices, the values are arrays of neighbors of each vertex.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Simple_cycle_graph.svg/1024px-Simple_cycle_graph.svg.png" width="25%" />

_A sample graph_

<table>
  <thead>
    <th colspan="3">The graph pictured above has this adjacency list representation:</th>
  </thead>
  <tbody>
  <tr>
    <td>a</td>
    <td>adjacent to</td>
    <td>b, c</td>
  </tr>
  <tr>
    <td>b</td>
    <td>adjacent to</td>
    <td>a, c</td>
  </tr>
  <tr>
    <td>c</td>
    <td>adjacent to</td>
    <td>a, b</td>
  </tr>
  <tbody>
</table>

> Throughout the discussion, adjacency list representation of graphs will be used because it is much more efficient in terms of time and space complexity for searching.

```py
from typing import List, Dict
class Graph:
  def __init__(self) -> None:
    self.adj_list: Dict[int, List[List[int]]] = {}
```

2. Adjacency Matrix Representation: by using a 2D array. If there is an edge between vertex `u` and `v`, we label `matrix[u][v] = 1`

<div>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/6n-graph2.svg/300px-6n-graph2.svg.png" width="25%" />

_A sample graph_

</div>
<div>
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/a773011024de5e3cbe8da03e97c79e1fe3101937" />

_Coordinates are 1-6_

</div>

## Undirected Graphs

An undirected graph is a graph where there are **no directions** between edges.

> An example of which are the roads where a person can travel from road A to road B, while also can travel from road B to road A.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Undirected.svg/1024px-Undirected.svg.png" width="25%" />

**Add Edge**:

Suppose we have an adjacency list `adjList` and we want to add an edge between vertex `u` and `v` to `adjList`.

1.  If either `u` or `v` is not in `adjList`, we will initialize `adjList[u]` or `adjList[v]` to an empty list
2.  Otherwise, we add `u` to `adjList[v]` to indicate a direction from `v` to `u`, and add `v` to `adjList[u]` to indicate a direction from `u` to `v`.

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/8_graphs/UndirectedGraph.py)

## Directed Graphs (Digraphs)

A directed graph is a graph where there are **directions** between edges.

> An example of which is course scheduling where if you want to take a course, you must finish prerequisites of that course first. Similarly, if you want to complete the prerequisites of that course, you would have to finish the prerequisites of prerequisites of that course.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Directed.svg/1024px-Directed.svg.png" width="25%" />

**Add Edge**:

Suppose we have an adjacency list `adjList` and we want to add an edge **from vertex `u` to `v`** to `adjList`.

1.  Same as undirected graph, if either `u` or `v` is not in `adjList`, we will initialize `adjList[u]` or `adjList[v]` to an empty list
2.  Otherwise, we only add `v` to `adjList[u]` to indicate there is an only direction from `u` to `v`.

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/8_graphs/DirectedGraph.py)

## Graph Searching Algorithm

### 1. Depth-first Search (DFS)

The first basic graph searching algorithm is depth-first search. As the name suggests, the algorithm starts at an arbitrary vertex in a graph and explores as far as possible along each branch before backtracking. DFS works for both undirected and directed graph.

![Visualization](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif)

The only problem in DFS is to deal with cycle as it can result in an infinite loop. Therefore, we need to use a **set** `visited` to keep track of visited nodes so we do not visit it one more time.

**Algorithm**:

1. Start at an arbitrary node and call it `u`.
2. Add `u` to `visited`
3. Check every `neighbor` of `u`. If `neighbor` is not in the `visited` set, recursively visit `neighbor`

**Time complexity**: `O(V + E)`

### 2. Breadth-first Search (BFS)

Breadth-first search is another graph searching algorithm. Unlike DFS, it explores every vertex at the present depth instead of visiting nodes at the next depth level.
DFS uses the underlying call stack, while BFS uses a queue. We also need a `visited` set to keep track of explored vertices.

![Visualization](https://upload.wikimedia.org/wikipedia/commons/4/46/Animated_BFS.gif)

**Algorithm**:

1. Start at an arbitrary node and call it `u`.
2. Initialize a queue `q` and add `u` to `q`.
3. Add `u` to `visited`
4. If `q` is not empty

   1. Dequeue `q` to get a vertex `v`
   2. Add `v` to `visited`
   3. Check every `neighbor` of `v`. If `neighbor` is not in `visited`, add `neighbor` to `q`

**Time complexity**: `O(V + E)`

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/8_graphs/GraphSearch.py)

## 3. Connected Components (CCs)

### 1. Definition

A **connected component (CC)** is a maximal set of connected vertices.

![CC](https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Pseudoforest.svg/360px-Pseudoforest.svg.png)

_A graph with 3 connected components_

### 2. Implementation

This is a problem where DFS is used to count the number of CCs in a graph. We check every single vertex in a graph, if it is not visited then visit all the neighbors of that vertex.
After visiting all the neighbors in a CC, we add 1 to the total number of CCs. Then visit the next CC.

**Algorithm**:

1. Initialize `count` to 0, which is the number of CCs in a graph.
2. Go through every vertex `u` in `adjList`, if `u` is not in `visited`, call `dfs(u)`
3. Increment `count` by 1 after the DFS
4. Repeat step 2 and 3

## 4. Topological Sort

### 1. Definition

A topological sort or topological ordering of a **directed acyclic graph (DAG)** (a directed graph with no cycle) is a linear ordering of its vertices such that for every directed edge `uv` from vertex `u` to vertex `v`, `u` comes before `v` in the ordering.

> Suppose each vertex is each course that has to be completed. For example, if we want to finish course 9 then we first have to complete course 8 and course 11. Similarly, if we want to finish course 8 and 11, we would have to complete course 5, 7 and 3. Same applies for other courses.
> <br>
> Therefore, the topological order would be `[5, 7, 3, 11, 8, 2, 9, 10]`. <br> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Directed_acyclic_graph_2.svg/458px-Directed_acyclic_graph_2.svg.png" width="25%" > <br> _A sample graph_

### 2. Implementation

We do the same thing like we do in DFS. Except for the fact we will need a **stack** to store the topological order of a graph and reverse it.

**Algorithm**:

1. Initialize a stack `st` to store the topological ordering
2. Check every vertex `u` in the graph. If `u` not in `visited`, call `dfs(u)`
3. At the end of `dfs(u)`, push `u` to `st`
4. Reverse `st` to get the topological order.

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/8_graphs/TopologicalSort.py)

**Time complexity**: `O(V + E)`

## 5. Strongly Connected Components (SCCs)

### 1. Definition

A **strongly connected component (SCC)** is a maximal set of vertices in a directed graph where at any two vertices `u` and `v`, there is a directed path from `u` to `v` and from `v` to `u`.

<img width="50%" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Scc-1.svg/330px-Scc-1.svg.png">

_There are 3 SCCs highlighted_

**Idea**: Kosaraju-Sharir Algorithm

- SCCs in the original graph `G` are the same as in the reversed graph `Gr`.
- Compute the topological order of `Gr`
- Run DFS on the original graph `G`

**Algorithm**:

1. Initialize a variable `count` to compute the number of SCCs in a graph.
1. Reverse (transpose) the graph `G` to get the reversed graph `Gr`
1. Compute the topological order `rev_topo` of `Gr`
1. Check every vertex `u` in the `rev_topo`. If `u` is not in `visited`, call `dfs(u)`
1. Increment `count` by 1 after a traversal.

[See the implementation here](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/8_graphs/KosarajuSharirSCC.py)

**Time complexity**: `O(V + E)`

## 6. Dijkstra Algorithm

Dijkstra Algorithm is used to find the shortest path from the source vertex `s` to other vertices in a graph.

**Algorithm**:

1. Initialize a hash map `dist` which stores keys as vertices and values as the distance from `s` to any vertex in the graph, and a set `Q`.
2. Set `dist[s]` to 0 and `dist[other nodes]` to infinity.
3. Add all the vertices in the graph to `Q`
4. If `Q` is not empty, find the vertex `u` whose distance from `s` is the minimum and remove `u` from `Q`
5. Check every `neighbor` of `u`. Update the shortest path from `u` to `neighbor` if the shortest path to `neighbor` is greater than the sum of shortest path to `u` and the distance between `u` and `neighbor`: `dist[neighbor] = min(dist[neighbor], dist[u] + weight(u, neighbor))`

![Dijkstra Algorithm](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif)

**Time complexity**: `O(V^2 + E)`

> The time complexity can be optimized using a min-heap because getting the minimum vertex will take `O(log(n))` only. Therefore, the total time complexity for the algorithm is `O((E + V) * log(V))`

[See the implementation using set](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/8_graphs/Dijkstra.py)

[See the implementation using min-heap](https://github.com/alphazero-wd/algorithms-and-data-structures/blob/8_graphs/DijkstraHeap.py)
