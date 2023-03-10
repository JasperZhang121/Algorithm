class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # use dp for solving 
        
        # each pos in dp array is the max number we can get from previous subarry
        
        # if the current number larger than previous sub array
        
        # we record the current number meaning start a new array
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            max_sum = max(dp[i], max_sum)
        return max_sum