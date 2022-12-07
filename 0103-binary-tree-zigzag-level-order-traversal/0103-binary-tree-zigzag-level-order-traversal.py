# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        
        queue = [root]
        next_ = []
        level = []
        res = []
        count  = 1
        
        while queue!=[]:
            for root in queue:
                level.append(root.val)
                if root.right:
                    next_.append(root.right)
                if root.left:
                    next_.append(root.left)
                    
            if count % 2==0:
                res.append(level)
            else:
                level.reverse()
                res.append(level)
            
            count+=1
            level = []
            queue = next_
            next_ = []
        return res
                
                