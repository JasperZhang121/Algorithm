class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        dp = [0]*len(nums)
        summ = 0 
        
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] == nums[i-1] - nums[i-2]:                
                dp[i] = 1+dp[i-1]
                summ+=dp[i]
        return summ
                       
        
        