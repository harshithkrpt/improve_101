# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for i in range(n):
            if fast:
                fast = fast.next
        slow = head
        dummy = ListNode()
        dummy.next = slow
        pre = dummy
        while fast:
            pre = slow
            fast = fast.next
            slow = slow.next
        if pre.next:
            pre.next = slow.next
        else:
            pre.next = None
        return dummy.next