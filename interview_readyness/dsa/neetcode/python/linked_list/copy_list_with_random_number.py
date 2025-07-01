"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        new_head = None
        ptr = head
        ctr = None

        hash_map = {
            None: None
        }

        while ptr is not None:
            # get the random index
            hash_map[ptr] = Node(ptr.val)
            ptr = ptr.next
        
        ptr = head
        while ptr is not None:
            copy = hash_map[ptr]
            copy.next = hash_map[ptr.next]
            copy.random = hash_map[ptr.random]
            ptr = ptr.next
        return hash_map[head]