# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        # use BFS
        queue, level, maxi, count, res = [root], [], root.val, 1, 1
        
        while True:
            while queue:
                node = queue.pop(0)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            
            queue = level
            if queue:
                count+=1
                temp = maxi
                maxi = max(sum([x.val for x in level if x]),maxi)
                if maxi != temp:
                    res = count
            level = []
            
            if not queue:
                return res
            
            
            
        


        
        
            