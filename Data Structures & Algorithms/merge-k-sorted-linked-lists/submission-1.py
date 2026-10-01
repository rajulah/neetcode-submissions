# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1, l2) -> Optional[ListNode]:
            if l1 is None or l2 is None:
                return l1 or l2
            dummy = ListNode(0)
            curr = dummy
            while l1 or l2:
                if l1 and l2 and l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                elif l1 and l2 and l1.val > l2.val:
                    curr.next = l2
                    l2 = l2.next
                elif l1:
                    curr.next = l1
                    break
                else:
                    curr.next = l2
                    break
                curr = curr.next
            return dummy.next
        
        if len(lists) == 0 or lists is None:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(mergeTwoLists(l1,l2))
            lists = mergedLists
        return lists[0]

        

