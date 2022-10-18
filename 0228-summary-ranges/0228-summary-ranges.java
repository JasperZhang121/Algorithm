class Solution {
    public List<String> summaryRanges(int[] nums) {
      
        List<String> list = new ArrayList();
        if (nums==null || nums.length==0) return list;

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            while(i<nums.length-1 && nums[i]+1==nums[i+1]){
                i++;
            }
            if (num!=nums[i]){
                list.add(num+"->"+nums[i]);
            } else {
                list.add(num+"");
            }
        }
        return list;  
    }
}