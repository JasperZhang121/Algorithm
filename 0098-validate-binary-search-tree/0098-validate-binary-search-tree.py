# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        '''
        Inorder traversal should return a sorted array for a BST. then check whether the sorted array           is sorted to tell whether it is a valid BST 
        '''
        
        path = [] 
        def dfs(node):
            if root:
                if node.left:
                    dfs(node.left)
                path.append(node.val)
                if node.right:
                    dfs(node.right)
        dfs(root)
        if len(path)==1:
            return True
        
        for i in range(1,len(path)):
            if path[i]<=path[i-1]:
                return False
        
        return True
                
                
        