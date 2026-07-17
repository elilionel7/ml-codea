# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: 
            return None
        elif len(lists) == 1:
            return lists[0]

        result = None
        for ls in lists:
            result = self._mergeTwo(result, ls)
        return result
    def _mergeTwo(self,l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = tail = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next




        