# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if node is None:
                res.append("N")
                return
            
            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        dfs(root)

        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.i = 0

        def dfs():
            value = values[self.i]
            self.i += 1

            if value == "N":
                return None
            
            node = TreeNode(int(value))
            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()
