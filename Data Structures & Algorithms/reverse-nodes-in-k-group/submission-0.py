# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        gPrev = dummy

        while True:

            kth = gPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            gNext = kth.next

            prev = gNext
            cur = gPrev.next

            while cur != gNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = gPrev.next
            gPrev.next = kth
            gPrev = temp

        