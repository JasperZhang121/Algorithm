class Solution {
    public int[] runningSum(int[] nums) {
       var res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            var total = 0;
            for (int j = 0; j <=i; j++) {
                total+=nums[j];
            }
            res[i]=total;
        }
        return res;
    }
} 