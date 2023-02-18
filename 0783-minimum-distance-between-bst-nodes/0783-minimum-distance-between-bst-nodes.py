# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        res = []
        def dfs(node):
            
            nonlocal res
            
            if not node:
                return
            
            
            
            res.append(node.val)
        
            dfs(node.left); dfs(node.right)
        
        
        dfs(root)
        res.sort()
        
        diff = 1000000
        for i in range(1,len(res)):
            diff = min(res[i]-res[i-1],diff)
        
        return int(diff)
        