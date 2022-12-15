class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if nums==[]:return 0
        
        n = len(nums)
        dp = [0]*(n+1)
        dp[1] = nums[0]
        
        for i in range(1,n):
            dp[i+1] = max(dp[i],dp[i-1]+nums[i])
        
        return dp[n]
    