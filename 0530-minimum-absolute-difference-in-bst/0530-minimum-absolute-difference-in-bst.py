# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        lis,res = [],10000000000
        
        def dfs(node):
            if not node:
                return
            lis.append(node.val)
            dfs(node.left)
            dfs(node.right)
          
        dfs(root)
        
        lis = sorted(lis)
        
        for i in range(1,len(lis)):
            if lis[i]-lis[i-1]<res:
                res = lis[i]-lis[i-1]
        
        return res
            