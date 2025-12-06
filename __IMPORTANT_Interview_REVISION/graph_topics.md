Here’s a compact checklist you can treat like a training montage before diving into LeetCode graph hell:

**Foundations**

* Representations: adjacency list, adjacency matrix
* Directed vs undirected, weighted vs unweighted
* Graph traversal boilerplate: visited, queue, recursion stack

**Core Algorithms**

* BFS: traversal + shortest path in unweighted graphs
* DFS: traversal, connected components, cycle detection
* Topological sort: Kahn’s algorithm + DFS version
* Dijkstra’s algorithm: shortest path with non-negative weights
* Union-Find (Disjoint Set Union): union, find, path compression
* Minimum Spanning Tree: Prim + Kruskal (with DSU)

**Core Problem Patterns**

* Connected components counting
* Cycle detection (directed + undirected)
* Bipartite graph check (2-coloring)
* Shortest path in grids/graphs
* Cloning/Copying graphs
* Course schedule / dependency ordering
* Flood fill / island counting

**Implementation Skills**

* Build graph from edge list
* Efficient use of queues, stacks, priority queues
* Recursion pitfalls (stack overflow)
* Handling large inputs / performance thinking

**Stretch Topics (optional but nice)**

* Bellman-Ford (negative weights)
* Floyd-Warshall (all pairs shortest paths)

Working through these gives you 90% coverage of interview-grade graph problems.


Graphs are basically friendship charts between nodes, and computers need a data structure to remember who hangs out with whom. Two classic ways to do it are:

---

## 1. Adjacency List

This stores, for each node, the list of nodes it is connected to.
It’s like "Alice: Bob, Charlie", "Bob: Alice", etc.

In JavaScript, the easiest mental model is a `Map` or plain object where keys are nodes and values are arrays.

### Example (Undirected graph)

```js
// Graph: 1 - 2, 1 - 3, 2 - 4
const graph = {
  1: [2, 3],
  2: [1, 4],
  3: [1],
  4: [2]
};

// iterate neighbors of 1
for (const neighbor of graph[1]) {
  console.log(neighbor);
}
```

### Using Map (cleaner when nodes are not simple strings)

```js
const graph = new Map();

graph.set(1, [2, 3]);
graph.set(2, [1, 4]);
graph.set(3, [1]);
graph.set(4, [2]);

console.log(graph.get(1)); // [2, 3]
```

### Add edge function

```js
function addEdge(g, u, v) {
  if (!g.has(u)) g.set(u, []);
  if (!g.has(v)) g.set(v, []);
  g.get(u).push(v);
  g.get(v).push(u); // remove for directed graph
}
```

Adjacency list is compact, good for sparse graphs, and very friendly for BFS/DFS.

---

## 2. Adjacency Matrix

This keeps a 2D array of 0/1 (or weights) indicating if an edge exists between nodes.
Think of it as a table. Matrix[i][j] = 1 means node i connects to j.

### Example (Undirected, unweighted)

Nodes 1–4, represented as 0–3 indexes.

```js
const n = 4;
const matrix = Array.from({ length: n }, () => Array(n).fill(0));

// add edges
function addEdge(i, j) {
  matrix[i][j] = 1;
  matrix[j][i] = 1; // remove for directed graph
}

addEdge(0, 1);
addEdge(0, 2);
addEdge(1, 3);

console.log(matrix);
```

Matrix ends up like:

```
[
  [0,1,1,0],
  [1,0,0,1],
  [1,0,0,0],
  [0,1,0,0]
]
```

Matrix is good when:

* graph is dense
* fast edge lookup matters (`O(1)` check if edge exists)
* you need matrix operations (e.g., in algorithms class)

Bad when graph is large and sparse, because memory is quadratic.

---

## Differences in vibe

Adjacency list is like a lazy person who only remembers relevant friends.
Adjacency matrix is a paranoid accountant who writes down every possible relationship, even if it's empty.

---

## Quick “interview brain” notes

* List: `O(V + E)` space, good for traversal
* Matrix: `O(V^2)` space, fast edge lookup
* List is default choice in coding interviews unless the problem screams matrix

Graphs in JavaScript are basically DIY Lego models: you choose how fancy the bricks are depending on what you want to build next.

Graphs come in a few personality types, and they dramatically change how algorithms behave. Let’s break the archetypes down without performing a boring taxonomy ritual.

---

## Directed vs Undirected

Directed edges have a direction.
Node A points to B, but B doesn’t necessarily point back.
Undirected edges don’t care about orientation—A and B mutually acknowledge each other’s existence.

In an **undirected graph**, the edge `(u, v)` implicitly means `(v, u)` too.
In a **directed graph**, `(u, v)` is a one-way street.

Imagine people:

* Undirected: mutual friendship.
* Directed: one-sided crush.

### Representation consequences

Adjacency list:

Undirected:

```js
graph[u].push(v);
graph[v].push(u);
```

Directed:

```js
graph[u].push(v);
```

Adjacency matrix:

Undirected: matrix is symmetric.
Directed: matrix can look like a drunken Tetris board, asymmetric all over the place.

### Algorithm behaviors

Traversal (BFS/DFS) still works fine, just follow directions.
But directed graphs spawn exotic creatures:

* Strongly connected components
* Topological sorting
* Directed cycles

Undirected graphs have simpler connectivity structure.

---

## Weighted vs Unweighted

Edges may have costs attached.
Unweighted graphs are just "exists or doesn’t exist".
Weighted graphs say “going from A to B costs W.”

Think of a road network:

* Unweighted: each road takes exactly one unit of effort—teleport highways.
* Weighted: roads have length, toll, or existential frustration level.

Representation:

Adjacency list (weighted):

```js
graph[u].push({ node: v, weight: w });
```

Adjacency list (unweighted):

```js
graph[u].push(v);
```

Matrix (weighted):

* Instead of 0/1, you store numbers or `Infinity` for "no edge".

```js
matrix[u][v] = w;
```

### Algorithmic implications

Unweighted shortest path:

* BFS works in linear time, and gracefully ignores weights because they don’t exist.

Weighted shortest path:

* You summon fancier algorithms:

  * Dijkstra (non-negative weights)
  * Bellman-Ford (negative weights allowed, potential unicorn tears)
  * Floyd–Warshall (all-pairs, cubic time, CPU cry-fest)

Weighted graphs also give birth to Minimum Spanning Tree problems (Kruskal, Prim), though MST is usually on undirected weighted graphs.

---

## Mix-and-match weirdness

Graphs aren’t limited to one checkbox.

Examples:

* Directed + weighted: flight routes with ticket prices.
* Undirected + weighted: road map with distances.
* Directed + unweighted: dependency graph.
* Undirected + unweighted: friendship network.

Real world usually leans weighted. Interview problems often don’t, because implementing Dijkstra under pressure is like solving calculus while juggling ferrets.

---

## Tiny JavaScript example of a directed weighted graph

```js
const graph = new Map();

function addEdge(u, v, w) {
  if (!graph.has(u)) graph.set(u, []);
  graph.get(u).push({ node: v, weight: w });
}

addEdge('A', 'B', 5);
addEdge('A', 'C', 2);
addEdge('C', 'D', 1);
```

---

Graphs have the delightful property of being simple in definition but chaotic in flavor: a small decision—arrow directions, weight labels—spawns a zoo of algorithms and behaviors. If one stares too long, one starts seeing networks everywhere: social groups, neuronal circuits, gossip chains, cosmic filaments, and the wiring behind a terrible dating app.
