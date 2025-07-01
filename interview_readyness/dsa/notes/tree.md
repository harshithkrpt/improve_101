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


## Core Concepts: Tree Terminology

- **Root:** The top-most node of a tree.
- **Node:** A single entity in the tree that holds a value.
- **Edge:** The connection between two nodes.
- **Parent:** A node that has a connection to a node below it.
- **Child:** A node that has a connection from a node above it.
- **Leaf:** A node with zero children.
- **Subtree:** A portion of the tree that can be considered a complete tree in itself (a node and all its descendants).
- **Depth of a Node:** The number of edges from the root to the node. (Root's depth is 0).
- **Height of a Tree:** The number of edges in the longest path from the root to a leaf.

## Core Concepts: Trees vs. Graphs

- A **Tree** is a special, restricted type of **Graph**.
- **Key Differences:**
  - **Cycles:** Trees **cannot** have cycles. Graphs **can**.
  - **Root:** Trees have **one root**. Graphs have **no concept of a root**.
  - **Paths:** There is only **one unique path** between any two nodes in a tree. Graphs can have multiple paths.
  - **Analogy:** A Tree is a hierarchical org chart. A Graph is a social network or a city map.


## Core Concepts: Tree Representation in Python

- Trees are represented by defining a `Node` class.
- For Binary Trees, the node contains the value and pointers to `left` and `right` children.

## Standard TreeNode Class

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # The value of the node
        self.left = left    # A pointer to the left child (another TreeNode)
        self.right = right  # A pointer to the right child (another TreeNode)

# Tree structure to build:
#      10
#     /  \
#    5    15

# 1. Create the nodes
root = TreeNode(10)
node5 = TreeNode(5)
node15 = TreeNode(15)

# 2. Link them together
root.left = node5
root.right = node15

```
## Tree Traversals: Preorder (DFS)

- **Order:** Root -> Left -> Right
- **Mnemonic:** Process the current node **Pre** (before) its children.
- **Use Case:** Useful for creating a copy of a tree, or when you need to process the root node before its descendants (e.g., in some expression trees).

## Recustive solution

```python
    def preorder_traversal(root):
        result = []
        if root:
            result.append(root.val)
            result.extend(preorder_traversal(root.left))
            result.extend(preorder_traversal(root.right))
        return result

```

## Iterative solution using stack

```python
    def preorder_traversal_iterative(root):
        if not root:
            return []
        
        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.push(node.val)
            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)

        return result
```

## Inorder Traversal (Left -> Root -> Right)

This is another flavor of DFS. The key difference is the order in which you visit the root.

    - Traverse the Left subtree.
    - Visit the Root node.
    - Traverse the Right subtree.

- The "Magic" of Inorder

- This traversal has a very special and important property:

- When you perform an Inorder traversal on a Binary Search Tree (BST), you visit the nodes in ascending sorted order.

```python
def inorder_traversal(root):
    result = []
    if root:
        # 1. Traverse Left
        result.extend(inorder_traversal(root.left))
        # 2. Visit Root
        result.append(root.val)
        # 3. Traverse Right
        result.extend(inorder_traversal(root.right))
    return result
```

```python
def inorder_traversal_iterative(root):
    result = []
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)

        current = current.right
    return result
```


## Postorder Traversal (Left -> Right -> Root)

You can probably guess the pattern by now! This time, we visit the root node last.

    Traverse the Left subtree.
    Traverse the Right subtree.
    Visit the Root node.

```python
def postorder_traversal(root):
    result = []
    if root:
        # 1. Traverse Left
        result.extend(postorder_traversal(root.left))
        # 2. Traverse Right
        result.extend(postorder_traversal(root.right))
        # 3. Visit Root
        result.append(root.val)
    return result
```


Iterative Postorder (The Clever Trick)

Instead of a complex one-stack solution, we can get the Postorder traversal by slightly modifying the Preorder traversal we already know.

    Remember the Preorder traversal order: Root -> Left -> Right.
    Let's create a modified Preorder traversal with the order: Root -> Right -> Left. The code for this is almost identical to the standard iterative Preorder; we just visit the left child after the right.
    If we take the result of this modified traversal and reverse it, we get Left -> Right -> Root, which is exactly the Postorder traversal!


```python
def postorder_traversal_iterative(root):
    if not root:
        return []
    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result[::-1]
```

## Level Order Traversal (BFS)

The Right Tool for the Job: A Queue

To achieve this level-by-level exploration, we can't use a stack. A stack is LIFO (Last-In, First-Out), which gives us depth. We need a Queue, which is FIFO (First-In, First-Out).


```python
from collections import deque

def level_order_traversal(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []
    while queue:
        level_size = len(queue)
        current_level = []

        for i in range(level_size):
            n = queue.popleft()
            current_level.append(n.val)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)

        result.append(current.level)
    return result
```

# Traversal Strategy: DFS vs. BFS

## Core Differences
- **DFS (Depth-First Search):**
    - **Strategy:** Goes deep.
    - **Data Structure:** Stack (LIFO), often via recursion.
    - **Flavors:** Preorder, Inorder, Postorder.
- **BFS (Breadth-First Search):**
    - **Strategy:** Goes wide.
    - **Data Structure:** Queue (FIFO).
    - **Flavor:** Level Order Traversal.

## Complexity
- **Time Complexity:** $O(N)$ for both.
- **Space Complexity:**
    - **DFS:** $O(H)$ (Height of tree). Better for wide trees.
    - **BFS:** $O(W)$ (Max Width of tree). Better for deep, narrow trees.

## When to Use Which
- **Use BFS for:**
    - Shortest path problems.
    - Any problem related to tree levels.
    - Finding nodes closer to the root.
- **Use DFS for:**
    - Checking path existence.
    - Problems requiring full subtree processing (e.g., BST validation).
    - Problems where recursion is a natural fit.
    - When the tree is very wide.


## Max Depth

- find the max (left + right) + 1 calling left , right recursively

```python
def maxDepth(root):
    # Base case: an empty tree has a depth of 0
    if not root:
        return 0
    
    # Recursively find the depth of the left and right subtrees
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    # The depth of the tree is 1 (for the current node) + the max of the two subtrees
    return 1 + max(left_depth, right_depth)
```