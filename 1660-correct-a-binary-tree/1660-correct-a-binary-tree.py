# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        
        
        seen = set()
        
        def dfs(root):
            if not root or (root.right and root.right.val in seen):
                return
            seen.add(root.val)
            root.right = dfs(root.right)
            root.left = dfs(root.left)
            return root
            
        return dfs(root)
            
                