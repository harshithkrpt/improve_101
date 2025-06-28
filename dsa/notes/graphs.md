# Graphs

- has two parts 
    1. vertices or nodes 
    2. edges
- has bidirectional flow and directed flow
- we can represent graph using adjacent list and adjacent matrixes

## Graph Representation using adjacent list

```python
from collections import defaultdict

class Graph:
    def __init__(self):
        """
        Initializes the graph using a defaultdict with a list as the default factory.
        This means if you access a key that doesn't exist, it will be created with an empty list.
        """
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        Adds an edge between u and v for an undirected graph.
        We add v to u's list and u to v's list.
        """
        self.graph[u].append(v)
        self.graph[v].append(u)

    def print_graph(self):
        """
        Prints the adjacency list representation of the graph.
        """
        print("Adjacency List:")
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {neighbors}")

# --- Let's build the social network graph ---

# Create a graph instance
social_network = Graph()

# Add the edges based on our example
# Anna is friends with Bob and Casey
social_network.add_edge('Anna', 'Bob')
social_network.add_edge('Anna', 'Casey')
# Casey is also friends with David
social_network.add_edge('Casey', 'David')

# Print the graph to see the result
social_network.print_graph()
```

## Graph Representation using adjacent matrix

Instead of a list of neighbors, an Adjacency Matrix uses a 2D grid (like a spreadsheet) of 0s and 1s.

| Feature               | Adjacency List                | Adjacency Matrix            |
|-----------------------|-------------------------------|-----------------------------|
| **Space Complexity**  | O(V + E)                      | O(V²)                       |
| **Why?**              | Only stores existing edges. Great for sparse graphs. | Stores all possible pairs, even if no edge. Wastes space for sparse graphs. |
| **Check Edge (u, v)** | O(k), where k = # of neighbors of u | O(1)                       |
| **Why?**              | Must scan u's neighbor list for v. | Direct index lookup: matrix[u][v]. Fastest check. |
| **Get All Neighbors(u)** | O(k), where k = # of neighbors of u | O(V)                   |
| **Why?**              | Directly grab u's list. Fast. | Must scan full row for 1s (neighbors).           |
| **Add/Remove Edge**   | O(1) on average               | O(1)                        |
| **Why?**              | Appending/removing from list is fast. | Matrix value update is constant time.         |
