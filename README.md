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
