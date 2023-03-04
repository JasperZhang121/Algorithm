# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        inorder, stack = [], []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            L = stack.pop()
            inorder.append(L.val)
            node = L.right
        return inorder