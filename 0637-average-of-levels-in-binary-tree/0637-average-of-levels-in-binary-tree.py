# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        res,queue,level,next_ = [],[root],[],[]
        
        while queue!=[]:
            for root in queue:
                level.append(root.val)
                if root.right:
                    next_.append(root.right)
                if root.left:
                    next_.append(root.left)
                
            res.append(sum(level)/len(level))
            queue,next_,level = next_,[],[]
        
        return res
        