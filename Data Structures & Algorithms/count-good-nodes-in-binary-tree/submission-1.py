# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # the key idea is to carry the largest value seen so far from the root to the current node

        from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        queue = deque([(root, root.val)])
        count = 0

        while queue:
            node, max_value = queue.popleft()

            if node.val >= max_value:
                count += 1

            new_max = max(max_value, node.val)

            if node.left:
                queue.append((node.left, new_max))

            if node.right:
                queue.append((node.right, new_max))

        return count


        