# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKthNode(self,node, k):
            while node and k>0:
                node = node.next
                k -= 1
            return node
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKthNode(groupPrev, k)
            if kth is None:
                return dummy.next
            groupNext = kth.next

            prev = kth.next
            curr = groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            oldGroupStart = groupPrev.next
            groupPrev.next = kth
            groupPrev = oldGroupStart

        return dummy.next

        

        