class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            max_sum = max(dp[i], max_sum)
        return max_sum