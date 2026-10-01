# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        if head is None:
            return None
        node = head
        while node:
            length += 1
            node = node.next
        if n > length:
            return None
        fromFirst = length - n + 1
        if n == length:
            return head.next
        i = 1
        curr = head
        while i < fromFirst - 1:
            curr = curr.next
            i += 1
       
        tmp = curr.next
        curr.next = tmp.next if tmp else None
        print(curr.val, tmp.val)
        return head
        
