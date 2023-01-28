"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root: return []
        
        res,level,next_,q = ([] for i in range(4))
        q.append(root)
        while q:
            for x in q:
                level.append(x.val)
                for y in x.children:
                    next_.append(y)
            
            if level:
                res.append(level[:])
            q,level,next_ = next_,[],[]
        return res