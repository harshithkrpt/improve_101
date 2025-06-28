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


## Breath First Traversal Python Code

```python
from collections import deque
def bfs(graph, start_node):
    if start_node not in graph:
        return []
    queue = deque([start_node])
    visited = {start_node}
    traversal_order = []

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order

social_graph = {
  'Anna': ['Bob', 'Casey'],
  'Bob': ['Anna'],
  'Casey': ['Anna', 'David'],
  'David': ['Casey']
}

# Call the function starting from 'Anna'
visited_nodes = bfs(social_graph, 'Anna')
print(f"BFS traversal starting from Anna: {visited_nodes}")

# Call the function starting from 'David'
visited_nodes_from_david = bfs(social_graph, 'David')
print(f"BFS traversal starting from David: {visited_nodes_from_david}")
```


## Depth First Traversal Python Code

```python
def dfs_recursive(graph, start_node):
    visited = set()
    traversal_order = []

    def _dfs_helper(node):
        visited.add(node)
        traversal_order.append(node)

        for n in graph[node]:
            if n not in visited:
                _dfs_helper(n)
    _dfs_helper(start_node)
    return traversal_order

social_graph = {
  'Anna': ['Bob', 'Casey'],  # Note the order: Bob is first
  'Bob': ['Anna'],
  'Casey': ['Anna', 'David'],
  'David': ['Casey']
}

# Call the function starting from 'Anna'
visited_nodes = dfs_recursive(social_graph, 'Anna')
print(f"Recursive DFS traversal starting from Anna: {visited_nodes}")
```