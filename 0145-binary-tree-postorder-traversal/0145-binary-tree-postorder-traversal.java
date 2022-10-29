/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    ArrayList arr = new ArrayList<Integer>();
    public List<Integer> postorderTraversal(TreeNode root) {
       
        helper(root);
        return arr;
    }
    
    public void helper(TreeNode node){
        if (node==null) return;
        if (node.left==null && node.right==null){
            arr.add(node.val);
            return;
        }
        
        if (node.left!=null) {
            helper(node.left);
        }
         
        if (node.right!=null){
            helper(node.right);
        }
        arr.add(node.val);
        
    }
}