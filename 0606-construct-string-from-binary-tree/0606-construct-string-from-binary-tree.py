# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        if not root:
            return ''
        
        if not root.left and not root.right:
            return str(root.val)
        
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        return f'{root.val}({left})' + (f'({right})' if right else '')