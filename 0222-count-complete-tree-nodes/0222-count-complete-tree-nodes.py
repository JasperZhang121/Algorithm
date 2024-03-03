# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        c = 0
        def dfs(node):
            if node:
                nonlocal c
                c+=1
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)       
        return c