# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is empty:
        #     return True

        # If root is empty:
        #     return False

        # Create a queue containing root

        # While the queue is not empty:
        #     Remove the next node

        #     If the current node's value equals subRoot's value:
        #         Check whether the tree starting at current node
        #         is exactly the same as subRoot

        #         If they are the same:
        #               return True

        #     Add the current node's left child to the queue
        #     Add the current node's right child to the queue

        # If no matching subtree was found:
        # return False

        if subRoot is None:
            return True
        
        if root is None:
            return False
        
        queue = deque([root])

        while queue:
            n = queue.popleft()

            if n.val == subRoot.val:
                if self.sameTree(n, subRoot):
                    return True
            
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        return False
            


    def sameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Create a queue containing the pair (node1, node2)

        # While the queue is not empty:
        #     Remove a pair of nodes

        #     If both nodes are empty:
        #         continue

        #     If only one node is empty:
        #         return False

        #     If their values are different:
        #         return False

        #     Add their left children as a pair
        #     Add their right children as a pair

        # Return True
        if root1 is None and root2 is None:
            return True
        queue = deque([(root1, root2)])

        while queue:
            n1, n2 = queue.popleft()

            if n1 is None and n2 is None:
                continue
            
            if n1 is None or n2 is None:
                return False
            
            if n1.val != n2.val:
                return False
            
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))
        return True
