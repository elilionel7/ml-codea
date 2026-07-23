# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        

        queue = deque([(p,q)])


        while queue:
            pn, qn = queue.popleft()

            if pn is None and qn is None:
                continue
            
            if pn is None or qn is None:
                return False

            if pn.val != qn.val:
                return False
            
            queue.append((pn.left, qn.left))
            queue.append((pn.right, qn.right))
        return True
            
            
        
        