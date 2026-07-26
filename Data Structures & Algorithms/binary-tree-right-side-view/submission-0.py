# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        q = deque([root])
        res = []
        while q:
            n = len(q)
            for _ in range(n):
                nd = q.popleft()

                if nd.left:
                    q.append(nd.left)
                if nd.right:
                    q.append(nd.right)
            res.append(nd.val)
        return res
        