# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symmetric(node_a, node_b):
            if not node_a and not node_b:
                return True
            if not node_a or not node_b:
                return False
            if node_b.val != node_a.val:
                return False
            return symmetric(node_a.left, node_b.right) and symmetric(node_a.right, node_b.left)
        
        return symmetric(root, root)        