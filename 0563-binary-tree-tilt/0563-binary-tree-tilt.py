# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        
        def dfs(node):
            
            temp = 0
            
            if not node: return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            self.res += abs(l-r)
            
            return l+r+node.val
        
        dfs(root)
        return self.res
                      
            
                