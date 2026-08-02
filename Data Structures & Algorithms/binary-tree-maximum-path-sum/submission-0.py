
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -float('inf')
        def dfs(root):
            if not root:
                return
            
            left = self._getMax(root.left)
            right = self._getMax(root.right)
            self.res = max(self.res, root.val + left + right)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res
    
    def _getMax(self, root: Optional[TreeNode]) -> int: 
        if not root:
            return 0
        
        left = self._getMax(root.left)
        right = self._getMax(root.right)
        path = root.val + max(left, right)

        return max(0, path)
        