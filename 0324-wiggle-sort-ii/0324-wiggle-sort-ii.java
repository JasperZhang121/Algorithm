class Solution {
    public void wiggleSort(int[] nums) {
        
        Arrays.sort(nums);
        int [] temp = new int[nums.length];
        
        for(int i=0; i<nums.length;i++){
            temp[i] = nums[i];
        }
        
        int mid = (nums.length+1)/2 -1;
        int end = nums.length-1;
        
        for (int i = 0 ; i<nums.length;i++){
            nums[i] = (i%2==1)? temp[end--]:temp[mid--];
        }
    }
}