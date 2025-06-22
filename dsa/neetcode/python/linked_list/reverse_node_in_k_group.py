# Key Observations:
# We can treat the problem segment-wise: cut the list into chunks of size k.

# For each chunk:

# If it's of length k: reverse it.

# If it’s less than k: don’t reverse, just keep it as it is.

# After reversing a group, we must connect it properly to the previous and next parts of the list.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            # now reverse the linked list
            prev, cur = kth.next, groupPrev.next
            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            # most important logic and complex one to remember
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next
                
        

    def getKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur