# Core Concepts: Trees

## 1. What is a Tree?
- A hierarchical data structure made of **nodes** and **edges**.
- Has a single starting point called the **root**.
- Each node can have child nodes, but every child has exactly **one parent**.
- This "one parent" rule prevents cycles.

## 2. Common Tree Types
- **Binary Tree (BT):** A tree where each node has at most **two children** (a `left` child and a `right` child).
- **Binary Search Tree (BST):** A special, ordered Binary Tree. For any given node:
    - All values in the **left subtree** are **less than** the node's value.
    - All values in the **right subtree** are **greater than** the node's value.
- **Self-Balancing BSTs (e.g., AVL, Red-Black Trees):** These are BSTs that automatically adjust their structure (using "rotations") to stay balanced. This guarantees that operations like search, insert, and delete remain very fast, typically $O(\log n)$.


# Core Concepts: Tree Terminology

- **Root:** The top-most node of a tree.
- **Node:** A single entity in the tree that holds a value.
- **Edge:** The connection between two nodes.
- **Parent:** A node that has a connection to a node below it.
- **Child:** A node that has a connection from a node above it.
- **Leaf:** A node with zero children.
- **Subtree:** A portion of the tree that can be considered a complete tree in itself (a node and all its descendants).
- **Depth of a Node:** The number of edges from the root to the node. (Root's depth is 0).
- **Height of a Tree:** The number of edges in the longest path from the root to a leaf.