# Linked List

- linked list is a chain of nodes , with two pieces -> a data & a pointer node.
- first node is called head, 
- last nodes last pointer will be null

 
 [ Head ]
     |
     v
+-------+    +-------+    +-------+
| Data  | -> | Data  | -> | Data  | -> null
+-------+    +-------+    +-------+
  Node 1       Node 2       Node 3


```python

    class Node:
        def __init__(self, data):
            self.data = data
            seld.next = None
    
    node1 = Node(10)
    node2 = Node(20)
    node1.next = node2
```

Why use a linked list instead of a simple array (or a Python list)?

Array Vs Linked List

Memory : Array continuous memory , linked list stors any where
Element Access: O(1) in array, O(n) in linked list
Insertion/Deletion: O(n) in array, O(1) in linked list


Types of Linked List:

- Singly Linked List 
    Singly Linked List: The one we've been discussing. Each node has one pointer, and it points forward to the next node.
- Doubly Linked List
    Doubly Linked List: This is like a train with couplers on both ends of each car. Each node has two pointers: one pointing to the next node and one pointing to the previous node. This lets us travel both forwards and backwards!
- Circular Linked List
    Circular Linked List: The next pointer of the last node doesn't point to null. Instead, it loops back and points to the Head (the first node), creating a circle.


```python
    # First, let's redefine our Node class for clarity
    class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # A function to print all elements of a list
    def print_list(head):
    current = head  # Start at the beginning
    
    while current is not None:
        print(current.data, end=" -> ") # Visit the node
        current = current.next # Move to the next node
        
    print("null") # Print null at the end

    # --- Let's build the list: 10 -> 20 -> 30 -> null ---
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)

    # --- Now, let's traverse it! ---
    print_list(head) 
    # Expected Output: 10 -> 20 -> 30 -> null
```

### Insert at beginning

```python
    # (Assuming our Node class is already defined)

    def insert_at_beginning(head, data_to_insert):
    # 1. Create the new node
    new_node = Node(data_to_insert)
    
    # 2. Make the new node point to the old head
    new_node.next = head
    
    # 3. The new node is now the head!
    return new_node

    # --- Let's test it ---
    # Start with a simple list
    head = Node(10)
    head.next = Node(20)

    print("Original list:")
    print_list(head) # Output: 10 -> 20 -> null

    # Now, insert 5 at the beginning
    head = insert_at_beginning(head, 5)

    print("New list:")
    print_list(head) # Output: 5 -> 10 -> 20 -> null
```

### Insert at end

```python
    def insert_at_end(head, data_to_insert):
    new_node = Node(data_to_insert)
    
    # If the list is empty, the new node is the head
    if head is None:
        return new_node
        
    # 1. Traverse to the end of the list
    current = head
    while current.next is not None:
        current = current.next
        
    # 2. Link the last node to our new node
    current.next = new_node
    return head
```

### Insertion in the Middle

```python
    # Let's say we want to insert 'C' after node 'B' in the list A -> B -> D
    def insert_after_node(prev_node, data_to_insert):
    if prev_node is None:
        print("Previous node cannot be null")
        return
        
    # 1. Create the new node
    new_node = Node(data_to_insert)
    
    # 2. Store the original next node (just as you said!)
    original_next = prev_node.next
    
    # 3. Link the previous node to our new node
    prev_node.next = new_node
    
    # 4. Link the new node to the original next node
    new_node.next = original_next
```


### Delete first node

```python
    def delete_first_node(head):
    # If the list is empty, there's nothing to delete
    if head is None:
        return None
        
    # The new head is simply the next node
    new_head = head.next
    return new_head

    # --- Let's test it ---
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)

    print("Original list:")
    print_list(head) # Output: 10 -> 20 -> 30 -> null

    # Now, delete the first node
    head = delete_first_node(head)

    print("New list:")
    print_list(head) # Output: 20 -> 30 -> null
```

### Deleting the Last Node

```python
    def delete_last_node(head):
    # Handle empty list or list with one node
    if head is None or head.next is None:
        return None
        
    # Traverse until the second-to-last node
    current = head
    while current.next.next is not None:
        current = current.next
        
    # Unlink the last node
    current.next = None
    return head
```


### delete a node in middle with value

```python
def delete_by_value(head, key):
  # Handle case where the list is empty
  if head is None:
    return None

  # Handle case where the head node itself holds the key
  if head.data == key:
    return head.next

  # Traverse to find the key, keeping track of the previous node
  current = head
  while current.next is not None and current.next.data != key:
    current = current.next
  
  # If the key was found, current is now the node BEFORE the one to delete
  if current.next is not None:
    node_to_delete = current.next
    current.next = node_to_delete.next # Bypass the node
    
  return head

# --- Let's test it ---
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Original list:")
print_list(head) # Output: 10 -> 20 -> 30 -> null

# Now, delete the node with value 20
head = delete_by_value(head, 20)

print("New list:")
print_list(head) # Output: 10 -> 30 -> null    
```


### Search

```python
    def search(head, key):
  """
  Searches for a key in the linked list.
  Returns True if found, False otherwise.
  """
  current = head # Start at the beginning
  
  while current is not None:
    if current.data == key:
      return True # Found it!
    current = current.next # Move to the next node
    
  return False # Reached the end, not found.

# --- Let's test it ---
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print(f"Is 20 in the list? {search(head, 20)}") # Expected Output: Is 20 in the list? True
print(f"Is 40 in the list? {search(head, 40)}") # Expected Output: Is 40 in the list? False
```