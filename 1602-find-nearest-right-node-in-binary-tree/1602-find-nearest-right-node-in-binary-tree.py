# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        
        q,level,next_= [root],[],[]
        
        while q:
            for cur in q:
                level.append(cur)
                if cur.left:
                    next_.append(cur.left)
                if cur.right:
                    next_.append(cur.right)
                
            if u in level:
                if level[-1]==u:
                    return None
                else:
                    a = level.index(u)+1
                    return level[a]
                
            q = next_
            level, next_ = [], []
            
            
        return None