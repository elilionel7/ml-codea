# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        q = deque([root])
        res = []

        while q:
            n = len(q)
            level = []
            for i in range(n):
                nd = q.popleft()
                level.append(nd.val)

                if nd.left:
                    q.append(nd.left)
                if nd.right:
                    q.append(nd.right)
            res.append(level)
        return res
        