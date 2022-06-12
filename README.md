# Graph

## Introduction to Graphs

### 1. Definition

A **graph** is a **non-linear data structure** consisting of nodes (vertices) and edges. Edges are lines that connect any two vertices in a graph.

![Graph](https://www.geeksforgeeks.org/wp-content/uploads/undirectedgraph.png)

In the image above, the set of vertices is `V = { 0, 1, 2, 3, 4 }` and the set of edges is `E = { 0-1, 1-2, 1-3, 1-4, 0-4, 3-4 }`

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

![Two examples of graphs](https://f5-zpcloud.zdn.vn/203888782971244562/4f493bb3af176f493606.jpg)

**Some graph terminologies** (see the image above):

- _Vertex_ (`V` for Big-O analysis): In the image above, vertices are A, B, C, D, E.
- _Edge_ (`E` for Big-O analysis) is a connection i.e. line between any two vertices e.g. A-B, B-C, D-E
- _Degree_ of vertex is the number of edges on a vertex e.g. In the undirected graph, node C has a degree of 3 as there are 3 edges on C.
- _Sparse Graph_ is a graph where there are **a few connections** between vertices (see the image below).

![Sparse Graph](https://f4-zpcloud.zdn.vn/4281416261235602009/ce6096430ee7ceb997f6.jpg)

- _Dense Graph_ is a graph where there are **a lot of connections** between vertices (see the image below).

![Sparse Graph](https://f5-zpcloud.zdn.vn/8484809617237858085/559309a59301535f0a10.jpg)

- _Cyclical Graph_ is a **directed graph** where there is a vertex that travels from and back to itself.
  In the image below, B can follow an edge to C, D, E and back to B again.

![Graph with a cycle on B](https://f4-zpcloud.zdn.vn/2174628740394335079/54ae4b5eccfa0ca455eb.jpg)

In constrast, if we remove the edge from node D to E, the graph would no longer be a cyclical graph.

![Graph without a cycle](https://f7-zpcloud.zdn.vn/7031975612525241153/e880e9fd6459a407fd48.jpg)

- _Weights_ are used to signify various things e.g. distance, cost, etc. depends on the context. For example, the distance to get from one vertex to another, as shown in the image below:

![Directed graph with weights](https://f6-zpcloud.zdn.vn/8759161994293116278/2342b97b1edfde8187ce.jpg)

### 2. Graph Representation

There are different ways to represent graphs. Two most common ways of doing this are using **adjacency matrix** and **adjacency list**.

1. Adjacency List Representation: by using a hash table data structure we have learned. The keys will be the vertices, the values are arrays of neighbors of each vertex.
2. Adjacency Matrix Representation: by using a 2D array. If there is an edge between vertex `u` and `v`, we label `matrix[u][v] = 1`

![Graph (left), adjacency list (middle), and adjacency matrix (right)](https://f4-zpcloud.zdn.vn/4599104860191815490/34c8dabdc61a06445f0b.jpg)

## Undirected Graphs

An undirected graph is a graph where there are **no directions** between edges.

> An example of which are the roads where a person can travel from road A to road B, while also can travel from road B to road A.

![An Undirected Graph](https://f4-zpcloud.zdn.vn/7047462688418844196/c7cd7fc8996c5932007d.jpg)
