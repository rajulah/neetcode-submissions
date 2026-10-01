# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        for _ in range(n+1):
            fast = fast.next
        # n+ 1 because dummy is at 0th place before head
        while fast:
            slow = slow.next
            fast = fast.next
        
        # now slow is before nth node form the last, because there are exactly n nodes between fast and slow.
        slow.next = slow.next.next

        return dummy.next
        
