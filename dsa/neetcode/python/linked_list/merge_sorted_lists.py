# ✅ Optimal Strategy 2: Divide & Conquer
# Analogy: Merge like merge sort – pair up lists and merge them recursively.

# 🧩 Step-by-step:
# Recursively divide the k lists into pairs.

# Merge each pair of lists.

# Merge the results of those pairs, until you're left with one list.

# Why this is good:
# You're merging two lists at a time (which is efficient: O(n)).

# You're reducing problem size logarithmically.

# ⏱ Time: O(N log k)
# 📦 Space: O(log k) (due to recursion)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        # run the loop till length becomes 1
        while len(lists) > 1:
            mergeMe = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i + 1 < len(lists) else None
                mergeMe.append(self.mergeTwoLists(list1, list2))
            lists = mergeMe
        
        return lists[0]
    
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        ptr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        ptr.next = l1 if l1 else l2
        return dummy.next
