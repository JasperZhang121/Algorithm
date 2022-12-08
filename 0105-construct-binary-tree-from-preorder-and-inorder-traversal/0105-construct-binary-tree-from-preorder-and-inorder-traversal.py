# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build (preL, preR, InL, InR):
            if preL>preR or InL>InR: return None
             
            index_root = index[preorder[preL]]
            left_size = index_root-InL
            
            root = TreeNode(preorder[preL])
            root.left = build(preL+1, preL+left_size, InL, index_root-1)
            root.right = build(preL+1+left_size, preR, index_root+1,InR)
            return root
        
        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i
        n = len(preorder)
        return build(0,n-1,0,n-1)
                
            