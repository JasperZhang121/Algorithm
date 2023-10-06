class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [1] * (n + 1)

        for i in range(2, n + 1):
            max_res = 1
            for right in range(2, i):
                left = i - right
                max_res = max(max_res, left * right, left * dp[right])
            dp[i] = max_res
        
        return dp[n]
        