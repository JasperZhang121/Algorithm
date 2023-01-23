"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        copy = Node(root.val)
        
        for c in root.children:
            copy.children.append(self.cloneTree(c))
        
        return copy