class Solution {
    public int[] getConcatenation(int[] nums) {
        var res = new int[nums.length*2];
        for (int i = 0; i < nums.length*2; i++) {
            res[i] = nums[i% nums.length];
        }
        return res;     
    }
}