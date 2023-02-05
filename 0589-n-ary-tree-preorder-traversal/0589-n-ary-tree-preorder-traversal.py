"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        ret = []
        def dfs(node):
            if not node:
                return 
            ret.append(node.val)
            
            for x in node.children:
                dfs(x)
        
        dfs(root)
        return ret