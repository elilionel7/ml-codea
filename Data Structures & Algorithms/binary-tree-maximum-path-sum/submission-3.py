
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.res = -float("inf")

        def dfs(root):
            if root is None:
                return 0
            
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            
            cur_path = root.val + left + right
            self.res = max(self.res, cur_path)

            return root.val + max(left, right)

        dfs(root)

        return self.res

        

        