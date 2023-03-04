# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        lev,summ = 0,0
        def level(node,leve):
            if not node: return
            level(node.left,leve+1); level(node.right,leve+1)
            nonlocal lev
            lev = max(lev,leve)
        
        
        def helper(node,leve):
            nonlocal lev; nonlocal summ
            if not node: return 
            if not node.left and not node.right and lev==leve:
                summ+=node.val
            helper(node.left,leve+1); helper(node.right,leve+1)            
        
        level(root,0)
        helper(root,0)
        
        return summ
            