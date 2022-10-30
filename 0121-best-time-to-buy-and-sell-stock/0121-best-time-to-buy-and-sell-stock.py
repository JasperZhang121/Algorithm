class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minv = float('inf')
        maxv = 0
        for i in range(len(prices)):
            if prices[i]<minv:
                minv = prices[i]
            elif prices[i] - minv > maxv:
                maxv = prices[i]-minv
        return maxv
                
        