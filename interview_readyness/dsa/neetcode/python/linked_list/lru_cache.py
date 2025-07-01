# Real-Life Analogy:
# Imagine a small office fridge that only holds 3 lunch boxes. When a 4th lunch comes in:

# The oldest (least recently accessed) lunch box is thrown out.

# Recently accessed lunch boxes are kept.

# Core Concepts:
# Hash Map gives O(1) access to values via keys.

# Doubly Linked List maintains the order of usage:

# Most recently used at front (head).

# Least recently used at end (tail).

# We can insert and remove nodes in O(1) time.

# Why Doubly Linked List + HashMap?
# HashMap: key → node (for fast lookup)

# Doubly Linked List: maintain usage order (move to front on access, remove from end on overflow)

class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # dummy left and right pointers for resolving edge cases
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    # remove element from node
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    # add elements to right
    def add(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        # remove the lru
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            # delete from cache
            del self.cache[lru.key]