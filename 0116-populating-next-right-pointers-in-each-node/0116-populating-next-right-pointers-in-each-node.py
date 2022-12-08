"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root == None:
            return None
        
        # BSF
        
        queue = [root]
        next_que = []
        level = []
        res = []
        
        while queue!=[]:
            for x in queue:
                level.append(x)
                if x.left:
                    next_que.append(x.left)
                if x.right:
                    next_que.append(x.right)
            
            res.append(level) 
            queue = next_que
            level = []
            next_que = []
        
        for x in res:
            for i in range(len(x)):
                if i+1!=len(x):
                    x[i].next = x[i+1]
                else:
                    x[i].next = None
        
        return root
        
                
            