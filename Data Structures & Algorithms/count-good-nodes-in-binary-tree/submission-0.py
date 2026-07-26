# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # the key idea is to carry the largest value seen so far from the root to the current node

        def dfs(node, max_value):
            if node is None:
                return 0
            
            good = 0

            if node.val >= max_value:
                good = 1
            
            max_value = max(max_value, node.val)

            left_good = dfs(node.left, max_value)
            right_good = dfs(node.right, max_value)

            return good + left_good + right_good
        
        return dfs(root, root.val)


        