# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        # if list1 is None and list2 is None:
        #     return None
        # if list1 is None:
        #     return list2
        # if list2 is None:
        #     return list1
        # if list1.val <= list2.val:
        #     newHead = ListNode(list1.val)
        #     list1 = list1.next
        # else:
        #     newHead = ListNode(list2.val)
        #     list2 = list2.next
        node = newHead
        while list1 and list2:
            if list1.val < list2.val:
                newHead.next = list1
                list1 = list1.next
            else:
                newHead.next = list2
                list2 = list2.next
            newHead = newHead.next
        newHead.next = list1 or list2
        return node.next       
        