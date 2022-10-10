# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        l = []
        if not root:
            return l
        
        def hel(n,le):
            if len(l)==le:
                l.append([])
            l[le].append(n.val)
            if n.left:
                hel(n.left,le+1)
            if n.right:
                hel(n.right,le+1)
        hel(root,0)
        return l