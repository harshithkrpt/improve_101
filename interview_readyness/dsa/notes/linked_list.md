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


## Double Linked List

- two pointers next & previous node
- traversal both forward and backward

```python
class DoublyNode:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None # The new addition!
```

### Linked List vs. Array: Time Complexity Cheat Sheet

| Operation             | Array / Python `list` | Singly Linked List | Notes                                                                   |
| :-------------------- | :-------------------- | :----------------- | :---------------------------------------------------------------------- |
| **Access (by index)** | `O(1)`                | `O(n)`             | Arrays have direct access; linked lists must traverse from the head.      |
| **Search (by value)** | `O(n)`                | `O(n)`             | In the worst case, both need to check every element.                    |
| **Insertion (Start)** | `O(n)`                | `O(1)`             | Arrays must shift all elements; linked lists just update the head.      |
| **Insertion (End)** | `O(1)` (amortized)    | `O(n)`* | Python lists are fast. *Linked lists must traverse to the end first.    |
| **Insertion (Middle)**| `O(n)`                | `O(n)`             | Both require finding the position, but arrays also need to shift.       |
| **Deletion (Start)** | `O(n)`                | `O(1)`             | Same logic as insertion at the start.                                   |
| **Deletion (End)** | `O(1)`                | `O(n)`             | Arrays have direct access to the end; linked lists must traverse.         |
| **Deletion (Middle)** | `O(n)`                | `O(n)`             | Both require finding the element to delete.                             |

---

### Space Complexity

* **Array / Python `list`**: `O(n)`
    * Stores `n` elements.
* **Linked List**: `O(n)`
    * Stores `n` elements, but has slightly more overhead because each of the `n` nodes also needs to store a pointer.


### Two Pointer Technique 

- we keep two pointers in linked list 'slow' and 'fast'
- slow = slow.next -> one step at a time
- fast = fast.next.next -> two steps at a time

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
```


### Floyd's Cycle-Finding Algorithm

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True


        return False
        
```


> https://leetcode.com/problems/remove-linked-list-elements/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        previous = dummy
        current = dummy
        while current is not None:
            if current.val == val:
                previous.next = current.next
                current = current.next
            else:
                previous = current
                current = current.next
        return dummy.next
```

https://leetcode.com/problems/reverse-linked-list/


- use three pointers and previous node , current node and next node 

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_node = None
        cur_node = head
        next_node = head.next if head else None
        
        
        while next_node is not None:
            cur_node.next = pre_node
            temp = next_node.next
            next_node.next = cur_node
            # make current node and previous node
            pre_node = cur_node
            cur_node = next_node
            next_node = temp
            
        
        return cur_node
        
        
```


- solution from gemini


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a pointer for the previous node. It starts as None
        # because the new tail of the list will point to nothing.
        previous_node = None
        
        # Start the current node pointer at the head of the list.
        current_node = head
        
        # Loop until we have processed the entire list.
        while current_node is not None:
            # 1. Save the next node before we break the link.
            #    We store it in a temporary variable.
            next_node_temp = current_node.next
            
            # 2. Reverse the actual pointer. This is the core step.
            #    The current node now points backward to the previous node.
            current_node.next = previous_node
            
            # 3. Move the previous_node pointer one step forward.
            #    For the next loop, our current node will be the previous one.
            previous_node = current_node
            
            # 4. Move the current_node pointer one step forward.
            #    We use the temporary variable we saved in step 1.
            current_node = next_node_temp
            
        # When the loop finishes, current_node is None, and previous_node
        # is at the new head of the reversed list.
        return previous_node
```

-- https://leetcode.com/problems/merge-two-sorted-lists/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_head = None
        lp = None
        while list1 is not None or list2 is not None:
                if list1 and list2:  
                    if list1.val <= list2.val:
                        if merged_head is None:
                            merged_head = list1
                            lp = merged_head
                        else:
                            lp.next = list1
                            lp = lp.next
                        
                        list1 = list1.next
                    else:
                        if merged_head is None:
                            merged_head = list2
                            lp = merged_head
                        else:
                            lp.next = list2
                            lp = lp.next
                        list2 = list2.next
                elif list1:
                    if merged_head is None:
                        merged_head = list1
                        lp = merged_head
                    else:
                        lp.next = list1
                        lp = lp.next

                    list1 = list1.next
                else:
                    if merged_head is None:
                        merged_head = list2
                        lp = merged_head
                    else:
                        lp.next = list2
                        lp = lp.next

                    list2 = list2.next
                        
        return merged_head
                        
```


-- better approach is to use dummy node for merge two sorted array

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
                        
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 if list1 else list2

        return dummy.next
```

-- https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

<!-- Hint: Creating a gap of size n is super important -->

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # calculate total size
        slow = head
        fast = head
        exp_gap = n
        cur_gap = 0
        prev = ListNode()
        dummy  = prev
        prev.next = head
        while fast or cur_gap != exp_gap:
            if fast:  
                if cur_gap != exp_gap:
                    fast = fast.next
                    cur_gap += 1
                else:
                    prev = slow
                    slow = slow.next
                    fast = fast.next
        
        if slow:
            prev.next = slow.next
        else:
            prev.next = None
        return dummy.next
```



<!-- check for palindrome in linked list -->

- find middle element
- second half reverse it
- compare head before middle with revsersed second half if all equal valid else not valid

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        cur = slow
        pre = None
        while cur is not None:
            next_ptr = cur.next
            cur.next = pre
            pre = cur
            cur = next_ptr
        # now loop till head does not rach slow pointer 
        is_valid = True
        print(slow.val)
        print(pre)
        while slow and head and head != slow:
            if pre.val != head.val:
                is_valid = False
                break
            head = head.next
            pre = pre.next
        return is_valid
```