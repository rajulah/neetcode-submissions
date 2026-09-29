# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        
        i = 0
        j = len(nodes) - 1

        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1
        nodes[i].next = None
        # head = ListNode()
        # node = head
        # for i in range(len(nodes)):
        #     if i%2 == 0:
        #         head.next = nodes[i]
        #     else:
        #         head.next = nodes[len(nodes)-i-1]
        #     head = head.next
        # return node.next

        # def reverseList(node):
        #     if node is None:
        #         return None
        #     prev = None
        #     curr = node
        #     while curr:
        #         tmp = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = tmp
        #     return prev
        # reversedList = reverseList(head)
        
        