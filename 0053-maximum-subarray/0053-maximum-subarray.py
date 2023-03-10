class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # use dp for solving 
        
        # each pos in dp array is the max number at that position we can get from any possible combination of previous subarrys
        # even it decreases, but it is the max in that position
        
        # if the current number > previous sub array + current number (meaning previous is negative) 
        # we record the current number meaning start a new array
        
        # else the current number < previous sub array + current number (the max number we can get so far at this positon even it decreases)
        # record the sum
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            max_sum = max(dp[i], max_sum)
        return max_sum