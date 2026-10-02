# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def rev(node: Optional[ListNode]) -> Optional[ListNode]:
            if node is None:
                return None
            prev = None
            curr = node
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        
        i = 1
        curr = head
        currHead = head
        finalHead = None
        prevTail = None
        while curr:
            if i % k == 0:
                tmp = curr.next
                curr.next = None
                reversedHead = rev(currHead)
                currHead.next = tmp
                if finalHead is None:
                    finalHead = reversedHead
                if prevTail:
                    prevTail.next = reversedHead
                prevTail = currHead
                prevTail.next = tmp
                currHead = tmp
                curr = tmp
            else:
                curr = curr.next
            i += 1

        return finalHead if finalHead else head

