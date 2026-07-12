# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next

        arr2 = []
        left, right = 0, len(arr) - 1

        while left <= right:
            arr2.append(arr[left])

            if left != right:
                arr2.append(arr[right])

            left += 1
            right -= 1

        cur = head

        for value in arr2:
            cur.val = value
            cur = cur.next